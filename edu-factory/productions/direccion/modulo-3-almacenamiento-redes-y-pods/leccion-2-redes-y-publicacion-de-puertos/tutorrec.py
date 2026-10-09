#!/usr/bin/env python3
"""Tutorrec Cinematográfico - Generado por edu-factory.

Plan: Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
Módulo: Almacenamiento, redes y pods · Lección: Redes y publicación de puertos
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
        'comando': 'podman network ls',
        'descripcion': 'Paso 1 de 7: Redes y publicación de puertos',
    },
    {
        'comando': 'podman network create red-curso',
        'descripcion': 'Paso 2 de 7: Redes y publicación de puertos',
    },
    {
        'comando': "podman network inspect red-curso --format '{{range .Subnets}}{{.Subnet}}{{end}}'",
        'descripcion': 'Paso 3 de 7: Redes y publicación de puertos',
    },
    {
        'comando': 'podman run -d --name api --network red-curso docker.io/library/alpine:latest sleep 300',
        'descripcion': 'Paso 4 de 7: Redes y publicación de puertos',
    },
    {
        'comando': "podman inspect api --format '{{range $k,$v := .NetworkSettings.Networks}}{{$k}}{{end}}'",
        'descripcion': 'Paso 5 de 7: Redes y publicación de puertos',
    },
    {
        'comando': 'podman rm -f api',
        'descripcion': 'Paso 6 de 7: Redes y publicación de puertos',
    },
    {
        'comando': 'podman network rm red-curso',
        'descripcion': 'Paso 7 de 7: Redes y publicación de puertos',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="demo").ejecutar_secuencia(SECUENCIA)
