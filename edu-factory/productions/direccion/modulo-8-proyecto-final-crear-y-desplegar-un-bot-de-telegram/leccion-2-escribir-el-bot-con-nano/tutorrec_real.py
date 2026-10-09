#!/usr/bin/env python3
"""Tutorrec Cinematográfico (modo real) - Generado por edu-factory.

Plan: Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
Módulo: Proyecto final (crear y desplegar un Bot de Telegram) · Lección: Escribir el bot con nano
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
        'comando': 'export TELEGRAM_TOKEN="1200000000:AA-tu-token-real"',
        'descripcion': 'Paso 1 de 5: Escribir el bot con nano',
    },
    {
        'comando': 'echo $TELEGRAM_TOKEN',
        'descripcion': 'Paso 2 de 5: Escribir el bot con nano',
    },
    {
        'comando': 'nano bot.py',
        'descripcion': 'Paso 3 de 5: Escribir el bot con nano',
    },
    {
        'comando': 'python bot.py',
        'descripcion': 'Paso 4 de 5: Escribir el bot con nano',
    },
    {
        'comando': 'python -m py_compile bot.py',
        'descripcion': 'Paso 5 de 5: Escribir el bot con nano',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="real").ejecutar_secuencia(SECUENCIA)
