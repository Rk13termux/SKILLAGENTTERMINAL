#!/usr/bin/env python3
"""Tutorrec Cinematográfico (modo real) - Generado por edu-factory.

Plan: Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
Módulo: Operación en producción · Lección: Firewall y exposición segura de servicios
6 comandos extraídos del plan maestro.
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
        'comando': 'firewall-cmd --state',
        'descripcion': 'Paso 1 de 6: Firewall y exposición segura de servicios',
    },
    {
        'comando': 'firewall-cmd --get-default-zone',
        'descripcion': 'Paso 2 de 6: Firewall y exposición segura de servicios',
    },
    {
        'comando': 'firewall-cmd --list-services',
        'descripcion': 'Paso 3 de 6: Firewall y exposición segura de servicios',
    },
    {
        'comando': 'firewall-cmd --list-ports',
        'descripcion': 'Paso 4 de 6: Firewall y exposición segura de servicios',
    },
    {
        'comando': 'firewall-cmd --list-all',
        'descripcion': 'Paso 5 de 6: Firewall y exposición segura de servicios',
    },
    {
        'comando': 'ss -tln',
        'descripcion': 'Paso 6 de 6: Firewall y exposición segura de servicios',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="real").ejecutar_secuencia(SECUENCIA)
