"""Secuencia cinematográfica: flujo de trabajo básico con Git."""

SECUENCIA = [
    {
        "comando": "git clone https://github.com/usuario/repo.git",
        "descripcion": "Clonar repositorio remoto",
        "output": [
            "Cloning into 'repo'...",
            "remote: Enumerating objects: 1234, done.",
            "Receiving objects: 100% (1234/1234), done.",
        ],
    },
    {
        "comando": "cd repo",
        "descripcion": "Entrar al directorio del proyecto",
        "output": [],
    },
    {
        "comando": "git status",
        "descripcion": "Ver estado del repositorio",
        "output": [
            "On branch main",
            "Your branch is up to date with 'origin/main'.",
            "nothing to commit, working tree clean",
        ],
    },
]

__all__ = ["SECUENCIA"]