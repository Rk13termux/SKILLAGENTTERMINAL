"""Generador de output realista según el tipo de comando (modo demo).

Devuelve una lista de líneas que el terminal simularía; [] si el comando
normalmente no produce salida visible o no se conoce su salida.
"""

from __future__ import annotations

import re


def _pkg(comando: str) -> list[str]:
    return [
        "Hit:1 https://packages.termux.dev/apt/termux-main stable InRelease",
        "Reading package lists... Done",
        "Building dependency tree... Done",
        "Reading state information... Done",
        "All packages are up to date.",
    ]


def _pkg_install(comando: str) -> list[str]:
    resto = comando[len("pkg install"):].strip().split(" -y")[0].strip()
    paquetes = resto.split()
    if not paquetes:
        return ["Reading package lists... Done", "0 upgraded, 0 newly installed."]
    lineas = [
        "Reading package lists... Done",
        "Building dependency tree... Done",
        "The following NEW packages will be installed:",
    ]
    for paquete in paquetes:
        lineas.append(f"  {paquete}")
    lineas.append(f"{len(paquetes)} newly installed, 0 to remove.")
    lineas.append(f"Need to get {len(paquetes) * 3} MB of archives.")
    lineas.append(f"Get:1 ... {', '.join(paquetes)}")
    lineas.append("Fetched ... in 8s (1.2 MB/s)")
    for paquete in paquetes:
        lineas.append(f"Setting up {paquete} ...")
    lineas.append("Processing triggers ...")
    lineas.append("Done!")
    return lineas


def _pkg_list() -> list[str]:
    return [
        "bash 5.2.26-0            A POSIX-compatible shell",
        "python 3.12.3-1          A programming language",
        "openssh 9.7p1-1          Secure shell client and server",
    ]


def _git_clone(comando: str) -> list[str]:
    match = re.search(r"git clone\s+(\S+)", comando)
    url = match.group(1) if match else "url"
    repo = url.rstrip("/").split("/")[-1]
    if repo.endswith(".git"):
        repo = repo[:-4]
    return [
        f"Cloning into '{repo}'...",
        "remote: Enumerating objects: 42, done.",
        "remote: Counting objects: 100% (42/42), done.",
        "remote: Compressing objects: 100% (30/30), done.",
        "remote: Total 42 (delta 10), reused 42 (delta 10)",
        "Receiving objects: 100% (42/42), 1.20 MiB | 1.10 MiB/s, done.",
        "Resolving deltas: 100% (10/10), done.",
    ]


def _git_status() -> list[str]:
    return [
        "On branch main",
        "Your branch is up to date with 'origin/main'.",
        "",
        "nothing to commit, working tree clean",
    ]


def _git_init() -> list[str]:
    return [
        "hint: Using 'master' as the name for the initial branch.",
        "Initialized empty Git repository in /com/termux/files/home/repo/.git/",
    ]


def _git_commit() -> list[str]:
    return [
        "[main 3f2a1b4] Cambios guardados",
        " 1 file changed, 3 insertions(+)",
    ]


def _git_push() -> list[str]:
    return [
        "Enumerating objects: 5, done.",
        "Counting objects: 100% (5/5), done.",
        "Writing objects: 100% (5/5), 620 bytes | 620.00 KiB/s, done.",
        "Total 5 (delta 2), reused 0 (delta 0)",
        "To https://github.com/usuario/repo.git",
        "   a1b2c3d..e4f5g6h  main -> main",
    ]


def _git_remote() -> list[str]:
    return ["set-url origin", "remote origin already exists"]


def _git_config() -> list[str]:
    return []


def _git_branch(comando: str) -> list[str]:
    extra = comando[len("git branch"):].strip()
    if extra.startswith("-M"):
        return [f"Renamed the current branch to '{extra.split()[-1]}'"]
    return []


def _git_checkout(comando: str) -> list[str]:
    target = comando.split("checkout", 1)[1].strip()
    return [f"Switched to branch '{target}'"]


def _git_merge() -> list[str]:
    return [
        "Updating a1b2c3d..e4f5g6h",
        "Fast-forward",
        " README.md | 5 +++++",
        " 1 file changed, 5 insertions(+)",
    ]


def _python_version() -> list[str]:
    return ["Python 3.12.3"]


def _python_venv() -> list[str]:
    return []


def _pip_version() -> list[str]:
    return [
        "pip 24.0 from /usr/lib/python3.12/site-packages/pip (python 3.12)",
    ]


def _pip_install() -> list[str]:
    return [
        "Collecting paquete",
        "  Downloading paquete-1.2.3-py3-none-any.whl (84 kB)",
        "Installing collected packages: paquete",
        "Successfully installed paquete-1.2.3",
    ]


def _node_version() -> list[str]:
    return ["v22.9.0"]


def _npm_version() -> list[str]:
    return ["10.9.0"]


