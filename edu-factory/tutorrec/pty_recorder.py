"""Grabador de terminal real a formato asciinema (.cast).

Abre el shell interactivo real del usuario (Powerlevel10k, zsh, plugins,
Nerd Fonts...) dentro de un PTY controlado, envía los comandos como teclas
con timing cinematográfico y captura el stream resultante como un archivo
`.cast` v2, reproducible con `asciinema play` o convertible con agg/ffmpeg.
"""

from __future__ import annotations

import fcntl
import json
import os
import pty
import select
import signal
import struct
import sys
import termios
import threading
import time
from pathlib import Path
from typing import Any

from tutorrec.human_typing import delay_caracter, pausa_post_enter, pausa_pensando
from tutorrec.output_simulator import es_comando_largo


class PtyAsciinemaRecorder:
    """Graba un shell interactivo real en un PTY y lo guarda como .cast."""

    def __init__(
        self,
        shell: str | None = None,
        velocidad_base: float = 0.04,
        pausas_naturales: bool = True,
        limpiar_entre_comandos: bool = True,
        mostrar_descripcion: bool = False,
        timeout_idle: float = 1.2,
        pausa_post_default: float | None = None,
    ) -> None:
        # Preferir zsh (p10k) para grabaciones profesionales
        candidato = shell or os.environ.get("TUTORREC_SHELL") or os.environ.get("SHELL")
        if not candidato or os.path.basename(candidato) not in ("zsh", "zsh5"):
            for ruta in ("/bin/zsh", "/usr/bin/zsh"):
                if os.path.exists(ruta):
                    candidato = ruta
                    break
            else:
                candidato = candidato or "/bin/bash"
        self.shell = candidato
        self.velocidad_base = velocidad_base
        self.pausas_naturales = pausas_naturales
        self.limpiar_entre_comandos = limpiar_entre_comandos
        self.mostrar_descripcion = mostrar_descripcion
        self.timeout_idle = timeout_idle
        if pausa_post_default is None:
            pausa_post_default = float(os.environ.get("TUTORREC_PAUSA_FINAL", "5.0"))
        self.pausa_post_default = pausa_post_default

    def grabar(self, comandos: list[dict[str, Any]], salida: str) -> int:
        inicio = time.monotonic()
        frames: list[tuple[float, str, str]] = []
        frames_lock = threading.Lock()
        estado = {"ultima": time.monotonic(), "cerrado": False}

        # Tamaño fijo profesional para p10k multi-línea (override con TUTORREC_COLS/ROWS)
        columnas = int(os.environ.get("TUTORREC_COLS", "100"))
        filas = int(os.environ.get("TUTORREC_ROWS", "28"))

        # ZDOTDIR: zshrc de grabación (p10k, fondo #000000, sin autosuggestions)
        zdot = os.environ.get(
            "TUTORREC_ZDOTDIR",
            str(Path(__file__).resolve().parent / "zdot"),
        )

        pid, maestro = pty.fork()
        if pid == 0:
            os.environ["TERM"] = os.environ.get("TUTORREC_TERM", "xterm-256color")
            os.environ["COLORTERM"] = "truecolor"
            os.environ["ZDOTDIR"] = zdot
            os.environ["POWERLEVEL9K_INSTANT_PROMPT"] = "off"
            os.execvpe(self.shell, [self.shell, "-i"], os.environ)
            os._exit(127)

        self._fijar_tamano(maestro, columnas, filas)

        def capturar(datos: bytes) -> None:
            now = time.monotonic()
            with frames_lock:
                frames.append((now - inicio, "o", datos.decode("utf-8", "replace")))
                estado["ultima"] = now

        def lector() -> None:
            try:
                while True:
                    r, _, _ = select.select([maestro], [], [], 0.2)
                    if not r:
                        continue
                    data = os.read(maestro, 65536)
                    if not data:
                        break
                    capturar(data)
            except OSError:
                pass
            finally:
                estado["cerrado"] = True

        hilo = threading.Thread(target=lector, daemon=True)
        hilo.start()

        def drenar() -> None:
            while True:
                r, _, _ = select.select([maestro], [], [], 0.0)
                if not r:
                    return
                data = os.read(maestro, 65536)
                if not data:
                    return
                capturar(data)

        def esperar_idle(tope: float = 90.0, umbral: float | None = None) -> None:
            lim = self.timeout_idle if umbral is None else umbral
            inicio = time.monotonic()
            while True:
                drenar()
                if estado["cerrado"]:
                    return
                if time.monotonic() - estado["ultima"] >= lim:
                    return
                if time.monotonic() - inicio >= tope:
                    return
                time.sleep(0.05)

        def enviar(datos: bytes) -> None:
            try:
                os.write(maestro, datos)
            except OSError:
                pass

        def limpiar() -> None:
            if self.limpiar_entre_comandos:
                # Ctrl+L + ANSI full clear (prompts multi-línea de p10k)
                enviar(b"\x0c")
                time.sleep(0.15)
                enviar(b"\x1b[H\x1b[2J\x1b[3J")
                time.sleep(0.25)

        def teclear(texto: str) -> None:
            for car in texto:
                enviar(car.encode("utf-8"))
                time.sleep(delay_caracter(car, self.velocidad_base, self.pausas_naturales))

        try:
            esperar_idle(tope=25.0)
            limpiar()
            esperar_idle(tope=10.0)

            for i, paso in enumerate(comandos):
                comando = str(paso.get("comando", "")).strip()
                descripcion = paso.get("descripcion", "")
                pausa_post = float(paso.get("pausa_post", self.pausa_post_default))
                largo = es_comando_largo(comando)
                # Largos (red/instalaciones): más margen de idle y tope mayor
                # para que el scroll se muestre entero
                idle_cmd = 3.5 if largo else self.timeout_idle
                tope_cmd = 240.0 if largo else 90.0

                if self.mostrar_descripcion and descripcion:
                    enviar(f"\n# {descripcion}\n".encode("utf-8"))
                    time.sleep(0.4)
                    limpiar()
                    esperar_idle()

                pausa_pensando(self.pausas_naturales)
                teclear(comando)
                time.sleep(0.2)
                enviar(b"\r")
                pausa_post_enter(self.pausas_naturales)
                esperar_idle(tope=tope_cmd, umbral=idle_cmd)

                if self.pausas_naturales:
                    # Hold final (5s por defecto) para leer la salida
                    time.sleep(pausa_post)

                # Último drenaje por si llegó output tardío
                drenar()

                if self.limpiar_entre_comandos and i < len(comandos) - 1:
                    limpiar()
                    esperar_idle()

            enviar(b"\x04")
            time.sleep(0.8)
        finally:
            try:
                enviar(b"\x04")
                os.close(maestro)
            except OSError:
                pass
            hilo.join(timeout=3)

        self._reap(pid)

        with frames_lock:
            lineas = list(frames)
        return self._escribir_cast(lineas, salida, columnas, filas)

    def _reap(self, pid: int, timeout: float = 5.0) -> None:
        """Recoge el shell del PTY sin bloquear si no termina solo."""
        limite = time.monotonic() + timeout
        while time.monotonic() < limite:
            try:
                wpid, _ = os.waitpid(pid, os.WNOHANG)
            except ChildProcessError:
                return
            except OSError:
                return
            if wpid == pid:
                return
            time.sleep(0.05)
        for senal in (signal.SIGTERM, signal.SIGKILL):
            try:
                os.kill(pid, senal)
            except (ProcessLookupError, OSError):
                return
            fin = time.monotonic() + 2.0
            while time.monotonic() < fin:
                try:
                    wpid, _ = os.waitpid(pid, os.WNOHANG)
                except (ChildProcessError, OSError):
                    return
                if wpid == pid:
                    return
                time.sleep(0.05)

    def _fijar_tamano(self, fd: int, columnas: int, filas: int) -> None:
        try:
            fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", filas, columnas, 0, 0))
        except OSError:
            pass

    def _escribir_cast(
        self,
        frames: list[tuple[float, str, str]],
        salida: str,
        columnas: int,
        filas: int,
    ) -> int:
        # Tema embebido: fondo negro puro #000000 (agg --theme custom lo usa)
        paleta = ":".join(
            [
                "#000000",
                "#ff5555",
                "#50fa7b",
                "#f1fa8c",
                "#bd93f9",
                "#ff79c6",
                "#8be9fd",
                "#f8f8f2",
                "#6272a4",
                "#ff6e6e",
                "#69ff94",
                "#ffffa5",
                "#d6acff",
                "#ff92df",
                "#a4ffff",
                "#ffffff",
            ]
        )
        cabecera = {
            "version": 2,
            "width": columnas,
            "height": filas,
            "timestamp": int(time.time()),
            "idle_time_limit": 2,
            "env": {
                "SHELL": self.shell,
                "TERM": os.environ.get("TUTORREC_TERM", "xterm-256color"),
                "COLORTERM": "truecolor",
            },
            "theme": {
                "fg": "#f8f8f2",
                "bg": "#000000",
                "palette": paleta,
            },
        }
        with open(salida, "w", encoding="utf-8") as f:
            f.write(json.dumps(cabecera) + "\n")
            for momento, tipo, datos in frames:
                if not datos:
                    continue
                f.write(json.dumps([round(momento, 4), tipo, datos]) + "\n")
        return 0


__all__ = ["PtyAsciinemaRecorder"]