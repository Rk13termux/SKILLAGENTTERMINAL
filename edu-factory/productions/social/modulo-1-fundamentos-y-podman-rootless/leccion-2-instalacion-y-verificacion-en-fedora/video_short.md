# Video corto (TikTok / Reels / Shorts) — Lección 2

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 1. Fundamentos y Podman rootless
**Lección:** 2. Instalación y verificación en Fedora
**Duración máxima:** 60 segundos
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Guion con marcas de tiempo

### [0:00-0:03] GANCHO
- **Texto en pantalla:** «Paquetes podman, buildah y skopeo en Fedora» paso a paso, sin relleno (lección 2).
- **Hook visual:** Plano de pantalla ejecutando el primer comando: `rpm -q podman`. Sin zoom lento: el resultado debe verse desde el primer segundo.

### [0:03-0:15] CONTEXTO
Qué se resuelve: Paquetes podman, buildah y skopeo en Fedora. Fedora incluye Podman en sus repositorios, así que la instalación es una sola transacción de DNF. Tras instalarlo conviene verificar la versión, el backend de almacenamiento y que el entorno rootless esté operativo en la sesión del usuario. Plantea el problema en una frase y di que el comando o el proceso de la lección lo cierra.

### [0:15-0:45] DEMO
1. Ejecuta en pantalla `rpm -q podman` y comenta en voz alta qué hace cada parte.
2. Ejecuta en pantalla `dnf list --installed podman` y comenta en voz alta qué hace cada parte.
3. Ejecuta en pantalla `podman info --format '{{.Version.Version}}'` y comenta en voz alta qué hace cada parte.
4. Menciona que hay 5 comandos en total y que el resto está en el material del curso.

### [0:45-0:55] RESULTADO
Cierre en pantalla: resultado correcto de «Paquetes podman, buildah y skopeo en Fedora» visible. Frase final: «esto es lo que hace falta para paquetes podman, buildah y skopeo en fedora; el resto es práctica».

### [0:55-1:00] CTA
«Guarda este video y practica esto hoy: Instala el paquete con sudo dnf install -y podman y confirma con rpm -q que quedó registrado. Sígueme para el siguiente paso de Podman en Fedora: contenedores sin Docker».

## Voz en off (texto plano para Edge-TTS, ~130 palabras)

Lección 2 del módulo 1 de Podman en Fedora: contenedores sin Docker. Fedora incluye Podman en sus repositorios, así que la instalación es una sola transacción de DNF. Tras instalarlo conviene verificar la versión, el backend de almacenamiento y que el entorno rootless esté operativo en la sesión del usuario. Primero vemos Paquetes podman, buildah y skopeo en Fedora, Verificación de versión y del cgroup v2 en modo rootless, Actualizaciones con dnf y reinicio de la sesión de usuario y después Diagnóstico rápido con podman info. En pantalla ejecuto 5 comandos, empezando por `rpm -q podman`. Observa qué cambia antes y después. El resultado debe verse completo antes de cerrar; si algo falla, revisa el mensaje de error en lugar de repetir a ciegas. Para practicar: Instala el paquete con sudo dnf install -y podman y confirma con rpm -q que quedó registrado. En el

## Hashtags

#paquetespodmanbuildahyskopeoenfedora #paquetes #podman #buildah #skopeo #fedora #verificaciondeversionydelcgroupv2enmodorootless #verificacion #version #cgroup #rootless #actualizacionescondnfyreiniciodelasesiondeusuario #actualizaciones #reinicio
