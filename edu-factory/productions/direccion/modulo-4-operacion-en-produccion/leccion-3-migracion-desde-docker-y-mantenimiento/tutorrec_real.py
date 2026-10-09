#!/usr/bin/env python3
"""Tutorrec Cinematográfico (modo real) - Generado por edu-factory.

Plan: Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
Módulo: Operación en producción · Lección: Migración desde Docker y mantenimiento
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
        'comando': 'podman --version',
        'descripcion': 'Paso 1 de 7: Migración desde Docker y mantenimiento',
    },
    {
        'comando': 'podman system df',
        'descripcion': 'Paso 2 de 7: Migración desde Docker y mantenimiento',
    },
    {
        'comando': 'podman images',
        'descripcion': 'Paso 3 de 7: Migración desde Docker y mantenimiento',
    },
    {
        'comando': 'podman ps -a',
        'descripcion': 'Paso 4 de 7: Migración desde Docker y mantenimiento',
    },
    {
        'comando': "podman info --format '{{.Store.GraphRoot}}'",
        'descripcion': 'Paso 5 de 7: Migración desde Docker y mantenimiento',
    },
    {
        'comando': 'podman events --help | head -n 3',
        'descripcion': 'Paso 6 de 7: Migración desde Docker y mantenimiento',
    },
    {
        'comando': 'podman system connection ls',
        'descripcion': 'Paso 7 de 7: Migración desde Docker y mantenimiento',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="real").ejecutar_secuencia(SECUENCIA)
