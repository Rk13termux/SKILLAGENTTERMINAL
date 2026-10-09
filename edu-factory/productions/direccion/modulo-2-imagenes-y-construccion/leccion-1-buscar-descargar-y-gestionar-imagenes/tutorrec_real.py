#!/usr/bin/env python3
"""Tutorrec Cinematográfico (modo real) - Generado por edu-factory.

Plan: Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
Módulo: Imágenes y construcción · Lección: Buscar, descargar y gestionar imágenes
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
        'comando': 'podman search docker.io/library/alpine --limit 3',
        'descripcion': 'Paso 1 de 5: Buscar, descargar y gestionar imágenes',
    },
    {
        'comando': 'podman pull docker.io/library/alpine:latest',
        'descripcion': 'Paso 2 de 5: Buscar, descargar y gestionar imágenes',
    },
    {
        'comando': 'podman images',
        'descripcion': 'Paso 3 de 5: Buscar, descargar y gestionar imágenes',
    },
    {
        'comando': 'podman history docker.io/library/alpine:latest',
        'descripcion': 'Paso 4 de 5: Buscar, descargar y gestionar imágenes',
    },
    {
        'comando': 'podman image tree docker.io/library/alpine:latest',
        'descripcion': 'Paso 5 de 5: Buscar, descargar y gestionar imágenes',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="real").ejecutar_secuencia(SECUENCIA)
