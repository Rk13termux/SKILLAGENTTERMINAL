# Termux desde Cero: Domina la terminal en tu Android

## Metadata
- id: TERMUX-101
- nivel: principiante a intermedio
- duracion: 4 semanas
- audiencia: principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular
- idioma: español
- plataforma: Termux (Play Store y F-Droid)

## Objetivos
- Configurar Termux de forma segura y distinguir la versión correcta de la Play Store.
- Dominar los comandos esenciales de Linux para moverse por el sistema de archivos.
- Gestionar archivos, permisos y editores de texto desde la terminal.
- Instalar y usar entornos de desarrollo reales: Python, Node.js y Git.
- Escribir y automatizar tareas con scripts Bash.
- Usar Git y GitHub para guardar y compartir código desde el celular.
- Conectarte a otros equipos por SSH y diagnosticar redes con ping y curl.
- Combinar todo en un proyecto final: un bot de Telegram desplegado desde Termux.

## Módulo 1: Configuración inicial y mitos de la Play Store

### Lección 1: Qué es Termux y por qué evitar la Play Store

**Resumen:** Termux es un emulador de terminal para Android que trae una distribución Linux completa sin root. La versión de Google Play lleva años sin mantenimiento y se queda atascada en paquetes antiguos: hoy la vía recomendada es F-Droid o las compilaciones de GitHub.

**Temas:**
- Qué es Termux y qué puede hacer sin permisos de root
- El problema de la versión de la Play Store (abandonada)
- Instalar desde F-Droid o GitHub releases

**Comandos:**
- pkg update
- pkg upgrade
- pkg list-installed
- termux-info

**Ejercicios:**
- Comprueba con termux-info la versión de Termux y de Android que usas.
- Confirma que pkg update y pkg upgrade terminan sin errores.

**Recursos:**
- Guía oficial de instalación (F-Droid)

### Lección 2: Acceso al almacenamiento y primeros pasos

**Resumen:** El comando termux-setup-storage concede a Termux permiso para leer y escribir en las carpetas compartidas de Android. Sin este paso, el terminal no ve fotos, descargas ni documentos.

**Temas:**
- La diferencia entre el almacenamiento interno de Termux y el de Android
- Conceder permisos con termux-setup-storage
- Localizar y verificar las carpetas compartidas

**Comandos:**
- termux-setup-storage
- ls ~/storage/shared
- termux-change-repo
- pwd

**Ejercicios:**
- Ejecuta termux-setup-storage y acepta el diálogo de permisos de Android.
- Crea una carpeta de trabajo en el almacenamiento compartido y verifícala con ls.

**Recursos:**
- Documentación de termux-setup-storage

## Módulo 2: Comandos esenciales de Linux (ls, cd, pwd, mkdir, rm)

### Lección 1: La jerarquía de directorios y el símbolo del sistema

**Resumen:** El prompt `~ $` indica que Termux está en la carpeta personal. La raíz del sistema Termux es `$PREFIX` (normalmente /data/data/com.termux/files/usr), no `/`. Saber dónde estás es el primer paso para no borrar nada por accidente.

**Temas:**
- El prompt y la carpeta personal (~)
- pwd para saber el directorio actual
- cd para cambiar de carpeta y volver con cd ~

**Comandos:**
- pwd
- echo $HOME
- cd /
- ls
- cd ~

**Ejercicios:**
- Recorre la jerarquía con cd y vuelve siempre a la carpeta personal con cd ~.
- Comprueba con pwd dónde estás en cada momento.

**Recursos:**
- Referencia de comandos de Termux

### Lección 2: listar, crear y eliminar carpetas

**Resumen:** ls lista, mkdir crea y rm elimina. Con esas tres herramientas se construye una estructura de proyectos, y con rm hay que actuar con cuidado porque no hay papelera.

**Temas:**
- Listar con ls, -l (detalle) y -a (ocultos)
- Crear carpetas con mkdir, también anidadas con -p
- Eliminar con rm y con rm -rf (usar con criterio)

