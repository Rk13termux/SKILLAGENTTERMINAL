# Podman en Fedora: contenedores sin Docker

## Metadata
- id: PODMAN-FEDORA-01
- nivel: intermedio
- duracion: 2 semanas
- audiencia: desarrolladores y administradores de sistemas que quieren usar contenedores en Linux
- idioma: español
- plataforma: Fedora Linux (Podman 5.x)

## Objetivos
- Comprender la arquitectura sin daemon de Podman y su modelo rootless.
- Instalar, verificar y diagnosticar Podman en Fedora.
- Ejecutar, inspeccionar y administrar el ciclo de vida de los contenedores.
- Construir imágenes propias con Containerfile y distribuirlas por registros.
- Gestionar persistencia con volúmenes y agrupar servicios con pods.
- Convertir contenedores en servicios de usuario con systemd y Quadlet.
- Exponer servicios de forma segura con firewalld.
- Migrar flujos de trabajo de Docker a Podman sin fricción.

## Módulo 1: Fundamentos y Podman rootless

### Lección 1: Podman frente a Docker: el contenedor sin daemon

**Resumen:** Podman ejecuta contenedores como procesos hijos del usuario, sin un demonio central en segundo plano. Esa diferencia reduce la superficie de ataque y elimina el grupo privilegiado que Docker necesita, a la vez que mantiene una interfaz de línea de comandos casi idéntica.

**Temas:**
- Modelo fork-exec frente al demonio dockerd
- Contenedores rootless: sin privilegios y sin grupo docker
- Compatibilidad de la CLI con los comandos de Docker
- El socket opcional podman.socket y cuándo conviene activarlo

**Comandos:**
- podman --version
- podman info --format '{{.Host.OS}} {{.Host.Arch}}'
- podman info --format '{{.Host.Security.Rootless}}'
- echo "UID: $(id -u) - usuario: $USER"
- podman ps -a

**Ejercicios:**
- Compara la salida de podman info con la de docker info y anota qué campos no existen en Podman.
- Ejecuta podman sin sudo y explica por qué no necesitas pertenecer a ningún grupo especial.

**Recursos:**
- Documentación oficial de Podman (podman.io)
- Blog de Red Hat: Podman y la arquitectura sin daemon

### Lección 2: Instalación y verificación en Fedora

**Resumen:** Fedora incluye Podman en sus repositorios, así que la instalación es una sola transacción de DNF. Tras instalarlo conviene verificar la versión, el backend de almacenamiento y que el entorno rootless esté operativo en la sesión del usuario.

**Temas:**
- Paquetes podman, buildah y skopeo en Fedora
- Verificación de versión y del cgroup v2 en modo rootless
- Actualizaciones con dnf y reinicio de la sesión de usuario
- Diagnóstico rápido con podman info

**Comandos:**
- rpm -q podman
- dnf list --installed podman
- podman info --format '{{.Version.Version}}'
- podman run --rm docker.io/library/alpine:latest cat /etc/os-release
- systemctl --user is-system-running

**Ejercicios:**
- Instala el paquete con sudo dnf install -y podman y confirma con rpm -q que quedó registrado.
- Ejecuta un contenedor Alpine que imprima /etc/os-release y explica qué imagen se descargó.

**Recursos:**
- Fedora Docs: Podman
- Página de manual podman-info

### Lección 3: Ciclo de vida de un contenedor

**Resumen:** Un contenedor pasa por estados bien definidos: se crea, arranca, ejecuta, se detiene y se elimina. Dominar ese ciclo con run, ps, logs, exec, stop y rm es la base de toda operación diaria.

**Temas:**
- Ejecución en primer plano y en segundo plano (-d)
- Nombres propios, publicación de puertos y reinicio automático
- Lectura de registros con podman logs
- Entrar en un contenedor en marcha con podman exec
- Detener y eliminar sin dejar residuos

**Comandos:**
- podman run -d --name web -p 8080:80 docker.io/library/nginx:alpine
- podman ps
- podman logs web
- podman port web
- podman exec web hostname
- podman stop web
- podman rm web

**Ejercicios:**
- Levanta un nginx en el puerto 8080 y compruébalo con curl -I http://localhost:8080.
- Detén el contenedor, elimínalo y verifica con podman ps -a que ya no existe.

**Recursos:**
- Página de manual podman-run
- Página de manual podman-exec

## Módulo 2: Imágenes y construcción

### Lección 1: Buscar, descargar y gestionar imágenes

**Resumen:** Las imágenes son plantillas de solo lectura que Podman descarga de registros como Docker Hub o Quay. Antes de usarlas conviene buscarlas, inspeccionar su origen y entender las capas que las componen.

**Temas:**
- Búsqueda en registros con podman search
- Descarga explícita con podman pull y nombres completos de imagen
- Listado e inspección con podman images, inspect y history
- Capas, digests y por qué conviene fijar etiquetas

**Comandos:**
- podman search docker.io/library/alpine --limit 3
- podman pull docker.io/library/alpine:latest
- podman images
- podman history docker.io/library/alpine:latest
- podman image tree docker.io/library/alpine:latest

