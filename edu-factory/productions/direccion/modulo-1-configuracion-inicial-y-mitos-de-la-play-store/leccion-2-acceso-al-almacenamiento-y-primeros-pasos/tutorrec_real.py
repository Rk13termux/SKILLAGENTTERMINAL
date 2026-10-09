#!/usr/bin/env python3
"""Tutorrec Cinematográfico (modo real) - Generado por edu-factory.

Plan: Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
Módulo: Configuración inicial y mitos de la Play Store · Lección: Acceso al almacenamiento y primeros pasos
4 comandos extraídos del plan maestro.
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
    CinematicTerminal(mode="real").ejecutar_secuencia(SECUENCIA)
