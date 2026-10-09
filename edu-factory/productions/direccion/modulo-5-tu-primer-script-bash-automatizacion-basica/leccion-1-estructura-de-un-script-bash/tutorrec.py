#!/usr/bin/env python3
"""Tutorrec Cinematográfico - Generado por edu-factory.

Plan: Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
Módulo: Tu primer script Bash (automatización básica) · Lección: Estructura de un script Bash
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
        'comando': 'mkdir -p ~/bin',
        'descripcion': 'Paso 1 de 5: Estructura de un script Bash',
    },
    {
        'comando': "echo '#!/data/data/com.termux/files/usr/bin/bash' > ~/bin/mi-script.sh",
        'descripcion': 'Paso 2 de 5: Estructura de un script Bash',
    },
    {
        'comando': 'echo \'echo "Hola desde Termux"\' >> ~/bin/mi-script.sh',
        'descripcion': 'Paso 3 de 5: Estructura de un script Bash',
    },
    {
        'comando': 'chmod +x ~/bin/mi-script.sh',
        'descripcion': 'Paso 4 de 5: Estructura de un script Bash',
    },
    {
        'comando': '~/bin/mi-script.sh',
        'descripcion': 'Paso 5 de 5: Estructura de un script Bash',
    },
]

if __name__ == "__main__":
    CinematicTerminal(mode="demo").ejecutar_secuencia(SECUENCIA)