def _npm_init() -> list[str]:
    return [
        "Wrote to /home/package.json:",
        "",
        "{",
        '  "name": "app",',
        '  "version": "1.0.0",',
        '  "main": "index.js",',
        "}",
    ]


def _npm_install() -> list[str]:
    return [
        "added 1 package in 4s",
        "found 0 vulnerabilities",
    ]


def _ssh_keygen() -> list[str]:
    return [
        "Generating public/private ed25519 key pair.",
        "Enter passphrase (empty for no passphrase):",
        "Enter same passphrase again:",
        "Your identification has been saved in /home/.ssh/id_ed25519",
        "Your public key has been saved in /home/.ssh/id_ed25519.pub",
        "The key fingerprint is:",
        "SHA256:u9Kx0abc123uvwXyZ usuario@hostname",
    ]


def _ssh_copy_id() -> list[str]:
    return [
        "/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s)",
        "Number of key(s) added: 1",
        "Now try logging into the machine, with: ssh usuario@192.168.1.10",
    ]


def _termux_info() -> list[str]:
    return [
        "Termux Version: 0.118.0",
        "Android Version: 14",
        "Device: Pixel 7",
        "Architecture: aarch64",
        "Kernel: 5.10.101-android12-9",
    ]


def _termux_storage() -> list[str]:
    return [
        "Info: Storage access was granted.",
    ]


def _echo(comando: str) -> list[str]:
    resto = comando[len("echo"):].strip()
    if resto.startswith("$"):
        resto = resto[1:].strip() or "usuario"
    if resto.startswith('--'):
        resto = resto.lstrip("-").strip()
    match = re.match(r"""^(["'])(.*?)\1""", resto)
    if match:
        return [match.group(2)]
    return [resto.split(">>")[0].split(">")[0].strip() or "usuario"]


def _ping() -> list[str]:
    return [
        "PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.",
        "64 bytes from 8.8.8.8: icmp_seq=1 ttl=118 time=8.21 ms",
        "64 bytes from 8.8.8.8: icmp_seq=2 ttl=118 time=8.14 ms",
        "64 bytes from 8.8.8.8: icmp_seq=3 ttl=118 time=8.33 ms",
        "",
        "--- 8.8.8.8 ping statistics ---",
        "3 packets transmitted, 3 received, 0% packet loss",
        "rtt min/avg/max/mdev = 8.140/8.227/8.330/0.080 ms",
    ]


def _curl_headers() -> list[str]:
    return [
        "HTTP/2 200",
        "server: nginx",
        "content-type: text/html",
        "content-length: 2588",
        "date: hoy",
    ]


REGLA: list[tuple[re.Pattern, object]] = [
    (re.compile(r"^pkg\s+install\b"), _pkg_install),
    (re.compile(r"^pkg\s+(update|upgrade)\b"), _pkg),
    (re.compile(r"^pkg\s+list-installed\b"), _pkg_list),
    (re.compile(r"^git\s+clone\b"), _git_clone),
    (re.compile(r"^git\s+status\b"), _git_status),
    (re.compile(r"^git\s+init\b"), _git_init),
    (re.compile(r"^git\s+commit\b"), _git_commit),
    (re.compile(r"^git\s+push\b"), _git_push),
    (re.compile(r"^git\s+remote\b"), _git_remote),
    (re.compile(r"^git\s+config\b"), _git_config),
    (re.compile(r"^git\s+branch\b"), _git_branch),
    (re.compile(r"^git\s+checkout\b"), _git_checkout),
    (re.compile(r"^git\s+merge\b"), _git_merge),
    (re.compile(r"^python\w*\s+--version\b"), _python_version),
    (re.compile(r"^python\w*\s+-m\s+venv\b"), _python_venv),
    (re.compile(r"^python\w*\s+.*\.py\b"), _python_venv),
    (re.compile(r"^pip\s+--version\b"), _pip_version),
    (re.compile(r"^pip\s+install\b"), _pip_install),
    (re.compile(r"^node\s+--version\b"), _node_version),
    (re.compile(r"^npm\s+--version\b"), _npm_version),
    (re.compile(r"^npm\s+init\b"), _npm_init),
    (re.compile(r"^npm\s+install\b"), _npm_install),
    (re.compile(r"^ssh-keygen\b"), _ssh_keygen),
    (re.compile(r"^ssh-copy-id\b"), _ssh_copy_id),
    (re.compile(r"^termux-info\b"), _termux_info),
    (re.compile(r"^termux-setup-storage\b"), _termux_storage),
    (re.compile(r"^echo\b"), _echo),
    (re.compile(r"^ping\b"), _ping),
    (re.compile(r"^curl\s+-\w*I\b"), _curl_headers),
]


def generar_output_realista(comando: str) -> list[str]:
    comando = comando.strip().strip(";")
    for patron, generador in REGLA:
        if patron.match(comando):
            try:
                return generador(comando)
            except TypeError:
                return generador()
    return []


__all__ = ["generar_output_realista"]