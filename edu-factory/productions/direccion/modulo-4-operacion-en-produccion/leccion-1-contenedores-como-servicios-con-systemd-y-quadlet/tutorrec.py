#!/usr/bin/env python3
"""Tutorrec Cinematográfico - Generado por edu-factory.

Plan: Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
Módulo: Operación en producción · Lección: Contenedores como servicios con systemd y Quadlet
9 comandos extraídos del plan maestro.
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
        'comando': 'mkdir -p ~/.config/containers/systemd',
        'descripcion': 'Paso 1 de 9: Contenedores como servicios con systemd y Quadlet',
    },
    {
        'comando': "printf '[Unit]\\nDescription=Nginx gestionado por Podman\\n[Container]\\nImage=docker.io/library/nginx:alpine\\nPublishPort=8082:80\\n[Install]\\nWantedBy=default.target\\n' > ~/.config/containers/systemd/nginx.container",
        'descripcion': 'Paso 2 de 9: Contenedores como servicios con systemd y Quadlet',
    },
    {
        'comando': 'systemctl --user daemon-reload',
        'descripcion': 'Paso 3 de 9: Contenedores como servicios con systemd y Quadlet',
    },
    {
        'comando': 'systemctl --user start nginx.service',
        'descripcion': 'Paso 4 de 9: Contenedores como servicios con systemd y Quadlet',
    },
    {
        'comando': 'systemctl --user status nginx.service --no-pager',
        'descripcion': 'Paso 5 de 9: Contenedores como servicios con systemd y Quadlet',
    },
    {
        'comando': "curl -s -o /dev/null -w 'HTTP %{http_code}\\n' http://localhost:8082",
        'descripcion': 'Paso 6 de 9: Contenedores como servicios con systemd y Quadlet',
    },
    {
        'comando': 'systemctl --user stop nginx.service',
        'descripcion': 'Paso 7 de 9: Contenedores como servicios con systemd y Quadlet',
    },
    {
        'comando': 'rm ~/.config/containers/systemd/nginx.container',
        'descripcion': 'Paso 8 de 9: Contenedores como servicios con systemd y Quadlet',
    },
    {
        'comando': 'systemctl --user daemon-reload',
        'descripcion': 'Paso 9 de 9: Contenedores como servicios con systemd y Quadlet',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="demo").ejecutar_secuencia(SECUENCIA)
