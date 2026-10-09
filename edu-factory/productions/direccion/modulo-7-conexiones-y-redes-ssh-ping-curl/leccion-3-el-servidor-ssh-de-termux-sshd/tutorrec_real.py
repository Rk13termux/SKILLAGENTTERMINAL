#!/usr/bin/env python3
"""Tutorrec Cinematográfico (modo real) - Generado por edu-factory.

Plan: Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
Módulo: Conexiones y redes (SSH, ping, curl) · Lección: El servidor SSH de Termux (sshd)
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
        'comando': 'pkg install openssh',
        'descripcion': 'Paso 1 de 5: El servidor SSH de Termux (sshd)',
    },
    {
        'comando': 'sshd',
        'descripcion': 'Paso 2 de 5: El servidor SSH de Termux (sshd)',
    },
    {
        'comando': 'ip addr',
        'descripcion': 'Paso 3 de 5: El servidor SSH de Termux (sshd)',
    },
    {
        'comando': 'whoami',
        'descripcion': 'Paso 4 de 5: El servidor SSH de Termux (sshd)',
    },
    {
        'comando': 'pkill sshd',
        'descripcion': 'Paso 5 de 5: El servidor SSH de Termux (sshd)',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="real").ejecutar_secuencia(SECUENCIA)
