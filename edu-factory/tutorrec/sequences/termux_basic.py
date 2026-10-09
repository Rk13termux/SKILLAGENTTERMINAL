"""Secuencia cinematográfica: configuración básica de Termux."""

SECUENCIA = [
    {
        "comando": "termux-info",
        "descripcion": "Verificar información del sistema",
        "output": [
            "Termux Version: 0.118.0",
            "Android Version: 14",
            "Device: Xiaomi Redmi Note",
            "Architecture: aarch64",
        ],
    },
    {
        "comando": "pkg update && pkg upgrade -y",
        "descripcion": "Actualizar repositorios y paquetes",
        "output": [
            "Hit:1 https://packages.termux.dev/apt/termux-main stable InRelease",
            "Reading package lists... Done",
            "All packages are up to date.",
        ],
    },
    {
        "comando": "termux-setup-storage",
        "descripcion": "Conceder acceso al almacenamiento",
        "output": [
            "[Popup de Android: 'Permitir acceso a archivos']",
            "Storage access granted",
        ],
    },
    {
        "comando": "pkg install python git -y",
        "descripcion": "Instalar herramientas esenciales",
        "output": [
            "The following NEW packages will be installed:",
            "  python git",
            "Setting up python ...",
            "Setting up git ...",
            "Done!",
        ],
    },
]

__all__ = ["SECUENCIA"]