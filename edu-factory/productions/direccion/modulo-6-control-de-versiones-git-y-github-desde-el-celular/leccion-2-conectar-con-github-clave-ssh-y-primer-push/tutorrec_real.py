#!/usr/bin/env python3
"""Tutorrec Cinematográfico (modo real) - Generado por edu-factory.

Plan: Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
Módulo: Control de versiones (Git y GitHub desde el celular) · Lección: Conectar con GitHub: clave SSH y primer push
7 comandos extraídos del plan maestro.
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
        'descripcion': 'Paso 1 de 7: Conectar con GitHub: clave SSH y primer push',
    },
    {
        'comando': 'ssh-keygen -t ed25519 -C "tu@correo.com"',
        'descripcion': 'Paso 2 de 7: Conectar con GitHub: clave SSH y primer push',
    },
    {
        'comando': 'cat ~/.ssh/id_ed25519.pub',
        'descripcion': 'Paso 3 de 7: Conectar con GitHub: clave SSH y primer push',
    },
    {
        'comando': 'git remote add origin git@github.com:usuario/repositorio.git',
        'descripcion': 'Paso 4 de 7: Conectar con GitHub: clave SSH y primer push',
    },
    {
        'comando': 'git branch -M main',
        'descripcion': 'Paso 5 de 7: Conectar con GitHub: clave SSH y primer push',
    },
    {
        'comando': 'git push -u origin main',
        'descripcion': 'Paso 6 de 7: Conectar con GitHub: clave SSH y primer push',
    },
    {
        'comando': 'git clone git@github.com:usuario/repositorio.git',
        'descripcion': 'Paso 7 de 7: Conectar con GitHub: clave SSH y primer push',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="real").ejecutar_secuencia(SECUENCIA)
