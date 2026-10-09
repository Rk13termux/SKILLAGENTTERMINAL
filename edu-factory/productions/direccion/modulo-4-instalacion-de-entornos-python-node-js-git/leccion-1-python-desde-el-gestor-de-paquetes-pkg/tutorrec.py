#!/usr/bin/env python3
"""Tutorrec Cinematográfico - Generado por edu-factory.

Plan: Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
Módulo: Instalación de entornos (Python, Node.js, Git) · Lección: Python desde el gestor de paquetes pkg
5 comandos extraídos del plan maestro.
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
        'comando': 'pkg install python',
        'descripcion': 'Paso 1 de 5: Python desde el gestor de paquetes pkg',
    },
    {
        'comando': 'python --version',
        'descripcion': 'Paso 2 de 5: Python desde el gestor de paquetes pkg',
    },
    {
        'comando': 'pip --version',
        'descripcion': 'Paso 3 de 5: Python desde el gestor de paquetes pkg',
    },
    {
        'comando': 'python -m venv mi-proyecto/venv',
        'descripcion': 'Paso 4 de 5: Python desde el gestor de paquetes pkg',
    },
    {
        'comando': 'source mi-proyecto/venv/bin/activate',
        'descripcion': 'Paso 5 de 5: Python desde el gestor de paquetes pkg',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="demo").ejecutar_secuencia(SECUENCIA)
