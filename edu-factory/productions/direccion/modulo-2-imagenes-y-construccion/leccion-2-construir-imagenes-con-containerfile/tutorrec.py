#!/usr/bin/env python3
"""Tutorrec Cinematográfico - Generado por edu-factory.

Plan: Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
Módulo: Imágenes y construcción · Lección: Construir imágenes con Containerfile
6 comandos extraídos del plan maestro.
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
        'comando': 'mkdir -p /tmp/podman-curso && cd /tmp/podman-curso',
        'descripcion': 'Paso 1 de 6: Construir imágenes con Containerfile',
    },
    {
        'comando': 'printf \'FROM docker.io/library/alpine:latest\\nRUN echo "construido en Fedora" > /mensaje.txt\\nCMD ["cat","/mensaje.txt"]\\n\' > Containerfile',
        'descripcion': 'Paso 2 de 6: Construir imágenes con Containerfile',
    },
    {
        'comando': 'cat Containerfile',
        'descripcion': 'Paso 3 de 6: Construir imágenes con Containerfile',
    },
    {
        'comando': 'podman build -t hola-podman .',
        'descripcion': 'Paso 4 de 6: Construir imágenes con Containerfile',
    },
    {
        'comando': 'podman run --rm hola-podman',
        'descripcion': 'Paso 5 de 6: Construir imágenes con Containerfile',
    },
    {
        'comando': "podman images 'localhost/*'",
        'descripcion': 'Paso 6 de 6: Construir imágenes con Containerfile',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="demo").ejecutar_secuencia(SECUENCIA)
