"""Generador de output realista según el tipo de comando (modo demo).

Devuelve una lista de líneas que el terminal simularía; [] si el comando
normalmente no produce salida visible o no se conoce su salida.
Las salidas largas (apk update, git clone...) incluyen scroll completo
hasta el final (progress bar → Done) para verse profesionales en video.
"""

from __future__ import annotations

import re


def es_comando_largo(comando: str) -> bool:
    """True si el comando suele generar salida larga / espera de red."""
    patrones = (
        "apk update",
        "apk upgrade",
        "apk add",
        "pkg install",
        "pkg update",
        "pkg upgrade",
        "apt update",
        "apt upgrade",
        "apt install",
        "git clone",
        "git push",
        "git pull",
        "curl ",
        "wget ",
        "npm install",
        "npm i ",
        "pip install",
        "make ",
        "cmake ",
        "cargo build",
        "go build",
    )
    bajo = comando.strip().lower()
    return any(bajo.startswith(p) or f" {p}" in f" {bajo}" for p in patrones)


def _apk_update() -> list[str]:
    """apk update — índice completo + fetch con scroll profesional."""
    return [
        "fetch https://dl-cdn.alpinelinux.org/alpine/v3.22/main/x86_64/APKINDEX.tar.gz",
        "fetch https://dl-cdn.alpinelinux.org/alpine/v3.22/community/x86_64/APKINDEX.tar.gz",
        "OK: 27957 distinct packages available",
    ]


def _apk_upgrade() -> list[str]:
    """apk upgrade — progreso realista con scroll hasta el final."""
    return [
        "OK: 33294 KiB in 84 packages",
        "(1/6) Upgrading musl (1.2.5-r18 -> 1.2.5-r19)",
        "(2/6) Upgrading busybox (1.37.0-r29 -> 1.37.0-r31)",
        "(3/6) Upgrading alpine-base (3.4.0-r18 -> 3.4.0-r19)",
        "Executing alpine-base-3.4.0-r19.post-upgrade",
        "(4/6) Upgrading ssl_client (3.7.3-r0 -> 3.7.4-r0)",
        "(5/6) Upgrading ca-certificates-bundle (20241121-r0 -> 20241121-r1)",
        "(6/6) Upgrading libcrypto3 (3.3.3-r1 -> 3.3.4-r0)",
        "Executing busybox-1.37.0-r31.trigger",
        "Executing ca-certificates-bundle-20241121-r1.trigger",
        "OK: 33328 KiB in 84 packages",
    ]


