#!/usr/bin/env python3
"""Tutorrec Cinematográfico (modo real) - Generado por edu-factory.

Plan: Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
Módulo: Instalación de entornos (Python, Node.js, Git) · Lección: Node.js y npm
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
        'comando': 'pkg install nodejs',
        'descripcion': 'Paso 1 de 6: Node.js y npm',
    },
    {
        'comando': 'node --version',
        'descripcion': 'Paso 2 de 6: Node.js y npm',
    },
    {
        'comando': 'npm --version',
        'descripcion': 'Paso 3 de 6: Node.js y npm',
    },
    {
        'comando': 'mkdir app && cd app',
        'descripcion': 'Paso 4 de 6: Node.js y npm',
    },
    {
        'comando': 'npm init -y',
        'descripcion': 'Paso 5 de 6: Node.js y npm',
    },
    {
        'comando': 'npm install lodash',
        'descripcion': 'Paso 6 de 6: Node.js y npm',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="real").ejecutar_secuencia(SECUENCIA)
