#!/usr/bin/env python3
"""Tutorrec Cinematográfico - Generado por edu-factory.

Plan: Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
Módulo: Conexiones y redes (SSH, ping, curl) · Lección: SSH cliente: conectarte a otro equipo
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
        'comando': 'pkg install openssh',
        'descripcion': 'Paso 1 de 5: SSH cliente: conectarte a otro equipo',
    },
    {
        'comando': 'ssh usuario@192.168.1.10',
        'descripcion': 'Paso 2 de 5: SSH cliente: conectarte a otro equipo',
    },
    {
        'comando': 'ssh-copy-id usuario@192.168.1.10',
        'descripcion': 'Paso 3 de 5: SSH cliente: conectarte a otro equipo',
    },
    {
        'comando': 'ssh -p 8022 usuario@servidor.com',
        'descripcion': 'Paso 4 de 5: SSH cliente: conectarte a otro equipo',
    },
    {
        'comando': 'exit',
        'descripcion': 'Paso 5 de 5: SSH cliente: conectarte a otro equipo',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="demo").ejecutar_secuencia(SECUENCIA)
