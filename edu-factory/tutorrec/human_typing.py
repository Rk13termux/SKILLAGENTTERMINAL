"""Algoritmo de escritura humana variable para tutorrec cinematográfico."""

from __future__ import annotations

import random
import sys
import time


def pausa_pensando(pausas_naturales: bool = True) -> None:
    if pausas_naturales:
        time.sleep(random.uniform(0.3, 0.8))


def pausa_post_enter(pausas_naturales: bool = True) -> None:
    if pausas_naturales:
        time.sleep(random.uniform(1.0, 2.0))


def delay_caracter(caracter: str, velocidad_base: float, pausas_naturales: bool) -> float:
    if not pausas_naturales:
        return velocidad_base
    delay = random.uniform(velocidad_base * 0.5, velocidad_base * 1.5)
    if caracter == " ":
        delay *= 1.5
    elif caracter in ".,;:":
        delay *= 2.0
    elif caracter == "\n":
        delay *= 0.5
    return delay


def typewriter_humano(texto: str, velocidad_base: float = 0.04, pausas_naturales: bool = True) -> None:
    for caracter in texto:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(delay_caracter(caracter, velocidad_base, pausas_naturales))
    if pausas_naturales and len(texto) > 30:
        time.sleep(0.3)


def typewriter_a_destino(
    destino,
    texto: str,
    velocidad_base: float = 0.04,
    pausas_naturales: bool = True,
) -> None:
    """Escribe texto carácter a carácter en un file-like (p. ej. un PTY)."""
    for caracter in texto:
        destino.write(caracter)
        destino.flush()
        time.sleep(delay_caracter(caracter, velocidad_base, pausas_naturales))
    if pausas_naturales and len(texto) > 30:
        time.sleep(0.3)


__all__ = [
    "pausa_pensando",
    "pausa_post_enter",
    "delay_caracter",
    "typewriter_humano",
    "typewriter_a_destino",
]