**Comandos:**
- mkdir -p proyectos/cursos
- ls -la proyectos
- touch proyectos/notas.txt
- rm proyectos/notas.txt
- rm -rf proyectos

**Ejercicios:**
- Crea la estructura proyectos/cursos/python con mkdir -p.
- Lista el detalle con ls -la y elimina una prueba con rm.
- Haz una prueba con rm -rf en una carpeta que puedas borrar.

**Recursos:**
- Manual de mkdir en la wiki de Termux

### Lección 3: mover, copiar y ver archivos

**Resumen:** cp copia, mv mueve o renombra y cat muestra el contenido. Con estos comandos ya puedes organizar tus apuntes y tus scripts sin abrir un administrador de archivos.

**Temas:**
- Copiar con cp y sus variantes -r para carpetas
- Mover y renombrar con mv
- Ver archivos con cat y paginar con less

**Comandos:**
- cp notas.txt notas-copia.txt
- mv notas-copia.txt apuntes.txt
- cat apuntes.txt
- mkdir -p ~/backup && mv apuntes.txt ~/backup
- less apuntes.txt

**Ejercicios:**
- Crea un archivo, cópialo, renómbralo y muévelo a una carpeta backup.
- Abre un archivo con less y sal con q.

**Recursos:**
- Referencia de cp y mv

## Módulo 3: Gestión de archivos y permisos (chmod, chown, nano)

### Lección 1: Permisos de Linux y chmod

**Resumen:** Cada archivo tiene permisos de lectura, escritura y ejecución para su dueño, su grupo y los demás. chmod (léase "change mode") los cambia; la forma con números, como 755, es la más legible.

**Temas:**
- Leer permisos con ls -l
- Cifras: 4 lectura, 2 escritura, 1 ejecución
- chmod 755 y chmod +x en la práctica

**Comandos:**
- ls -l
- chmod 644 notas.txt
- chmod 755 script.sh
- chmod +x script.sh
- stat notas.txt

**Ejercicios:**
- Crea script.sh vacío y hazlo ejecutable con chmod +x.
- Cambia permisos a 644 y observa el cambio en ls -l.

**Recursos:**
- Guía de permisos de Linux en Termux

### Lección 2: Propietario y edición de texto con nano

**Resumen:** chown cambia el propietario de un archivo y en Termux resulta útil al operar con archivos del almacenamiento compartido. nano es el editor más amigable para empezar: abre, edita y guarda sin aprender vi.

**Temas:**
- Qué es el propietario y para qué sirve chown
- Abrir, editar y guardar con nano
- Atajos: Ctrl-O guardar y Ctrl-X salir

**Comandos:**
- pkg install nano
- nano notas.txt
- chown $(id -u):$(id -g) notas.txt
- ls -l ~/storage/shared
- file notas.txt

**Ejercicios:**
- Escribe tres líneas en nano y guárdalas con Ctrl-O y Ctrl-X.
- Comprueba qué propietario tiene un archivo recién creado con ls -l.

**Recursos:**
- Manual de nano

## Módulo 4: Instalación de entornos (Python, Node.js, Git)

### Lección 1: Python desde el gestor de paquetes pkg

**Resumen:** pkg es el gestor que empaqueta la colección de Termux. Instalar Python trae también pip, y con python -m venv creas entornos aislados para cada proyecto sin ensuciar el sistema.

**Temas:**
- El gestor pkg y sus subcomandos (install, remove, search)
- Python 3 y pip en Termux
- Entornos virtuales con venv

**Comandos:**
- pkg install python
- python --version
- pip --version
- python -m venv mi-proyecto/venv
- source mi-proyecto/venv/bin/activate

**Ejercicios:**
- Instala Python y activa un entorno virtual.
- Instala una librería dentro del entorno con pip install.

**Recursos:**
- Paquete python en la wiki de Termux

