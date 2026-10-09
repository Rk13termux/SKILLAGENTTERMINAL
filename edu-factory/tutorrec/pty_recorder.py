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
import shutil
import struct
import sys
import termios
import threading
import time
from typing import Any

from tutorrec.human_typing import delay_caracter, pausa_post_enter, pausa_pensando


def _tam_terminal() -> tuple[int, int]:
    try:
        tam = shutil.get_terminal_size()
        return tam.columns, tam.lines
    except Exception:
        return 80, 24


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
    ) -> None:
        self.shell = shell or os.environ.get("SHELL") or "/bin/bash"
        self.velocidad_base = velocidad_base
        self.pausas_naturales = pausas_naturales
        self.limpiar_entre_comandos = limpiar_entre_comandos
        self.mostrar_descripcion = mostrar_descripcion
        self.timeout_idle = timeout_idle

    def grabar(self, comandos: list[dict[str, Any]], salida: str) -> int:
        inicio = time.monotonic()
        frames: list[tuple[float, str, str]] = []
        frames_lock = threading.Lock()
        estado = {"ultima": time.monotonic(), "cerrado": False}

        columnas, filas = _tam_terminal()

        pid, maestro = pty.fork()
        if pid == 0:
            os.environ["TERM"] = os.environ.get("TUTORREC_TERM", "xterm-256color")
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

        def esperar_idle(tope: float = 120.0) -> None:
            while True:
                drenar()
                if estado["cerrado"]:
                    return
                if time.monotonic() - estado["ultima"] >= self.timeout_idle:
                    return
                time.sleep(0.05)

        def enviar(datos: bytes) -> None:
            try:
                os.write(maestro, datos)
            except OSError:
                pass

        def limpiar() -> None:
            if self.limpiar_entre_comandos:
                enviar(b"\x0c")

        def teclear(texto: str) -> None:
            for car in texto:
                enviar(car.encode("utf-8"))
                time.sleep(delay_caracter(car, self.velocidad_base, self.pausas_naturales))

        try:
            esperar_idle()
            limpiar()
            esperar_idle()

            for i, paso in enumerate(comandos):
                comando = str(paso.get("comando", "")).strip()
                descripcion = paso.get("descripcion", "")
                pausa_post = float(paso.get("pausa_post", 1.6))

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
                esperar_idle()

                if self.pausas_naturales:
                    time.sleep(pausa_post)

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

        try:
            os.waitpid(pid, 0)
        except OSError:
            pass
        except ChildProcessError:
            pass

        with frames_lock:
            lineas = list(frames)
        return self._escribir_cast(lineas, salida, columnas, filas)

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
        cabecera = {
            "version": 2,
            "width": columnas,
            "height": filas,
            "timestamp": int(time.time()),
            "idle_time_limit": 2,
            "env": {
                "SHELL": self.shell,
                "TERM": os.environ.get("TUTORREC_TERM", "xterm-256color"),
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