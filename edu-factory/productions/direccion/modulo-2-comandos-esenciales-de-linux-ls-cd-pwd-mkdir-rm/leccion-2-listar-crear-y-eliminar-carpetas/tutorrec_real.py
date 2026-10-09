#!/usr/bin/env python3
"""Tutorrec Cinematográfico (modo real) - Generado por edu-factory.

Plan: Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
Módulo: Comandos esenciales de Linux (ls, cd, pwd, mkdir, rm) · Lección: listar, crear y eliminar carpetas
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
        'comando': 'mkdir -p proyectos/cursos',
        'descripcion': 'Paso 1 de 5: listar, crear y eliminar carpetas',
    },
    {
        'comando': 'ls -la proyectos',
        'descripcion': 'Paso 2 de 5: listar, crear y eliminar carpetas',
    },
    {
        'comando': 'touch proyectos/notas.txt',
        'descripcion': 'Paso 3 de 5: listar, crear y eliminar carpetas',
    },
    {
        'comando': 'rm proyectos/notas.txt',
        'descripcion': 'Paso 4 de 5: listar, crear y eliminar carpetas',
    },
    {
        'comando': 'rm -rf proyectos',
        'descripcion': 'Paso 5 de 5: listar, crear y eliminar carpetas',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="real").ejecutar_secuencia(SECUENCIA)
