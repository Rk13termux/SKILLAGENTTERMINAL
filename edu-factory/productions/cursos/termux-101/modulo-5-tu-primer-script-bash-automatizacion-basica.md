# Módulo 5: Tu primer script Bash (automatización básica)

Curso: Termux desde Cero: Domina la terminal en tu Android · Nivel: principiante a intermedio

### Lección 1: Estructura de un script Bash

Un script es un archivo con la línea `#!/data/data/com.termux/files/usr/bin/bash` en la primera línea, comandos en las siguientes y permisos de ejecución. Crearlo en ~/bin permite ejecutarlo como un comando más.

**Temas cubiertos**

- El shebang de Termux y por qué difiere de Linux normal
- Variables y echo
- Hacer un script ejecutable

**Ejercicios prácticos**

- Reproduce el script de ejemplo y ejecútalo.
- Añade una variable que imprima la hora con date.

**Recursos**

- Escribir scripts en Termux

### Lección 2: Condicionales, bucles y respaldo automático

Con if, for, y variables posicionales ($1, $2) pasas de mostrar mensajes a resolver tareas: comprobar si existe una carpeta, recorrer archivos y guardar respaldos con fecha.

**Temas cubiertos**

- Condicional if y comparaciones de archivo
- Bucle for sobre listas de archivos
- Respaldos con marca de fecha

**Ejercicios prácticos**

- Crea listar.sh que recorra tus scripts y los imprima.
- Ejecuta respaldar.sh dos veces en días distintos y compara los nombres con la fecha.

**Recursos**

- Guía de Bash scripting

### Lección 3: Programar tareas con cron y termux-wake-lock

termux-services activa el daemon cron para ejecutar scripts a horas fijas, y termux-wake-lock evita que Android suspenda el proceso mientras la tarea corre en segundo plano.

**Temas cubiertos**

- Trabajar en segundo plano y no morir con termux-wake-lock
- Instalar y activar servicios con termux-services
- Registrar una tarea con crontab

**Ejercicios prácticos**

- Programa tu respaldar.sh cada 30 minutos un rato y revísalo con crontab -l.
- Activa termux-wake-lock y comprueba que el teléfono no duerme la tarea.

**Recursos**

- Servicios en Termux (wiki)
