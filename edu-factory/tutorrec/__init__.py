"""Tutorrec cinematográfico: simulador de sesión de terminal humana.

Expone la clase CinematicTerminal, la paleta ANSI y utilidades de color.
Solo usa la biblioteca estándar de Python.
"""

from __future__ import annotations

import os
import sys

VERDE = "\033[92m"
CIAN = "\033[96m"
AMARILLO = "\033[93m"
ROJO = "\033[91m"
BLANCO = "\033[97m"
DIM = "\033[2m"
RESET = "\033[0m"
NEGRITA = "\033[1m"


def soporta_color() -> bool:
    if os.environ.get("NO_COLOR"):
        return False
    if os.environ.get("TUTORREC_NO_COLOR"):
        return False
    return sys.stdout.isatty()


def limpiar_permite() -> bool:
    if os.environ.get("TUTORREC_NO_LIMPIAR"):
        return False
    return sys.stdout.isatty()


from tutorrec.cinematic import CinematicTerminal  # noqa: E402

__all__ = [
    "CinematicTerminal",
    "VERDE",
    "CIAN",
    "AMARILLO",
    "ROJO",
    "BLANCO",
    "DIM",
    "RESET",
    "NEGRITA",
    "soporta_color",
    "limpiar_permite",
]