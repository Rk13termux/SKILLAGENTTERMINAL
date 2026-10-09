#!/usr/bin/env python3
"""Tutorrec Cinematográfico (modo real) - Generado por edu-factory.

Plan: Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
Módulo: Proyecto final (crear y desplegar un Bot de Telegram) · Lección: Obtener el token y preparar el entorno
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
        'comando': 'pkg install python',
        'descripcion': 'Paso 1 de 6: Obtener el token y preparar el entorno',
    },
    {
        'comando': 'mkdir -p ~/telebot',
        'descripcion': 'Paso 2 de 6: Obtener el token y preparar el entorno',
    },
    {
        'comando': 'cd ~/telebot',
        'descripcion': 'Paso 3 de 6: Obtener el token y preparar el entorno',
    },
    {
        'comando': 'python -m venv venv',
        'descripcion': 'Paso 4 de 6: Obtener el token y preparar el entorno',
    },
    {
        'comando': 'source venv/bin/activate',
        'descripcion': 'Paso 5 de 6: Obtener el token y preparar el entorno',
    },
    {
        'comando': 'pip install python-telegram-bot',
        'descripcion': 'Paso 6 de 6: Obtener el token y preparar el entorno',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="real").ejecutar_secuencia(SECUENCIA)
