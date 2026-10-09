#!/usr/bin/env python3
"""Tutorrec Cinematográfico (modo real) - Generado por edu-factory.

Plan: Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
Módulo: Instalación de entornos (Python, Node.js, Git) · Lección: Git y configuración de identidad
6 comandos extraídos del plan maestro.
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
        'comando': 'pkg install git',
        'descripcion': 'Paso 1 de 6: Git y configuración de identidad',
    },
    {
        'comando': 'git --version',
        'descripcion': 'Paso 2 de 6: Git y configuración de identidad',
    },
    {
        'comando': 'git config --global user.name "Tu Nombre"',
        'descripcion': 'Paso 3 de 6: Git y configuración de identidad',
    },
    {
        'comando': 'git config --global user.email "tu@correo.com"',
        'descripcion': 'Paso 4 de 6: Git y configuración de identidad',
    },
    {
        'comando': 'git init',
        'descripcion': 'Paso 5 de 6: Git y configuración de identidad',
    },
    {
        'comando': 'git status',
        'descripcion': 'Paso 6 de 6: Git y configuración de identidad',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="real").ejecutar_secuencia(SECUENCIA)
