#!/usr/bin/env python3
"""Tutorrec Cinematográfico - Generado por edu-factory.

Plan: Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
Módulo: Almacenamiento, redes y pods · Lección: Pods: varios contenedores como uno solo
7 comandos extraídos del plan maestro.
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
        'comando': 'podman pod create --name pod-web -p 8081:80',
        'descripcion': 'Paso 1 de 7: Pods: varios contenedores como uno solo',
    },
    {
        'comando': 'podman pod ls',
        'descripcion': 'Paso 2 de 7: Pods: varios contenedores como uno solo',
    },
    {
        'comando': 'podman run -d --pod pod-web --name pod-nginx docker.io/library/nginx:alpine',
        'descripcion': 'Paso 3 de 7: Pods: varios contenedores como uno solo',
    },
    {
        'comando': 'podman ps --pod',
        'descripcion': 'Paso 4 de 7: Pods: varios contenedores como uno solo',
    },
    {
        'comando': "podman pod inspect pod-web --format '{{.Name}} {{.NumContainers}}'",
        'descripcion': 'Paso 5 de 7: Pods: varios contenedores como uno solo',
    },
    {
        'comando': 'podman pod stop pod-web',
        'descripcion': 'Paso 6 de 7: Pods: varios contenedores como uno solo',
    },
    {
        'comando': 'podman pod rm -f pod-web',
        'descripcion': 'Paso 7 de 7: Pods: varios contenedores como uno solo',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="demo").ejecutar_secuencia(SECUENCIA)
