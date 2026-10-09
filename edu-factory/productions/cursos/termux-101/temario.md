# Temario — Termux desde Cero: Domina la terminal en tu Android

- **Identificador:** TERMUX-101
- **Nivel:** principiante a intermedio
- **Duración:** 4 semanas
- **Audiencia:** principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular

## Objetivos

- Configurar Termux de forma segura y distinguir la versión correcta de la Play Store.
- Dominar los comandos esenciales de Linux para moverse por el sistema de archivos.
- Gestionar archivos, permisos y editores de texto desde la terminal.
- Instalar y usar entornos de desarrollo reales: Python, Node.js y Git.
- Escribir y automatizar tareas con scripts Bash.
- Usar Git y GitHub para guardar y compartir código desde el celular.
- Conectarte a otros equipos por SSH y diagnosticar redes con ping y curl.
- Combinar todo en un proyecto final: un bot de Telegram desplegado desde Termux.

## Estructura

### Módulo 1: Configuración inicial y mitos de la Play Store

1. Qué es Termux y por qué evitar la Play Store — Termux es un emulador de terminal para Android que trae una distribución Linux completa sin root. La versión de Google Play lleva años sin mantenimiento y se queda atascada en paquetes antiguos: hoy la vía recomendada es F-Droid o las compilaciones de GitHub.
2. Acceso al almacenamiento y primeros pasos — El comando termux-setup-storage concede a Termux permiso para leer y escribir en las carpetas compartidas de Android. Sin este paso, el terminal no ve fotos, descargas ni documentos.

### Módulo 2: Comandos esenciales de Linux (ls, cd, pwd, mkdir, rm)

1. La jerarquía de directorios y el símbolo del sistema — El prompt `~ $` indica que Termux está en la carpeta personal. La raíz del sistema Termux es `$PREFIX` (normalmente /data/data/com.termux/files/usr), no `/`. Saber dónde estás es el primer paso para no borrar nada por accidente.
2. listar, crear y eliminar carpetas — ls lista, mkdir crea y rm elimina. Con esas tres herramientas se construye una estructura de proyectos, y con rm hay que actuar con cuidado porque no hay papelera.
3. mover, copiar y ver archivos — cp copia, mv mueve o renombra y cat muestra el contenido. Con estos comandos ya puedes organizar tus apuntes y tus scripts sin abrir un administrador de archivos.

### Módulo 3: Gestión de archivos y permisos (chmod, chown, nano)

1. Permisos de Linux y chmod — Cada archivo tiene permisos de lectura, escritura y ejecución para su dueño, su grupo y los demás. chmod (léase "change mode") los cambia; la forma con números, como 755, es la más legible.
2. Propietario y edición de texto con nano — chown cambia el propietario de un archivo y en Termux resulta útil al operar con archivos del almacenamiento compartido. nano es el editor más amigable para empezar: abre, edita y guarda sin aprender vi.

### Módulo 4: Instalación de entornos (Python, Node.js, Git)

1. Python desde el gestor de paquetes pkg — pkg es el gestor que empaqueta la colección de Termux. Instalar Python trae también pip, y con python -m venv creas entornos aislados para cada proyecto sin ensuciar el sistema.
2. Node.js y npm — Node.js permite ejecutar JavaScript fuera del navegador y npm trae miles de librerías. Igual que con Python, conviene trabajar por proyecto.
3. Git y configuración de identidad — Git es el control de versiones por defecto y viene listo en Termux. Lo único obligatorio antes de empezar es declarar tu nombre y correo, porque quedan grabados en cada commit.

### Módulo 5: Tu primer script Bash (automatización básica)

1. Estructura de un script Bash — Un script es un archivo con la línea `#!/data/data/com.termux/files/usr/bin/bash` en la primera línea, comandos en las siguientes y permisos de ejecución. Crearlo en ~/bin permite ejecutarlo como un comando más.
2. Condicionales, bucles y respaldo automático — Con if, for, y variables posicionales ($1, $2) pasas de mostrar mensajes a resolver tareas: comprobar si existe una carpeta, recorrer archivos y guardar respaldos con fecha.
3. Programar tareas con cron y termux-wake-lock — termux-services activa el daemon cron para ejecutar scripts a horas fijas, y termux-wake-lock evita que Android suspenda el proceso mientras la tarea corre en segundo plano.

### Módulo 6: Control de versiones (Git y GitHub desde el celular)

1. El ciclo de trabajo de Git: commit y log — El flujo diario es ver (git status), preparar (git add) y guardar (git commit). git log registra la historia y git diff muestra qué cambió antes de confirmar.
2. Conectar con GitHub: clave SSH y primer push — Con una clave SSH (ed25519), git habla con GitHub sin contraseña. La clave se copia en GitHub y luego el repositorio remoto se enlaza con git remote add.
3. Ramas y gestión de cambios remotos — Las ramas permiten trabajar sin romper la versión estable: se crea una rama, se comprueba con git branch, se publica y se fusiona con merge.

### Módulo 7: Conexiones y redes (SSH, ping, curl)

1. SSH cliente: conectarte a otro equipo — ssh abre una sesión remota segura. Con la clave que ya generaste puede funcionar sin contraseña añadiéndola a las autorizadas del equipo remoto con ssh-copy-id.
2. Diagnosticar la red con ping y curl — ping comprueba si un host responde midiendo latencia, y curl hace peticiones HTTP. El trío ping, curl -I y curl -v da una imagen de si el problema es la red o el servidor.
3. El servidor SSH de Termux (sshd) — Termux puede servir como servidor: con sshd cualquiera con tu IP y contraseña se conecta a tu teléfono. Se levanta bajo demanda y se detiene cuando ya no se necesita.

### Módulo 8: Proyecto final (crear y desplegar un Bot de Telegram)

1. Obtener el token y preparar el entorno — Los bots de Telegram se crean con BotFather, que entrega un token de API. En Termux se prepara el entorno: carpeta del proyecto, entorno virtual y dependencias con pip.
2. Escribir el bot con nano — El bot escucha mensajes y responde. El script pide el token por variable de entorno, define un manejador de /start y otro de texto libre, y arranca con polling.
3. Desplegarlo en segundo plano y mantenerlo vivo — Un bot que se apaga cuando cierras la terminal no sirve de nada. nohup lo lanza en segundo plano ignorando señales, y termux-wake-lock impide que Android lo suspenda.