### Lección 2: Node.js y npm

**Resumen:** Node.js permite ejecutar JavaScript fuera del navegador y npm trae miles de librerías. Igual que con Python, conviene trabajar por proyecto.

**Temas:**
- Instalar Node.js y comprobar la versión
- npm init para crear un proyecto
- Instalar dependencias locales con npm install

**Comandos:**
- pkg install nodejs
- node --version
- npm --version
- mkdir app && cd app
- npm init -y
- npm install lodash

**Ejercicios:**
- Crea un proyecto con npm init -y e instala una dependencia.
- Ejecuta un archivo de prueba con node archivo.js.

**Recursos:**
- Paquete nodejs en la wiki de Termux

### Lección 3: Git y configuración de identidad

**Resumen:** Git es el control de versiones por defecto y viene listo en Termux. Lo único obligatorio antes de empezar es declarar tu nombre y correo, porque quedan grabados en cada commit.

**Temas:**
- Instalar Git y comprobar la versión
- Configurar user.name y user.email a nivel global
- Iniciar un repositorio e inspeccionarlo

**Comandos:**
- pkg install git
- git --version
- git config --global user.name "Tu Nombre"
- git config --global user.email "tu@correo.com"
- git init
- git status

**Ejercicios:**
- Configura tu identidad con tus datos reales.
- Inicia un repositorio, crea un archivo y mira git status.

**Recursos:**
- Primera configuración de Git

## Módulo 5: Tu primer script Bash (automatización básica)

### Lección 1: Estructura de un script Bash

**Resumen:** Un script es un archivo con la línea `#!/data/data/com.termux/files/usr/bin/bash` en la primera línea, comandos en las siguientes y permisos de ejecución. Crearlo en ~/bin permite ejecutarlo como un comando más.

**Temas:**
- El shebang de Termux y por qué difiere de Linux normal
- Variables y echo
- Hacer un script ejecutable

**Comandos:**
- mkdir -p ~/bin
- echo '#!/data/data/com.termux/files/usr/bin/bash' > ~/bin/mi-script.sh
- echo 'echo "Hola desde Termux"' >> ~/bin/mi-script.sh
- chmod +x ~/bin/mi-script.sh
- ~/bin/mi-script.sh

**Ejercicios:**
- Reproduce el script de ejemplo y ejecútalo.
- Añade una variable que imprima la hora con date.

**Recursos:**
- Escribir scripts en Termux

### Lección 2: Condicionales, bucles y respaldo automático

**Resumen:** Con if, for, y variables posicionales ($1, $2) pasas de mostrar mensajes a resolver tareas: comprobar si existe una carpeta, recorrer archivos y guardar respaldos con fecha.

**Temas:**
- Condicional if y comparaciones de archivo
- Bucle for sobre listas de archivos
- Respaldos con marca de fecha

**Comandos:**
- echo 'for archivo in *.sh; do echo "$archivo"; done' >> ~/bin/listar.sh
- chmod +x ~/bin/listar.sh
- mkdir -p ~/backups
- echo 'cp notas.txt ~/backups/notas-$(date +%Y%m%d).txt' >> ~/bin/respaldar.sh
- chmod +x ~/bin/respaldar.sh
- ~/bin/respaldar.sh

**Ejercicios:**
- Crea listar.sh que recorra tus scripts y los imprima.
- Ejecuta respaldar.sh dos veces en días distintos y compara los nombres con la fecha.

**Recursos:**
- Guía de Bash scripting

### Lección 3: Programar tareas con cron y termux-wake-lock

**Resumen:** termux-services activa el daemon cron para ejecutar scripts a horas fijas, y termux-wake-lock evita que Android suspenda el proceso mientras la tarea corre en segundo plano.

**Temas:**
- Trabajar en segundo plano y no morir con termux-wake-lock
- Instalar y activar servicios con termux-services
- Registrar una tarea con crontab

