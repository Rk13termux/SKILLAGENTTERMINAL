#!/usr/bin/env python3
"""Tutorrec Cinematográfico (modo real) - Generado por edu-factory.

Plan: Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
Módulo: Gestión de archivos y permisos (chmod, chown, nano) · Lección: Permisos de Linux y chmod
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
        'comando': 'ls -l',
        'descripcion': 'Paso 1 de 5: Permisos de Linux y chmod',
    },
    {
        'comando': 'chmod 644 notas.txt',
        'descripcion': 'Paso 2 de 5: Permisos de Linux y chmod',
    },
    {
        'comando': 'chmod 755 script.sh',
        'descripcion': 'Paso 3 de 5: Permisos de Linux y chmod',
    },
    {
        'comando': 'chmod +x script.sh',
        'descripcion': 'Paso 4 de 5: Permisos de Linux y chmod',
    },
    {
        'comando': 'stat notas.txt',
        'descripcion': 'Paso 5 de 5: Permisos de Linux y chmod',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="real").ejecutar_secuencia(SECUENCIA)
