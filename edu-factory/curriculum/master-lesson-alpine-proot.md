# Alpine Linux en proot-distro: Linux completo dentro de Android sin root

## Metadata
- id: ALPINE-PROOT
- nivel: intermedio
- duracion: 3 semanas
- audiencia: desarrolladores y entusiastas de Linux que quieren un entorno completo en su celular sin root
- idioma: español
- plataforma: Android + Termux + proot-distro + Alpine Linux (musl, apk, OpenRC)

## Objetivos
- Identificar el sistema Alpine en ejecución con os-release, uname y alpine-release.
- Gestionar paquetes exclusivamente con apk (add, del, search, info), sin apt ni pkg y sin operaciones largas de red.
- Crear usuarios, configurar sudo de forma no interactiva y operar con privilegios elevados dentro del contenedor.
- Diagnosticar archivos, red y utilidades busybox dentro del entorno proot.
- Gestionar servicios con OpenRC (rc-service, rc-update, openrc, rc-status), nunca con systemctl.
- Montar un stack de desarrollo: git, Python 3 con venv, y Node.js con npm.
- Auditar entorno, PATH y recursos del sistema sin depender de herramientas externas a Alpine.
- Validar end-to-end un Alpine funcional en Android con una checklist final verificable.

## Módulo 1: Fundamentos del sistema Alpine

### Lección 1: Por qué Alpine y qué estás usando

**Resumen:** Alpine Linux es una distribución minimalista basada en musl y BusyBox que usa apk como gestor de paquetes y OpenRC como sistema de init. Ya estás dentro del contenedor proot; esta lección siente las bases conceptuales con comandos locales, sin salir ni instalar nada.

**Temas:**
- Alpine vs Debian/Ubuntu: musl en lugar de glibc, apk en lugar de apt, OpenRC en lugar de systemd
- Qué es proot y por qué no necesita root de Android
- Límites del entorno proot (sin systemd, servicios con OpenRC)
- Mapa del curso: 3 semanas, 6 módulos, 18 lecciones

**Comandos:**
- uname -m
- uname -r
- echo "Alpine dentro de proot: comandos locales"
- cat /etc/alpine-release

**Ejercicios:**
- Anota la arquitectura de tu dispositivo con uname -m (arm64 o aarch64 es lo habitual).
- Escribe en tus propias palabras por qué apk y OpenRC van juntos en Alpine.

**Recursos:**
- Wiki oficial de Alpine Linux (musl y apk)

### Lección 2: Identifica tu sistema Alpine

**Resumen:** Antes de tocar paquetes, confirma qué estás ejecutando: /etc/os-release describe la distribución, uname da kernel y host, y /etc/alpine-release fija la versión exacta de Alpine. Son comandos de solo lectura, ideales para grabar sin riesgo.

**Temas:**
- /etc/os-release: ID, VERSION_ID, PRETTY_NAME
- uname -a para host, kernel y arquitectura
- /etc/alpine-release y su versión
- whoami, id y pwd para saber quién y dónde estás

**Comandos:**
- cat /etc/os-release
- uname -a
- cat /etc/alpine-release
- whoami
- id
- pwd

**Ejercicios:**
- Confirma con /etc/os-release que ID=alpine.
- Compara uname -m y uname -r y anota ambos valores.

**Recursos:**
- Alpine Linux Wiki: primera instalación (referencia de os-release)

### Lección 3: Primer contacto con apk y el shell

**Resumen:** Dentro de Alpine, apk es el único gestor de paquetes que necesitas. Con apk update refrescas los índices del repositorio, con apk search localizas paquetes y con apk info inspeccionas lo instalado. El shell base es ash de BusyBox, aunque puedes instalar bash.

**Temas:**
- apk update y apk version
- Buscar paquetes con apk search
- Inspeccionar instalados con apk info
- ash, busybox y bash dentro de Alpine

**Comandos:**
- apk update
- apk version
- apk search --description bash
- apk info | head -5
- which busybox ash sh
- busybox | head -1

**Ejercicios:**
- Ejecuta apk update y confirma que termina sin errores.
- Localiza el paquete de curl con apk search y revisa su descripción.

**Recursos:**
- Manual de apk (Alpine Linux)

## Módulo 2: Paquetes, usuarios y sudo

### Lección 1: Gestión de paquetes con apk

**Resumen:** apk cubre el ciclo de paquetes: instalar con apk add, eliminar con apk del, inspeccionar con apk info. En esta lección practicas add/del/info con paquetes pequeños, sin upgrade completo (eso es lento y no hace falta para aprender).

**Temas:**
- apk add y apk del en la práctica
- apk info y apk info -a para metadatos
- apk info --who-owns para ver el dueño de un binario
- Por qué evitamos apk upgrade en demos (tarda demasiado)

