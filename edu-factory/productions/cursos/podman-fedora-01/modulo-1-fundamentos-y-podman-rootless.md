# Módulo 1: Fundamentos y Podman rootless

Curso: Podman en Fedora: contenedores sin Docker · Nivel: intermedio

### Lección 1: Podman frente a Docker: el contenedor sin daemon

Podman ejecuta contenedores como procesos hijos del usuario, sin un demonio central en segundo plano. Esa diferencia reduce la superficie de ataque y elimina el grupo privilegiado que Docker necesita, a la vez que mantiene una interfaz de línea de comandos casi idéntica.

**Temas cubiertos**

- Modelo fork-exec frente al demonio dockerd
- Contenedores rootless: sin privilegios y sin grupo docker
- Compatibilidad de la CLI con los comandos de Docker
- El socket opcional podman.socket y cuándo conviene activarlo

**Ejercicios prácticos**

- Compara la salida de podman info con la de docker info y anota qué campos no existen en Podman.
- Ejecuta podman sin sudo y explica por qué no necesitas pertenecer a ningún grupo especial.

**Recursos**

- Documentación oficial de Podman (podman.io)
- Blog de Red Hat: Podman y la arquitectura sin daemon

### Lección 2: Instalación y verificación en Fedora

Fedora incluye Podman en sus repositorios, así que la instalación es una sola transacción de DNF. Tras instalarlo conviene verificar la versión, el backend de almacenamiento y que el entorno rootless esté operativo en la sesión del usuario.

**Temas cubiertos**

- Paquetes podman, buildah y skopeo en Fedora
- Verificación de versión y del cgroup v2 en modo rootless
- Actualizaciones con dnf y reinicio de la sesión de usuario
- Diagnóstico rápido con podman info

**Ejercicios prácticos**

- Instala el paquete con sudo dnf install -y podman y confirma con rpm -q que quedó registrado.
- Ejecuta un contenedor Alpine que imprima /etc/os-release y explica qué imagen se descargó.

**Recursos**

- Fedora Docs: Podman
- Página de manual podman-info

### Lección 3: Ciclo de vida de un contenedor

Un contenedor pasa por estados bien definidos: se crea, arranca, ejecuta, se detiene y se elimina. Dominar ese ciclo con run, ps, logs, exec, stop y rm es la base de toda operación diaria.

**Temas cubiertos**

- Ejecución en primer plano y en segundo plano (-d)
- Nombres propios, publicación de puertos y reinicio automático
- Lectura de registros con podman logs
- Entrar en un contenedor en marcha con podman exec
- Detener y eliminar sin dejar residuos

**Ejercicios prácticos**

- Levanta un nginx en el puerto 8080 y compruébalo con curl -I http://localhost:8080.
- Detén el contenedor, elimínalo y verifica con podman ps -a que ya no existe.

**Recursos**

- Página de manual podman-run
- Página de manual podman-exec
