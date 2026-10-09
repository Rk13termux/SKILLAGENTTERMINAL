#!/usr/bin/env python3
"""Tutorrec Cinematográfico - Generado por edu-factory.

Plan: Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
Módulo: Configuración inicial y mitos de la Play Store · Lección: Qué es Termux y por qué evitar la Play Store
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
        'comando': 'pkg update',
        'descripcion': 'Paso 1 de 4: Qué es Termux y por qué evitar la Play Store',
    },
    {
        'comando': 'pkg upgrade',
        'descripcion': 'Paso 2 de 4: Qué es Termux y por qué evitar la Play Store',
    },
    {
        'comando': 'pkg list-installed',
        'descripcion': 'Paso 3 de 4: Qué es Termux y por qué evitar la Play Store',
    },
    {
        'comando': 'termux-info',
        'descripcion': 'Paso 4 de 4: Qué es Termux y por qué evitar la Play Store',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="demo").ejecutar_secuencia(SECUENCIA)