**Ejercicios:**
- Inspecciona la imagen Alpine y localiza su digest con podman inspect.
- Descarga otra etiqueta de Alpine y compara el tamaño entre ambas con podman images.

**Recursos:**
- Docker Hub oficial
- Página de manual podman-pull

### Lección 2: Construir imágenes con Containerfile

**Resumen:** El Containerfile es el mismo formato que el Dockerfile y se construye con podman build sin demonio. Cada instrucción genera una capa, de modo que el orden de las instrucciones afecta directamente la velocidad de reconstrucción.

**Temas:**
- Estructura de un Containerfile: FROM, RUN, COPY, CMD
- Construcción con podman build y contexto de directorio
- Etiquetado de la imagen construida
- Ejecución y verificación de la imagen resultante

**Comandos:**
- mkdir -p /tmp/podman-curso && cd /tmp/podman-curso
- printf 'FROM docker.io/library/alpine:latest\nRUN echo "construido en Fedora" > /mensaje.txt\nCMD ["cat","/mensaje.txt"]\n' > Containerfile
- cat Containerfile
- podman build -t hola-podman .
- podman run --rm hola-podman
- podman images 'localhost/*'

**Ejercicios:**
- Añade una instrucción COPY a tu Containerfile y reconstruye la imagen.
- Cambia el CMD para que muestre la fecha con date y verifica el resultado.

**Recursos:**
- Referencia de Containerfile (formato Dockerfile)
- Página de manual podman-build

### Lección 3: Registros, etiquetas y distribución

**Resumen:** Una imagen se identifica por su repositorio, su etiqueta y su digest. Para compartirla se etiqueta con el nombre del registro y se sube con podman push tras autenticarse, mientras skopeo permite inspeccionar imágenes remotas sin descargarlas.

**Temas:**
- Anatomía de un nombre de imagen: registro, repositorio, etiqueta, digest
- podman tag para preparar una imagen antes de publicarla
- podman login y podman push hacia un registro
- Inspección remota con skopeo inspect

**Comandos:**
- podman tag hola-podman localhost:5000/hola-podman:1.0
- podman images 'localhost:5000/*'
- skopeo inspect --format '{{.Digest}}' docker://docker.io/library/alpine:latest
- podman login --help | head -n 3
- podman push --help | head -n 3

**Ejercicios:**
- Crea una cuenta en Quay.io y publica tu imagen con podman push.
- Explica la diferencia entre etiqueta y digest y cuándo conviene usar cada uno.

**Recursos:**
- Quay.io
- Página de manual skopeo-inspect

## Módulo 3: Almacenamiento, redes y pods

### Lección 1: Volúmenes y persistencia de datos

**Resumen:** El sistema de archivos de un contenedor es efímero: al eliminarlo se pierde su contenido. Los volúmenes de Podman guardan datos fuera del contenedor y sobreviven a su borrado, lo que permite separar el estado de la aplicación de su imagen.

**Temas:**
- Diferencia entre capa de escritura, bind mount y volumen gestionado
- Creación, listado e inspección de volúmenes
- Montaje de un volumen con -v en podman run
- Punto de montaje real en el host y permisos rootless

**Comandos:**
- podman volume create datos-web
- podman volume ls
- podman volume inspect datos-web --format '{{.Mountpoint}}'
- podman run --rm -v datos-web:/data docker.io/library/alpine:latest sh -c 'echo hola > /data/saludo.txt'
- podman run --rm -v datos-web:/data docker.io/library/alpine:latest cat /data/saludo.txt
- podman volume rm datos-web

**Ejercicios:**
- Escribe un archivo desde un contenedor y léelo desde otro distinto usando el mismo volumen.
- Compara el contenido de podman volume inspect con la ruta real que muestra en el host.

**Recursos:**
- Página de manual podman-volume
- Documentación sobre almacenamiento de contenedores

### Lección 2: Redes y publicación de puertos

**Resumen:** Podman crea una red por defecto y permite definir redes propias para aislar servicios. Los contenedores de una misma red se resuelven por nombre, y los puertos se publican hacia el host con -p indicando puerto_host:puerto_contenedor.

**Temas:**
- Red por defecto y resolución DNS interna entre contenedores
- Creación e inspección de redes personalizadas
- Publicación de puertos con -p y diferencias entre modos
- Cómo el firewall del host afecta el acceso a los puertos publicados

**Comandos:**
- podman network ls
- podman network create red-curso
- podman network inspect red-curso --format '{{range .Subnets}}{{.Subnet}}{{end}}'
- podman run -d --name api --network red-curso docker.io/library/alpine:latest sleep 300
- podman inspect api --format '{{range $k,$v := .NetworkSettings.Networks}}{{$k}}{{end}}'
- podman rm -f api
- podman network rm red-curso

**Ejercicios:**
- Crea dos contenedores en la misma red y haz que uno resuelva al otro por su nombre con ping.
- Publica un servicio en el puerto 9090 y compruébalo con curl desde el host.

