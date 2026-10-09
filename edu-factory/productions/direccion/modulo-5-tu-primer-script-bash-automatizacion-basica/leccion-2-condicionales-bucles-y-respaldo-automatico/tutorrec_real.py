#!/usr/bin/env python3
"""Tutorrec Cinematográfico (modo real) - Generado por edu-factory.

Plan: Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
Módulo: Tu primer script Bash (automatización básica) · Lección: Condicionales, bucles y respaldo automático
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
        'comando': 'echo \'for archivo in *.sh; do echo "$archivo"; done\' >> ~/bin/listar.sh',
        'descripcion': 'Paso 1 de 6: Condicionales, bucles y respaldo automático',
    },
    {
        'comando': 'chmod +x ~/bin/listar.sh',
        'descripcion': 'Paso 2 de 6: Condicionales, bucles y respaldo automático',
    },
    {
        'comando': 'mkdir -p ~/backups',
        'descripcion': 'Paso 3 de 6: Condicionales, bucles y respaldo automático',
    },
    {
        'comando': "echo 'cp notas.txt ~/backups/notas-$(date +%Y%m%d).txt' >> ~/bin/respaldar.sh",
        'descripcion': 'Paso 4 de 6: Condicionales, bucles y respaldo automático',
    },
    {
        'comando': 'chmod +x ~/bin/respaldar.sh',
        'descripcion': 'Paso 5 de 6: Condicionales, bucles y respaldo automático',
    },
    {
        'comando': '~/bin/respaldar.sh',
        'descripcion': 'Paso 6 de 6: Condicionales, bucles y respaldo automático',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="real").ejecutar_secuencia(SECUENCIA)
