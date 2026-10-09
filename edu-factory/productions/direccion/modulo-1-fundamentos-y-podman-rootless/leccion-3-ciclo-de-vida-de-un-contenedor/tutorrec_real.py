#!/usr/bin/env python3
"""Tutorrec Cinematográfico (modo real) - Generado por edu-factory.

Plan: Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
Módulo: Fundamentos y Podman rootless · Lección: Ciclo de vida de un contenedor
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
        'comando': 'podman run -d --name web -p 8080:80 docker.io/library/nginx:alpine',
        'descripcion': 'Paso 1 de 7: Ciclo de vida de un contenedor',
    },
    {
        'comando': 'podman ps',
        'descripcion': 'Paso 2 de 7: Ciclo de vida de un contenedor',
    },
    {
        'comando': 'podman logs web',
        'descripcion': 'Paso 3 de 7: Ciclo de vida de un contenedor',
    },
    {
        'comando': 'podman port web',
        'descripcion': 'Paso 4 de 7: Ciclo de vida de un contenedor',
    },
    {
        'comando': 'podman exec web hostname',
        'descripcion': 'Paso 5 de 7: Ciclo de vida de un contenedor',
    },
    {
        'comando': 'podman stop web',
        'descripcion': 'Paso 6 de 7: Ciclo de vida de un contenedor',
    },
    {
        'comando': 'podman rm web',
        'descripcion': 'Paso 7 de 7: Ciclo de vida de un contenedor',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="real").ejecutar_secuencia(SECUENCIA)
