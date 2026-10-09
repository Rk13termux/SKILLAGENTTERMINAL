"""Motor de simulación cinematográfica de terminal.

CinematicTerminal actúa una secuencia de comandos como si la tecleara y
ejecutara un programador real: escritura variable, pausas naturales y
limpieza de pantalla entre comandos.
"""

from __future__ import annotations

import os
import random
import socket
import sys
import time
from typing import Any

from tutorrec import CIAN, AMARILLO, DIM, RESET, ROJO, VERDE, limpiar_permite, soporta_color
from tutorrec.human_typing import pausa_pensando, pausa_post_enter, typewriter_humano
from tutorrec.output_simulator import generar_output_realista

BANNER_TERMUX = """\
Welcome to Termux!

Docs:       https://termux.dev/docs
Donate:     https://termux.dev/donate
Community:  https://termux.dev/community

Working with packages:
 - Search:  pkg search <query>
 - Install: pkg install <package>
 - Upgrade: pkg upgrade

Report issues at https://termux.dev/issues"""


class CinematicTerminal:
    def __init__(
        self,
        mode: str = "demo",
        backend: str | None = None,
        velocidad_base: float | None = None,
        pausas_naturales: bool | None = None,
        limpiar_entre_comandos: bool = True,
        mostrar_descripcion: bool = False,
        prompt: str | None = None,
        banner: bool | None = None,
        output_file: str | None = None,
    ) -> None:
        if pausas_naturales is None:
            pausas_naturales = os.environ.get("TUTORREC_PAUSAS", "1") == "1"
        if prompt is None:
            prompt = os.environ.get("TUTORREC_PROMPT")
        if banner is None:
            banner = os.environ.get("TUTORREC_BANNER", "0") == "1"
        if not mostrar_descripcion and os.environ.get("TUTORREC_DESCRIPCION") == "1":
            mostrar_descripcion = True
        if velocidad_base is None:
            velocidad_base = float(os.environ.get("TUTORREC_VELOCIDAD", "0.12"))
        self.mode = mode
        self.backend = backend or os.environ.get("TUTORREC_BACKEND", "ansi")
        self.velocidad_base = velocidad_base
        self.pausas_naturales = pausas_naturales
        self.limpiar_entre_comandos = limpiar_entre_comandos
        self.mostrar_descripcion = mostrar_descripcion
        self.prompt = prompt
        self.banner = banner
        self.output_file = output_file or os.environ.get("TUTORREC_OUTPUT", "recording.cast")
        self._color = soporta_color()
        self.usuario = self._usuario_real()
        self.hostname = socket.gethostname() or "localhost"
        self.home = os.path.expanduser("~")
        self._cwd = os.path.expanduser("~")

    def _usuario_real(self) -> str:
        for var in ("LOGNAME", "USER", "USERNAME"):
            valor = os.environ.get(var)
            if valor:
                return valor
        try:
            import pwd as _pwd

            return _pwd.getpwuid(os.getuid()).pw_name
        except Exception:
            return "usuario"

    def _directorio_visible(self) -> str:
        try:
            rel = os.path.relpath(self._cwd, self.home)
        except Exception:
            return self._cwd
        if rel == ".":
            return "~"
        if not rel.startswith(".."):
            return f"~/{rel}"
        return self._cwd

    def _texto_prompt(self) -> str:
        if self.prompt:
            return self.prompt
        return f"{self.usuario}@{self.hostname}:{self._directorio_visible()}$ "

    def tipo(self, texto: str) -> None:
        self.escribir_prompt(self._texto_prompt())
        typewriter_humano(texto, self.velocidad_base, self.pausas_naturales)
        sys.stdout.write("\n")
        sys.stdout.flush()

    def escribir_prompt(self, texto: str) -> None:
        if self._color and texto.endswith("$"):
            base, simbolo = texto[:-1], texto[-1]
            sys.stdout.write(VERDE + base + RESET + VERDE + simbolo + RESET)
        else:
            sys.stdout.write(texto)
        sys.stdout.flush()

    def escribir_color(self, texto: str, color: str = RESET, extra: str = "") -> None:
        if self._color and color:
            sys.stdout.write(extra + color + texto + RESET)
        else:
            sys.stdout.write(texto)
        sys.stdout.flush()

    def limpiar_pantalla(self) -> None:
        if not self.limpiar_entre_comandos or not limpiar_permite():
            return
        if os.name == "nt":
            os.system("cls")
        else:
            sys.stdout.write("\033[2J\033[H")
            sys.stdout.flush()

    def simular_output(self, lineas: list[str]) -> None:
        for linea in lineas:
            self.escribir_color(linea, CIAN)
            sys.stdout.write("\n")
            sys.stdout.flush()
            if self.pausas_naturales:
                time.sleep(random.uniform(0.02, 0.07))

    def ejecutar_secuencia(self, comandos: list[dict[str, Any]]) -> None:
        if self.backend == "asciinema":
            self._ejecutar_con_asciinema(comandos)
            return
        self.limpiar_pantalla()
        if self.banner and self.mode == "demo":
            self._bienvenida()
        total = len(comandos)
        for indice, paso in enumerate(comandos, start=1):
            self._ejecutar_paso(paso, indice, total)
            if indice < total:
                self.limpiar_pantalla()
        self.limpiar_pantalla()

    def _ejecutar_con_asciinema(self, comandos: list[dict[str, Any]]) -> None:
        from tutorrec.pty_recorder import PtyAsciinemaRecorder

        grabador = PtyAsciinemaRecorder(
            shell=os.environ.get("TUTORREC_SHELL"),
            velocidad_base=self.velocidad_base,
            pausas_naturales=self.pausas_naturales,
            limpiar_entre_comandos=self.limpiar_entre_comandos,
            mostrar_descripcion=self.mostrar_descripcion,
        )
        ruta = self.output_file
        if not ruta.endswith(".cast"):
            ruta += ".cast"
        grabador.grabar(comandos, ruta)
        self._color = self._color
        print("\nGrabado en: " + ruta, file=sys.stderr)
        print("Reproduce con: asciinema play " + ruta, file=sys.stderr)
        print("Convierte con: agg " + ruta + " video.gif", file=sys.stderr)

    def _bienvenida(self) -> None:
        for linea in BANNER_TERMUX.splitlines():
            self.escribir_color(linea, RESET)
            sys.stdout.write("\n")
            sys.stdout.flush()
            if self.pausas_naturales:
                time.sleep(random.uniform(0.02, 0.06))
        sys.stdout.write("\n")
        sys.stdout.flush()
        if self.pausas_naturales:
            time.sleep(1.0)

    def _ejecutar_paso(self, paso: dict[str, Any], indice: int, total: int) -> None:
        comando = str(paso.get("comando", "")).strip()
        descripcion = paso.get("descripcion", "")
        pausa_post = float(paso.get("pausa_post", 1.6))
        output = paso.get("output")

        if comando.startswith("cd "):
            self._aplicar_cd(comando[3:].strip().lstrip(";").lstrip())
        elif comando == "cd":
            self._cwd = self.home

        if descripcion:
            if self.mostrar_descripcion:
                self.escribir_color(f"▶ {descripcion}", AMARILLO, "")
                sys.stdout.write("\n")
                sys.stdout.flush()
                time.sleep(0.4)
            elif self.pausas_naturales:
                time.sleep(random.uniform(0.4, 0.9))

        pausa_pensando(self.pausas_naturales)
        self.tipo(comando)
        pausa_post_enter(self.pausas_naturales)

        if self.mode == "real":
            retorno = os.system(comando)
            if retorno != 0:
                self.escribir_color(f"[Aviso: el comando devolvió {retorno}]", ROJO)
                sys.stdout.write("\n")
                sys.stdout.flush()
        else:
            if output is None:
                output = generar_output_realista(comando)
            self.simular_output(list(output))

        if self.pausas_naturales:
            time.sleep(pausa_post)

    def _aplicar_cd(self, destino: str) -> None:
        if not destino:
            self._cwd = self.home
            return
        destino = destino.strip("\"'").strip()
        if destino.startswith("~"):
            destino = self.home + destino[1:]
        elif not destino.startswith("/"):
            destino = os.path.join(self._cwd, destino)
        self._cwd = os.path.abspath(destino)


__all__ = ["CinematicTerminal"]