#!/usr/bin/env python3
"""Tutorrec Cinematográfico - Generado por edu-factory.

Plan: Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
Módulo: Fundamentos y Podman rootless · Lección: Podman frente a Docker: el contenedor sin daemon
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
        'comando': 'podman --version',
        'descripcion': 'Paso 1 de 5: Podman frente a Docker: el contenedor sin daemon',
    },
    {
        'comando': "podman info --format '{{.Host.OS}} {{.Host.Arch}}'",
        'descripcion': 'Paso 2 de 5: Podman frente a Docker: el contenedor sin daemon',
    },
    {
        'comando': "podman info --format '{{.Host.Security.Rootless}}'",
        'descripcion': 'Paso 3 de 5: Podman frente a Docker: el contenedor sin daemon',
    },
    {
        'comando': 'echo "UID: $(id -u) - usuario: $USER"',
        'descripcion': 'Paso 4 de 5: Podman frente a Docker: el contenedor sin daemon',
    },
    {
        'comando': 'podman ps -a',
        'descripcion': 'Paso 5 de 5: Podman frente a Docker: el contenedor sin daemon',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="demo").ejecutar_secuencia(SECUENCIA)