**Recursos:**
- Página de manual podman-network
- Documentación de redes CNI y Netavark

### Lección 3: Pods: varios contenedores como uno solo

**Resumen:** Un pod es un grupo de contenedores que comparten red, namespace y puertos, igual que en Kubernetes. Es la forma natural de juntar una aplicación con su base de datos o su servidor de caché sin publicar puertos internos.

**Temas:**
- Qué comparte un pod: red, IP, espacio de nombres y puertos
- Creación de pods con podman pod create
- Añadir contenedores a un pod con --pod
- Inspección, parada y eliminación atómica del pod

**Comandos:**
- podman pod create --name pod-web -p 8081:80
- podman pod ls
- podman run -d --pod pod-web --name pod-nginx docker.io/library/nginx:alpine
- podman ps --pod
- podman pod inspect pod-web --format '{{.Name}} {{.NumContainers}}'
- podman pod stop pod-web
- podman pod rm -f pod-web

**Ejercicios:**
- Añade un segundo contenedor al pod y comprueba que comparte la dirección IP con el primero.
- Detén el pod completo y explica por qué no hace falta detener cada contenedor por separado.

**Recursos:**
- Página de manual podman-pod
- Documentación de pods y Kubernetes

## Módulo 4: Operación en producción

### Lección 1: Contenedores como servicios con systemd y Quadlet

**Resumen:** Quadlet convierte un archivo .container en una unidad de systemd, de modo que Podman arranca, detiene y reinicia el contenedor junto con la sesión del usuario. Es la forma recomendada hoy, en lugar del antiguo podman generate systemd.

**Temas:**
- Qué es Quadlet y cómo lo integra systemd --user
- Estructura de un archivo .container en ~/.config/containers/systemd
- Recarga, arranque y estado del servicio generado
- Reinicio automático y dependencias entre unidades

**Comandos:**
- mkdir -p ~/.config/containers/systemd
- printf '[Unit]\nDescription=Nginx gestionado por Podman\n[Container]\nImage=docker.io/library/nginx:alpine\nPublishPort=8082:80\n[Install]\nWantedBy=default.target\n' > ~/.config/containers/systemd/nginx.container
- systemctl --user daemon-reload
- systemctl --user start nginx.service
- systemctl --user status nginx.service --no-pager
- curl -s -o /dev/null -w 'HTTP %{http_code}\n' http://localhost:8082
- systemctl --user stop nginx.service
- rm ~/.config/containers/systemd/nginx.container
- systemctl --user daemon-reload

**Ejercicios:**
- Añade la directiva WantedBy=default.target y habilita el servicio para que arranque con la sesión.
- Modifica la unidad para que reinicie el contenedor automáticamente y verifica con systemctl --user status.

**Recursos:**
- Documentación de Quadlet en Podman
- Página de manual systemd.container

### Lección 2: Firewall y exposición segura de servicios

**Resumen:** Publicar un puerto en Podman no siempre basta: firewalld puede bloquear el acceso desde la red. Conocer las zonas, los servicios y los puertos abiertos permite exponer solo lo necesario y cerrar todo lo demás.

**Temas:**
- Estado del firewall y zonas con firewall-cmd
- Consultar servicios y puertos ya abiertos
- Abrir y cerrar puertos de forma permanente con --permanent y --reload
- Zona public frente a interfaces concretas y buenas prácticas de exposición

**Comandos:**
- firewall-cmd --state
- firewall-cmd --get-default-zone
- firewall-cmd --list-services
- firewall-cmd --list-ports
- firewall-cmd --list-all
- ss -tln

**Ejercicios:**
- Abre temporalmente el puerto 8080 con sudo firewall-cmd --add-port=8080/tcp y ciérralo después.
- Hazlo permanente con --permanent, recarga con --reload y confirma el cambio con --list-ports.

**Recursos:**
- Fedora Docs: firewalld
- Página de manual firewall-cmd

### Lección 3: Migración desde Docker y mantenimiento

**Resumen:** Podman acepta casi todos los comandos de Docker, así que migrar suele empezar por un alias. Además conviene conocer las herramientas de mantenimiento: uso de disco, limpieza de imágenes y contenedores huérfanos, y el registro de eventos para diagnosticar problemas.

**Temas:**
- Alias docker=podman y variables de entorno compatibles
- Consumo de disco con podman system df
- Limpieza controlada de contenedores, imágenes y volúmenes
- Diagnóstico con podman events y revisión de la raíz de almacenamiento

**Comandos:**
- podman --version
- podman system df
- podman images
- podman ps -a
- podman info --format '{{.Store.GraphRoot}}'
- podman events --help | head -n 3
- podman system connection ls

**Ejercicios:**
- Crea el alias docker=podman en tu shell y ejecuta docker ps para comprobar la compatibilidad.
- Revisa el uso de disco, elimina una imagen sin usar y explica cómo liberar espacio de forma segura.

**Recursos:**
- Guía de migración de Docker a Podman
- Página de manual podman-system