**Comandos:**
- pkg install termux-services
- sv-enable crond
- termux-wake-lock
- crontab -e
- printf '*/30 * * * * ~/bin/respaldar.sh\n' | crontab -
- crontab -l

**Ejercicios:**
- Programa tu respaldar.sh cada 30 minutos un rato y revísalo con crontab -l.
- Activa termux-wake-lock y comprueba que el teléfono no duerme la tarea.

**Recursos:**
- Servicios en Termux (wiki)

## Módulo 6: Control de versiones (Git y GitHub desde el celular)

### Lección 1: El ciclo de trabajo de Git: commit y log

**Resumen:** El flujo diario es ver (git status), preparar (git add) y guardar (git commit). git log registra la historia y git diff muestra qué cambió antes de confirmar.

**Temas:**
- El ciclo status > add > commit
- Mensajes de commit claros
- Leer el historial con git log

**Comandos:**
- git status
- git add .
- git commit -m "Agrega mi primer proyecto"
- git log --oneline
- git diff

**Ejercicios:**
- Crea dos commits con mensajes distintos sobre el mismo proyecto.
- Revisa el historial con git log --oneline y explícalo en voz alta.

**Recursos:**
- Conceptos básicos de Git

### Lección 2: Conectar con GitHub: clave SSH y primer push

**Resumen:** Con una clave SSH (ed25519), git habla con GitHub sin contraseña. La clave se copia en GitHub y luego el repositorio remoto se enlaza con git remote add.

**Temas:**
- Generar una clave con ssh-keygen
- Añadir la clave pública a GitHub
- Enlazar, publicar (push) y descargar (clone)

**Comandos:**
- pkg install openssh
- ssh-keygen -t ed25519 -C "tu@correo.com"
- cat ~/.ssh/id_ed25519.pub
- git remote add origin git@github.com:usuario/repositorio.git
- git branch -M main
- git push -u origin main
- git clone git@github.com:usuario/repositorio.git

**Ejercicios:**
- Genera tu clave, cópiala en GitHub y haz tu primer push.
- Clona el repositorio en otra carpeta y comprueba git log.

**Recursos:**
- Conexión de GitHub con SSH

### Lección 3: Ramas y gestión de cambios remotos

**Resumen:** Las ramas permiten trabajar sin romper la versión estable: se crea una rama, se comprueba con git branch, se publica y se fusiona con merge.

**Temas:**
- Crear y cambiar de rama
- Publicar una rama nueva
- Fusionar cambios con merge

**Comandos:**
- git branch readme
- git checkout readme
- git add . && git commit -m "Mejora el readme"
- git checkout main
- git merge readme
- git push

**Ejercicios:**
- Crea una rama, haz un cambio y fúndela en main.
- Publica el resultado y compara en GitHub.

**Recursos:**
- Flujo de trabajo con ramas

## Módulo 7: Conexiones y redes (SSH, ping, curl)

### Lección 1: SSH cliente: conectarte a otro equipo

**Resumen:** ssh abre una sesión remota segura. Con la clave que ya generaste puede funcionar sin contraseña añadiéndola a las autorizadas del equipo remoto con ssh-copy-id.

**Temas:**
- Conexión básica con ssh usuario@host
- Añadir tu clave para entrar sin contraseña
- Trabajar dentro de la sesión remota

**Comandos:**
- pkg install openssh
- ssh usuario@192.168.1.10
- ssh-copy-id usuario@192.168.1.10
- ssh -p 8022 usuario@servidor.com
- exit

**Ejercicios:**
- Conecta a un equipo de prueba y revisa pwd en la sesión remota.
- Configura la autenticación por clave con ssh-copy-id.

**Recursos:**
- Manual de OpenSSH

### Lección 2: Diagnosticar la red con ping y curl

**Resumen:** ping comprueba si un host responde midiendo latencia, y curl hace peticiones HTTP. El trío ping, curl -I y curl -v da una imagen de si el problema es la red o el servidor.

