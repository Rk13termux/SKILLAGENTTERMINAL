#!/usr/bin/env python3
"""Tutorrec Cinematográfico - CLI independiente para pruebas."""

from __future__ import annotations

import argparse
import sys

from tutorrec import CinematicTerminal  # noqa: F401
from tutorrec.cinematic import CinematicTerminal
from tutorrec.sequences import git_workflow, python_script, termux_basic


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="tutorrec.cli", description="Tutorrec Cinematográfico")
    parser.add_argument(
        "--secuencia",
        choices=["termux", "git", "python"],
        default="termux",
        help="secuencia predefinida a ejecutar",
    )
    parser.add_argument(
        "--modo",
        choices=["demo", "real"],
        default="demo",
        help="demo simula el output; real ejecuta los comandos de verdad",
    )
    parser.add_argument(
        "--velocidad",
        type=float,
        default=None,
        help="velocidad base en segundos por carácter (defecto: 0.12, ~8 letras/s)",
    )
    parser.add_argument(
        "--sin-pausas",
        action="store_true",
        help="desactivar pausas naturales (pensando/post-enter)",
    )
    parser.add_argument(
        "--no-limpiar",
        action="store_true",
        help="no limpiar la pantalla entre comandos",
    )
    parser.add_argument(
        "--mostrar-descripcion",
        action="store_true",
        help="mostrar la línea «▶ descripción» antes de cada comando",
    )
    parser.add_argument(
        "--prompt",
        default=None,
        help="prompt de la terminal (defecto: usuario@hostname:carpeta$)",
    )
    parser.add_argument(
        "--banner",
        action="store_true",
        help="mostrar la pantalla de bienvenida de Termux al inicio (demo)",
    )
    parser.add_argument(
        "--backend",
        choices=["ansi", "asciinema"],
        default="ansi",
        help="ansi simula el output en colores; asciinema graba la terminal real a .cast",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="archivo .cast de salida (solo backend asciinema)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = construir_parser().parse_args(argv)
    secuencias = {
        "termux": termux_basic.SECUENCIA,
        "git": git_workflow.SECUENCIA,
        "python": python_script.SECUENCIA,
    }
    terminal = CinematicTerminal(
        mode=args.modo,
        backend=args.backend,
        velocidad_base=args.velocidad,
        pausas_naturales=not args.sin_pausas,
        limpiar_entre_comandos=not args.no_limpiar,
        mostrar_descripcion=args.mostrar_descripcion,
        prompt=args.prompt,
        banner=args.banner,
        output_file=args.output,
    )
    terminal.ejecutar_secuencia(secuencias[args.secuencia])
    return 0


if __name__ == "__main__":
    sys.exit(main())