#!/usr/bin/env python3
"""Tutorrec Cinematográfico (modo real) - Generado por edu-factory.

Plan: Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
Módulo: Fundamentos y Podman rootless · Lección: Instalación y verificación en Fedora
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
        'comando': 'rpm -q podman',
        'descripcion': 'Paso 1 de 5: Instalación y verificación en Fedora',
    },
    {
        'comando': 'dnf list --installed podman',
        'descripcion': 'Paso 2 de 5: Instalación y verificación en Fedora',
    },
    {
        'comando': "podman info --format '{{.Version.Version}}'",
        'descripcion': 'Paso 3 de 5: Instalación y verificación en Fedora',
    },
    {
        'comando': 'podman run --rm docker.io/library/alpine:latest cat /etc/os-release',
        'descripcion': 'Paso 4 de 5: Instalación y verificación en Fedora',
    },
    {
        'comando': 'systemctl --user is-system-running',
        'descripcion': 'Paso 5 de 5: Instalación y verificación en Fedora',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="real").ejecutar_secuencia(SECUENCIA)