**Temas:**
- Medir la conectividad con ping -c
- Ver cabeceras HTTP con curl -I
- Depurar con curl -v y --max-time

**Comandos:**
- ping -c 4 1.1.1.1
- pkg install curl
- curl -I https://example.com
- curl -v --max-time 10 https://api.telegram.org
- curl -s https://api.github.com/repos/termux/termux-packages

**Ejercicios:**
- Diagnostica tu conexión haciendo ping a 1.1.1.1.
- Compara la salida de curl -I frente a curl -v para entender los tiempos.

**Recursos:**
- Manual de curl

### Lección 3: El servidor SSH de Termux (sshd)

**Resumen:** Termux puede servir como servidor: con sshd cualquiera con tu IP y contraseña se conecta a tu teléfono. Se levanta bajo demanda y se detiene cuando ya no se necesita.

**Temas:**
- Arrancar el daemon con sshd
- Conocer tu IP local con ifconfig o ip addr
- Detener el servicio con pkill sshd

**Comandos:**
- pkg install openssh
- sshd
- ip addr
- whoami
- pkill sshd

**Ejercicios:**
- Levanta sshd, localiza tu IP y conéctate desde otro dispositivo.
- Termina la sesión del servidor con pkill sshd.

**Recursos:**
- OpenSSH en Termux (wiki)

## Módulo 8: Proyecto final (crear y desplegar un Bot de Telegram)

### Lección 1: Obtener el token y preparar el entorno

**Resumen:** Los bots de Telegram se crean con BotFather, que entrega un token de API. En Termux se prepara el entorno: carpeta del proyecto, entorno virtual y dependencias con pip.

**Temas:**
- Crear el bot con BotFather y anotar el token
- Entorno virtual aislado para el proyecto
- Instalar la librería python-telegram-bot

**Comandos:**
- pkg install python
- mkdir -p ~/telebot
- cd ~/telebot
- python -m venv venv
- source venv/bin/activate
- pip install python-telegram-bot

**Ejercicios:**
- Crea tu bot en BotFather y guarda el token en un lugar seguro.
- Deja el entorno virtual con la librería instalada.

**Recursos:**
- Crear bots con BotFather

### Lección 2: Escribir el bot con nano

**Resumen:** El bot escucha mensajes y responde. El script pide el token por variable de entorno, define un manejador de /start y otro de texto libre, y arranca con polling.

**Temas:**
- Estructura de un bot con python-telegram-bot
- Leer el token desde el entorno y no desde el código
- Probar el bot en Telegram

**Comandos:**
- export TELEGRAM_TOKEN="1200000000:AA-tu-token-real"
- echo $TELEGRAM_TOKEN
- nano bot.py
- python bot.py
- python -m py_compile bot.py

**Ejercicios:**
- Completa bot.py con los manejadores /start y /ayuda.
- Ejecuta python bot.py y escribe a tu bot desde el teléfono.

**Recursos:**
- Documentación de python-telegram-bot

### Lección 3: Desplegarlo en segundo plano y mantenerlo vivo

**Resumen:** Un bot que se apaga cuando cierras la terminal no sirve de nada. nohup lo lanza en segundo plano ignorando señales, y termux-wake-lock impide que Android lo suspenda.

**Temas:**
- Lanzar en segundo plano con nohup y el operador &
- Impedir el suspenso de Android con termux-wake-lock
- Ver los registros y detener el proceso

**Comandos:**
- pkg install termux-api
- termux-wake-lock
- nohup python bot.py > bot.log 2>&1 &
- tail -f bot.log
- ps aux | grep bot.py
- kill $(pgrep -f bot.py)

**Ejercicios:**
- Despliega tu bot con nohup y verifica que responde.
- Comprueba con tail -f que registra cada mensaje y deténlo al terminar.

**Recursos:**
- Ejecutar procesos en segundo plano en Termux