**Comandos:**
- apk add tree
- apk info -a tree | head -8
- tree --version
- apk info --who-owns /usr/bin/tree
- apk del tree
- apk info tree 2>&1 | head -2 || echo "tree eliminado"

**Ejercicios:**
- Instala tree, inspecciónalo con apk info -a y elimínalo con apk del.
- Confirma con apk info que el paquete ya no está instalado.

**Recursos:**
- Referencia de apk en la wiki de Alpine

### Lección 2: Usuarios, grupos y sudo

**Resumen:** Alpine trae adduser para crear cuentas y sudo está disponible como paquete. La configuración segura de privilegios se hace con un archivo en /etc/sudoers.d, validando la sintaxis de sudoers de forma no interactiva.

**Temas:**
- id, whoami y grupos del sistema
- Crear un usuario con adduser -D
- Instalar sudo con apk
- Autorizar al usuario sin contraseña con /etc/sudoers.d

**Comandos:**
- id
- whoami
- apk add sudo
- adduser -D dev
- echo "dev ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/dev
- chmod 440 /etc/sudoers.d/dev
- visudo -c

**Ejercicios:**
- Crea el usuario dev y actívalo para sudo sin contraseña.
- Comprueba la sintaxis de los archivos sudoers con visudo -c.

**Recursos:**
- sudoers.d en la wiki de Alpine

### Lección 3: Operar con sudo y entorno del usuario

**Resumen:** Con sudo instalado y el usuario autorizado, cada comando privilegiado se ejecuta con sudo delante. Verificas que sudo whoami responde root y revisas el PATH del sistema dentro del proot.

**Temas:**
- sudo whoami
- Cambiar de usuario con sudo -u
- PATH y entorno en Alpine musl
- Variables de entorno básicas

**Comandos:**
- whoami
- sudo whoami
- sudo -u dev whoami
- echo $PATH
- echo $HOME
- sudo id

**Ejercicios:**
- Confirma con sudo whoami que la elevación funciona desde el usuario no root.
- Cambia al usuario dev con sudo -u dev y verifica la identidad con id.

**Recursos:**
- Manual de sudo

## Módulo 3: Sistema de archivos, red y utilidades

### Lección 1: Estructura del sistema Alpine

**Resumen:** Alpine deja ver su configuración en /etc/apk (repositorios), sus init scripts en /etc/init.d y su estado de montaje con mount. Conocer estas rutas te permite auditar el sistema en segundos.

**Temas:**
- /etc/apk/repositories y los repositorios main y community
- /etc/init.d y los scripts de OpenRC
- mount y df para ver el espacio
- /etc/os-release y /etc/apk/world como inventario

**Comandos:**
- cat /etc/apk/repositories
- ls /etc/init.d | head -5
- ls /etc/apk
- mount | head -5
- df -h
- cat /etc/apk/world | head -10

**Ejercicios:**
- Revisa /etc/apk/repositories y confirma que incluye main y community.
- Lista los init scripts y cuenta cuántos hay con ls /etc/init.d | wc -l.

**Recursos:**
- Alpine Linux Wiki: repositorios

### Lección 2: Red dentro del proot

**Resumen:** proot hereda la red del sistema anfitrión. Compruebas la interfaz con ip addr, el resolutor con /etc/resolv.conf y la conectividad con ping. Si curl ya está instalado, puedes verificar HTTPS; si no, lo omitimos para no depender de red en la demo.

**Temas:**
- ip addr y las interfaces heredadas
- /etc/resolv.conf y resolución de nombres
- ping para latencia y ruta
- curl solo si ya está en el sistema (apk info curl)

**Comandos:**
- ip addr show 2>/dev/null || ifconfig 2>/dev/null | head -8
- cat /etc/resolv.conf
- ping -c 2 1.1.1.1
- apk info curl 2>/dev/null | head -1 || echo "curl no instalado"
- command -v curl || echo "sin curl: usamos solo ping y resolv.conf"

**Ejercicios:**
- Diagnostica la conectividad con ping a 1.1.1.1.
- Revisa /etc/resolv.conf y comprueba que hay al menos un nameserver.

**Recursos:**
- Documentación de iproute2 (ip addr)

### Lección 3: BusyBox, grep, find y sed

**Resumen:** Alpine es sinónimo de BusyBox: una sola multinilla con decenas de utilidades. Junto con grep, find y sed tienes el kit de supervivencia para buscar configuraciones y editar archivos sin instalar nada más.

**Temas:**
- BusyBox y su lista de applets con busybox --list
- find para localizar archivos por nombre
- grep para buscar dentro de archivos y directorios
- sed para ediciones puntuales en línea

**Comandos:**
- busybox --list | wc -l
- which busybox
- find /etc -name "*.conf" | head -5
- grep -R "nameserver" /etc 2>/dev/null | head -3
- sed -n "1,3p" /etc/os-release

