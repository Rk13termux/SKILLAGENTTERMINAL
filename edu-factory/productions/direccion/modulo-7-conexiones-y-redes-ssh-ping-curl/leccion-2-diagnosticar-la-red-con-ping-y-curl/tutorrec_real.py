#!/usr/bin/env python3
"""Tutorrec Cinematográfico (modo real) - Generado por edu-factory.

Plan: Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
Módulo: Conexiones y redes (SSH, ping, curl) · Lección: Diagnosticar la red con ping y curl
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
        'comando': 'ping -c 4 1.1.1.1',
        'descripcion': 'Paso 1 de 5: Diagnosticar la red con ping y curl',
    },
    {
        'comando': 'pkg install curl',
        'descripcion': 'Paso 2 de 5: Diagnosticar la red con ping y curl',
    },
    {
        'comando': 'curl -I https://example.com',
        'descripcion': 'Paso 3 de 5: Diagnosticar la red con ping y curl',
    },
    {
        'comando': 'curl -v --max-time 10 https://api.telegram.org',
        'descripcion': 'Paso 4 de 5: Diagnosticar la red con ping y curl',
    },
    {
        'comando': 'curl -s https://api.github.com/repos/termux/termux-packages',
        'descripcion': 'Paso 5 de 5: Diagnosticar la red con ping y curl',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="real").ejecutar_secuencia(SECUENCIA)
