#!/usr/bin/env python3
"""Tutorrec Cinematográfico (modo real) - Generado por edu-factory.

Plan: Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
Módulo: Control de versiones (Git y GitHub desde el celular) · Lección: El ciclo de trabajo de Git: commit y log
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
        'comando': 'git status',
        'descripcion': 'Paso 1 de 5: El ciclo de trabajo de Git: commit y log',
    },
    {
        'comando': 'git add .',
        'descripcion': 'Paso 2 de 5: El ciclo de trabajo de Git: commit y log',
    },
    {
        'comando': 'git commit -m "Agrega mi primer proyecto"',
        'descripcion': 'Paso 3 de 5: El ciclo de trabajo de Git: commit y log',
    },
    {
        'comando': 'git log --oneline',
        'descripcion': 'Paso 4 de 5: El ciclo de trabajo de Git: commit y log',
    },
    {
        'comando': 'git diff',
        'descripcion': 'Paso 5 de 5: El ciclo de trabajo de Git: commit y log',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="real").ejecutar_secuencia(SECUENCIA)