**Ejercicios:**
- Cuenta las applets de BusyBox con busybox --list | wc -l.
- Usa grep -R para localizar nameserver en /etc/resolv.conf.

**Recursos:**
- BusyBox oficial (lista de comandos embebidos)

## Módulo 4: OpenRC: servicios y arranque

### Lección 1: OpenRC frente a systemd

**Resumen:** Alpine no usa systemd: su init es OpenRC. rc-status muestra el estado de los servicios y los runlevels (sysinit, boot, default). Entender este modelo es clave para no buscar systemctl donde no existe.

**Temas:**
- Filosofía de OpenRC y su relación con Alpine
- Runlevels: sysinit, boot, default
- rc-status y rc-status default
- Por qué no hay systemctl en Alpine

**Comandos:**
- rc-status
- rc-status default
- rc-status --help | head -5
- ls /etc/runlevels
- ls /etc/runlevels/default

**Ejercicios:**
- Ejecuta rc-status y anota qué servicios están started o stopped.
- Lista los servicios del runlevel default con ls /etc/runlevels/default.

**Recursos:**
- Manual de OpenRC

### Lección 2: Gestionar servicios con rc-service

**Resumen:** rc-service arranca, detiene y consulta servicios con la sintaxis rc-service <servicio> <start|stop|restart|status>. Usamos servicios pequeños ya disponibles o fáciles de instalar con apk, sin depender de systemd.

**Temas:**
- rc-service start, stop, restart y status
- Servicios típicos de Alpine (crond, sshd si existen)
- Observar estado sin abrir un editor
- Limitaciones en proot (ciertos servicios no arrancan igual que en VM)

**Comandos:**
- rc-service --list 2>/dev/null | head -5 || ls /etc/init.d | head -5
- rc-service crond status 2>&1 || true
- rc-service sshd status 2>&1 || true
- ls /etc/init.d/crond 2>/dev/null || ls /etc/init.d | grep -i cron || echo "sin cron en init.d"

**Ejercicios:**
- Revisa el estado de crond o sshd con rc-service status (puede estar stopped: es normal en proot).
- Lista los init scripts disponibles y elige dos para inspeccionar.

**Recursos:**
- rc-service(8) en la wiki de OpenRC

### Lección 3: Habilitar servicios con rc-update y openrc

**Resumen:** Arrancar un servicio es temporal: para que vuelva con el sistema se registra en un runlevel con rc-update add. rc-update del lo elimina, rc-update show lista el estado. Este es el trabajo diario de administración en Alpine.

**Temas:**
- rc-update add <servicio> default
- rc-update del y rc-update show
- openrc default como arranque del runlevel
- Relación entre /etc/init.d y /etc/runlevels

**Comandos:**
- rc-update show
- rc-update show default
- ls /etc/runlevels/default
- rc-update add crond default 2>&1 || true
- rc-update show default
- rc-update del crond default 2>&1 || true
- rc-update show default

**Ejercicios:**
- Habilita crond en default, verifica con rc-update show y luego retíralo.
- Explica con tus palabras la diferencia entre rc-service crond start y rc-update add crond default.

**Recursos:**
- rc-update(8) y runlevels (OpenRC)

## Módulo 5: Stack de desarrollo (git, Python, Node.js)

### Lección 1: Git y SSH en Alpine

**Resumen:** Git es imprescindible para cualquier flujo de desarrollo. En Alpine se instala con apk git. Configuras tu identidad global y verificas que git y ssh responden con sus versiones.

**Temas:**
- apk add git y openssh-client
- git --version y ssh -V
- git config --global user.name y user.email
- Clave SSH con ssh-keygen (generación local, sin subir a ningún sitio)

**Comandos:**
- apk add git openssh-client
- git --version
- ssh -V
- git config --global user.name "Dev Alpine"
- git config --global user.email "dev@alpine.local"
- git config --global --list
- ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N "" -C "dev@alpine.local" -q
- ls ~/.ssh/id_ed25519.pub

**Ejercicios:**
- Instala git, configura tu identidad y genera una clave ed25519 local.
- Verifica con git config --global --list que la identidad quedó registrada.

**Recursos:**
- Git book (configuración inicial)

### Lección 2: Python 3, pip y venv en musl

**Resumen:** Alpine usa musl, así que conviene trabajar con venv por proyecto. Con python3 y py3-pip montas entornos aislados; en esta lección creamos el venv y verificamos pip sin instalar paquetes de red pesados.

**Temas:**
- apk add python3 y py3-pip
- Nota sobre musl y paquetes nativos
- python3 -m venv para entornos aislados
- pip --version y pip list (listado local del venv)