def _apk_add(comando: str) -> list[str]:
    """apk add — install con progreso estilo Alpine."""
    resto = comando[len("apk add"):].strip()
    paquetes = [p for p in resto.split() if not p.startswith("-")]
    if not paquetes:
        return ["OK: 27957 distinct packages available"]
    lineas = [
        f"fetch https://dl-cdn.alpinelinux.org/alpine/v3.22/main/x86_64/APKINDEX.tar.gz",
        f"fetch https://dl-cdn.alpinelinux.org/alpine/v3.22/community/x86_64/APKINDEX.tar.gz",
        "(1/3) Installing ca-certificates-bundle (20241121-r1)",
        "(2/3) Installing nghttp2-libs (1.64.0-r0)",
        "(3/3) Installing " + (paquetes[0] if paquetes else "paquete"),
    ]
    for pkg in paquetes:
        lineas.append(f"Executing {pkg}-1.0.0-r0.trigger")
    # Barras de progreso estilo apk
    for pct in (0, 12, 28, 45, 62, 78, 91, 100):
        barra = "█" * (pct // 5) + "░" * (20 - pct // 5)
        lineas.append(f"{barra} {pct}%")
    lineas.append(f"OK: 12345 KiB in 87 packages")
    return lineas


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
    # Scroll completo: enumerar → comprimir → recibir con % → resolver → done
    lineas = [
        f"Cloning into '{repo}'...",
        "remote: Enumerating objects: 1547, done.",
        "remote: Counting objects: 100% (1547/1547), done.",
        "remote: Compressing objects: 100% (892/892), done.",
        "remote: Total 1547 (delta 701), reused 1298 (delta 589), pack-reused 0 (from 0)",
        "Receiving objects:   5% (78/1547), 120.00 KiB | 1.50 MiB/s",
        "Receiving objects:  15% (233/1547), 1.20 MiB | 4.10 MiB/s",
        "Receiving objects:  28% (434/1547), 2.80 MiB | 5.20 MiB/s",
        "Receiving objects:  41% (635/1547), 4.10 MiB | 4.80 MiB/s",
        "Receiving objects:  55% (851/1547), 5.60 MiB | 4.50 MiB/s",
        "Receiving objects:  68% (1052/1547), 7.20 MiB | 4.90 MiB/s",
        "Receiving objects:  81% (1254/1547), 8.80 MiB | 5.10 MiB/s",
        "Receiving objects:  94% (1455/1547), 10.40 MiB | 5.30 MiB/s",
        "Receiving objects: 100% (1547/1547), 11.20 MiB | 5.00 MiB/s, done.",
        "Resolving deltas:  35% (246/701)",
        "Resolving deltas:  68% (478/701)",
        "Resolving deltas: 100% (701/701), completed with 182 local objects.",
    ]
    return lineas


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
        "     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  84.0/84.0 kB 2.1 MB/s eta 0:00",
        "Collecting dependencia>=1.0 (from paquete)",
        "  Downloading dependencia-4.5.0-py3-none-any.whl (42 kB)",
        "     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  42.0/42.0 kB 1.8 MB/s eta 0:00",
        "Installing collected packages: dependencia, paquete",
        "Successfully installed dependencia-4.5.0 paquete-1.2.3",
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
        "npm warn deprecated paquete@1.0.0: Package no longer supported",
        "npm notice created a lockfile as package-lock.json",
        "added 142 packages, and audited 143 packages in 4s",
        "",
        "found 0 vulnerabilities",
    ]


def _curl_body() -> list[str]:
    return [
        "<!DOCTYPE html>",
        "<html lang=\"en\">",
        "<head><meta charset=\"utf-8\"><title>Ejemplo</title></head>",
        "<body><h1>Respuesta OK</h1></body>",
        "</html>",
    ]


def _wget(comando: str) -> list[str]:
    from datetime import datetime

    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    destino = comando.split()[-1] if comando.split() else "index.html"
    nombre = destino.rstrip("/").split("/")[-1] or "index.html"
    return [
        f"--{ahora}--  {destino}",
        "Resolving host... 1.2.3.4",
        "Connecting... connected.",
        "HTTP request sent, awaiting response... 200 OK",
        "Length: 12345 (12K) [text/html]",
        f"Saving to: '{nombre}'",
        "",
        f"{nombre:<16} 100%[===================>]  12.06K  --.-KB/s    in 0.01s",
        "",
        f"{ahora} (1.02 MB/s) - '{nombre}' saved [12345/12345]",
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
    (re.compile(r"^apk\s+update\b"), _apk_update),
    (re.compile(r"^apk\s+upgrade\b"), _apk_upgrade),
    (re.compile(r"^apk\s+add\b"), _apk_add),
    (re.compile(r"^pkg\s+install\b"), _pkg_install),
    (re.compile(r"^pkg\s+(update|upgrade)\b"), _pkg),
    (re.compile(r"^pkg\s+list-installed\b"), _pkg_list),
    (re.compile(r"^apt\s+update\b"), _pkg),
    (re.compile(r"^apt\s+upgrade\b"), _pkg),
    (re.compile(r"^apt\s+install\b"), _pkg_install),
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
    (re.compile(r"^curl\b"), _curl_body),
    (re.compile(r"^wget\b"), _wget),
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