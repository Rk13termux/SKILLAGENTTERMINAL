#!/usr/bin/env python3
"""Tutorrec Cinematográfico - Generado por edu-factory.

Plan: Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
Módulo: Gestión de archivos y permisos (chmod, chown, nano) · Lección: Propietario y edición de texto con nano
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
        'comando': 'pkg install nano',
        'descripcion': 'Paso 1 de 5: Propietario y edición de texto con nano',
    },
    {
        'comando': 'nano notas.txt',
        'descripcion': 'Paso 2 de 5: Propietario y edición de texto con nano',
    },
    {
        'comando': 'chown $(id -u):$(id -g) notas.txt',
        'descripcion': 'Paso 3 de 5: Propietario y edición de texto con nano',
    },
    {
        'comando': 'ls -l ~/storage/shared',
        'descripcion': 'Paso 4 de 5: Propietario y edición de texto con nano',
    },
    {
        'comando': 'file notas.txt',
        'descripcion': 'Paso 5 de 5: Propietario y edición de texto con nano',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="demo").ejecutar_secuencia(SECUENCIA)