**Comandos:**
- apk add python3 py3-pip
- python3 --version
- pip3 --version
- python3 -m venv /tmp/venv-alp
- /tmp/venv-alp/bin/pip --version
- /tmp/venv-alp/bin/pip list

**Ejercicios:**
- Crea un venv en /tmp/venv-alp y verifica que pip responde dentro de él.
- Comprueba con pip list que el entorno arranca vacío (solo pip y setuptools si aplica).

**Recursos:**
- Python packaging user guide (venv)

### Lección 3: Node.js y npm

**Resumen:** Node.js y npm se instalan directamente con apk. Con npm init -y generas un package.json mínimo; en esta lección verificamos versiones y estructura sin descargar dependencias de npm (evita esperas de red en la demo).

**Temas:**
- apk add nodejs y npm
- node --version y npm --version
- npm init -y para un package.json
- Estructura de un proyecto npm local

**Comandos:**
- apk add nodejs npm
- node --version
- npm --version
- mkdir -p /tmp/nodetest && cd /tmp/nodetest
- npm init -y
- cat package.json | head -8
- node -e "console.log('Node OK en Alpine')"

**Ejercicios:**
- Crea el proyecto /tmp/nodetest con npm init -y y revisa el package.json.
- Ejecuta un script inline con node -e que imprima un mensaje de verificación.

**Recursos:**
- Node.js en Alpine packages

## Módulo 6: Auditoría del entorno, mantenimiento y cierre

### Lección 1: Entorno, PATH y recursos del sistema

**Resumen:** Antes de cerrar el curso, auditas lo que realmente estás usando: usuario, PATH, HOME, memoria y espacio en disco. Todo con comandos locales de Alpine, sin salir del proot ni invocar herramientas de Termux.

**Temas:**
- whoami, id, pwd y $HOME
- echo $PATH y $SHELL
- free -m y df -h para recursos
- uptime y cat /proc/cpuinfo | head para el equipo

**Comandos:**
- whoami
- id
- pwd
- echo $HOME
- echo $PATH
- echo $SHELL
- free -m 2>/dev/null | head -2 || cat /proc/meminfo | head -2
- df -h | head -3
- uptime

**Ejercicios:**
- Documenta usuario, PATH y espacio libre en un solo bloque de notas.
- Compara free -m (si existe) con /proc/meminfo y anota la memoria total.

**Recursos:**
- Manual de free (procps) o lectura directa de /proc/meminfo

### Lección 2: Mantenimiento con apk

**Resumen:** En un celular el espacio es oro. Con apk info --installed inventarias lo que hay, con apk del retiras lo que no usas y con apk cache limpias la caché sin tocar el sistema base. Evitamos apk upgrade en demos por su duración.

**Temas:**
- apk info --installed como inventario
- apk del para reducir el rootfs
- apk cache clean y /var/cache/apk
- Tamaño con du y df antes y después

**Comandos:**
- apk info --installed | wc -l
- du -sh /var/cache/apk 2>/dev/null || echo cache-vacia
- apk del tree 2>/dev/null || true
- apk cache clean 2>/dev/null || true
- du -sh /var/cache/apk 2>/dev/null || echo cache-vacia-tras-clean
- apk info --installed | wc -l

**Ejercicios:**
- Cuenta los paquetes instalados antes y después de una limpieza de cache.
- Ejecuta apk cache clean y comprueba el tamaño de /var/cache/apk con du.

**Recursos:**
- apk-cache(8) en la wiki de Alpine

### Lección 3: Checklist final de validación

**Resumen:** El cierre del curso es una verificación end-to-end: que apk funcione, que OpenRC responda, que el stack de desarrollo responda y que el entorno sea auditable. Ejecutas una sola tanda de comandos locales y confirmas que Alpine está plenamente operativo en tu Android.

**Temas:**
- Batería de pruebas: apk, OpenRC, git, Python, Node
- Auditoría rápida con os-release y world
- Cómo documentar tu entorno para reproducirlo en otro teléfono
- Próximos pasos: dotfiles, más paquetes, scripts de arranque

**Comandos:**
- apk --version
- openrc --version 2>/dev/null | head -1 || rc-status --version 2>/dev/null | head -1 || echo "openrc: comprobar rc-status"
- git --version 2>/dev/null || echo "git pendiente de apk add"
- python3 --version 2>/dev/null || echo "python3 pendiente de apk add"
- node --version 2>/dev/null || echo "node pendiente de apk add"
- cat /etc/os-release | grep ^ID
- cat /etc/alpine-release
- echo CHECKLIST-ALPINE-OK

**Ejercicios:**
- Ejecuta la batería completa y confirma que el último comando imprime CHECKLIST-ALPINE-OK.
- Exporta tu /etc/apk/world como plantilla para replicar el entorno.

**Recursos:**
- Alpine Linux Wiki: administración del sistema
