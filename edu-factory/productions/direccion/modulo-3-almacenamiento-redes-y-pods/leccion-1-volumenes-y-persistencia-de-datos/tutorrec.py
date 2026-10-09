#!/usr/bin/env python3
"""Tutorrec Cinematográfico - Generado por edu-factory.

Plan: Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
Módulo: Almacenamiento, redes y pods · Lección: Volúmenes y persistencia de datos
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
        'comando': 'podman volume create datos-web',
        'descripcion': 'Paso 1 de 6: Volúmenes y persistencia de datos',
    },
    {
        'comando': 'podman volume ls',
        'descripcion': 'Paso 2 de 6: Volúmenes y persistencia de datos',
    },
    {
        'comando': "podman volume inspect datos-web --format '{{.Mountpoint}}'",
        'descripcion': 'Paso 3 de 6: Volúmenes y persistencia de datos',
    },
    {
        'comando': "podman run --rm -v datos-web:/data docker.io/library/alpine:latest sh -c 'echo hola > /data/saludo.txt'",
        'descripcion': 'Paso 4 de 6: Volúmenes y persistencia de datos',
    },
    {
        'comando': 'podman run --rm -v datos-web:/data docker.io/library/alpine:latest cat /data/saludo.txt',
        'descripcion': 'Paso 5 de 6: Volúmenes y persistencia de datos',
    },
    {
        'comando': 'podman volume rm datos-web',
        'descripcion': 'Paso 6 de 6: Volúmenes y persistencia de datos',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="demo").ejecutar_secuencia(SECUENCIA)
