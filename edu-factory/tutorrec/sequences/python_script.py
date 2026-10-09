"""Secuencia cinematográfica: crear y ejecutar un script de Python."""

SECUENCIA = [
    {
        "comando": "nano hola.py",
        "descripcion": "Crear el script hola.py",
        "output": [
            "[Editor nano abierto]",
            "print('Hola desde Termux')",
        ],
    },
    {
        "comando": "python hola.py",
        "descripcion": "Ejecutar el script",
        "output": [
            "Hola desde Termux",
        ],
    },
]

__all__ = ["SECUENCIA"]