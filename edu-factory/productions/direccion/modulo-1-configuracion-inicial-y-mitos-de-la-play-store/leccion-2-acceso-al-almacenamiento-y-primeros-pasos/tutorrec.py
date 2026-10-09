#!/usr/bin/env python3
"""Tutorrec Cinematográfico - Generado por edu-factory.

Plan: Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
Módulo: Configuración inicial y mitos de la Play Store · Lección: Acceso al almacenamiento y primeros pasos
4 comandos extraídos del plan maestro.
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
        'comando': 'termux-setup-storage',
        'descripcion': 'Paso 1 de 4: Acceso al almacenamiento y primeros pasos',
    },
    {
        'comando': 'ls ~/storage/shared',
        'descripcion': 'Paso 2 de 4: Acceso al almacenamiento y primeros pasos',
    },
    {
        'comando': 'termux-change-repo',
        'descripcion': 'Paso 3 de 4: Acceso al almacenamiento y primeros pasos',
    },
    {
        'comando': 'pwd',
        'descripcion': 'Paso 4 de 4: Acceso al almacenamiento y primeros pasos',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="demo").ejecutar_secuencia(SECUENCIA)
