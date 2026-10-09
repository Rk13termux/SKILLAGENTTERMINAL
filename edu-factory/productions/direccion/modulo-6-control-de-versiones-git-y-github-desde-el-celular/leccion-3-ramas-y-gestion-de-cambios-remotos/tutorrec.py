#!/usr/bin/env python3
"""Tutorrec Cinematográfico - Generado por edu-factory.

Plan: Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
Módulo: Control de versiones (Git y GitHub desde el celular) · Lección: Ramas y gestión de cambios remotos
6 comandos extraídos del plan maestro.
Modo demo: simula el output realista sin ejecutar los comandos.
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
        'comando': 'git branch readme',
        'descripcion': 'Paso 1 de 6: Ramas y gestión de cambios remotos',
    },
    {
        'comando': 'git checkout readme',
        'descripcion': 'Paso 2 de 6: Ramas y gestión de cambios remotos',
    },
    {
        'comando': 'git add . && git commit -m "Mejora el readme"',
        'descripcion': 'Paso 3 de 6: Ramas y gestión de cambios remotos',
    },
    {
        'comando': 'git checkout main',
        'descripcion': 'Paso 4 de 6: Ramas y gestión de cambios remotos',
    },
    {
        'comando': 'git merge readme',
        'descripcion': 'Paso 5 de 6: Ramas y gestión de cambios remotos',
    },
    {
        'comando': 'git push',
        'descripcion': 'Paso 6 de 6: Ramas y gestión de cambios remotos',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="demo").ejecutar_secuencia(SECUENCIA)
