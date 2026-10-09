#!/usr/bin/env python3
"""Tutorrec Cinematográfico - Generado por edu-factory.

Plan: Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
Módulo: Tu primer script Bash (automatización básica) · Lección: Programar tareas con cron y termux-wake-lock
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
        'comando': 'pkg install termux-services',
        'descripcion': 'Paso 1 de 6: Programar tareas con cron y termux-wake-lock',
    },
    {
        'comando': 'sv-enable crond',
        'descripcion': 'Paso 2 de 6: Programar tareas con cron y termux-wake-lock',
    },
    {
        'comando': 'termux-wake-lock',
        'descripcion': 'Paso 3 de 6: Programar tareas con cron y termux-wake-lock',
    },
    {
        'comando': 'crontab -e',
        'descripcion': 'Paso 4 de 6: Programar tareas con cron y termux-wake-lock',
    },
    {
        'comando': "printf '*/30 * * * * ~/bin/respaldar.sh\\n' | crontab -",
        'descripcion': 'Paso 5 de 6: Programar tareas con cron y termux-wake-lock',
    },
    {
        'comando': 'crontab -l',
        'descripcion': 'Paso 6 de 6: Programar tareas con cron y termux-wake-lock',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="demo").ejecutar_secuencia(SECUENCIA)
