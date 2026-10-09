#!/usr/bin/env python3
"""Tutorrec Cinematográfico - Generado por edu-factory.

Plan: Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
Módulo: Imágenes y construcción · Lección: Registros, etiquetas y distribución
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
        'comando': 'podman tag hola-podman localhost:5000/hola-podman:1.0',
        'descripcion': 'Paso 1 de 5: Registros, etiquetas y distribución',
    },
    {
        'comando': "podman images 'localhost:5000/*'",
        'descripcion': 'Paso 2 de 5: Registros, etiquetas y distribución',
    },
    {
        'comando': "skopeo inspect --format '{{.Digest}}' docker://docker.io/library/alpine:latest",
        'descripcion': 'Paso 3 de 5: Registros, etiquetas y distribución',
    },
    {
        'comando': 'podman login --help | head -n 3',
        'descripcion': 'Paso 4 de 5: Registros, etiquetas y distribución',
    },
    {
        'comando': 'podman push --help | head -n 3',
        'descripcion': 'Paso 5 de 5: Registros, etiquetas y distribución',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="demo").ejecutar_secuencia(SECUENCIA)
