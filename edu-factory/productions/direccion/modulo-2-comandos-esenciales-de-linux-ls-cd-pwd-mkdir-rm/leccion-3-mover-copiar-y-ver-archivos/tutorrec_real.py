#!/usr/bin/env python3
"""Tutorrec Cinematográfico (modo real) - Generado por edu-factory.

Plan: Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
Módulo: Comandos esenciales de Linux (ls, cd, pwd, mkdir, rm) · Lección: mover, copiar y ver archivos
5 comandos extraídos del plan maestro.
Modo real: escribe los comandos y los ejecuta de verdad en el sistema.
"""

import sys
from pathlib import Path

for _padre in Path(__file__).resolve().parents:
    if (_padre / "tutorrec").is_dir():
        sys.path.insert(0, str(_padre))
        break

from tutorrec.cinematic import CinematicTerminal  # noqa: E402

SECUENCIA = [
    {
        'comando': 'cp notas.txt notas-copia.txt',
        'descripcion': 'Paso 1 de 5: mover, copiar y ver archivos',
    },
    {
        'comando': 'mv notas-copia.txt apuntes.txt',
        'descripcion': 'Paso 2 de 5: mover, copiar y ver archivos',
    },
    {
        'comando': 'cat apuntes.txt',
        'descripcion': 'Paso 3 de 5: mover, copiar y ver archivos',
    },
    {
        'comando': 'mkdir -p ~/backup && mv apuntes.txt ~/backup',
        'descripcion': 'Paso 4 de 5: mover, copiar y ver archivos',
    },
    {
        'comando': 'less apuntes.txt',
        'descripcion': 'Paso 5 de 5: mover, copiar y ver archivos',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="real").ejecutar_secuencia(SECUENCIA)
