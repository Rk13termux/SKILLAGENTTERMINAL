# Módulo 3: Almacenamiento, redes y pods

Curso: Podman en Fedora: contenedores sin Docker · Nivel: intermedio

### Lección 1: Volúmenes y persistencia de datos

El sistema de archivos de un contenedor es efímero: al eliminarlo se pierde su contenido. Los volúmenes de Podman guardan datos fuera del contenedor y sobreviven a su borrado, lo que permite separar el estado de la aplicación de su imagen.

**Temas cubiertos**

- Diferencia entre capa de escritura, bind mount y volumen gestionado
- Creación, listado e inspección de volúmenes
- Montaje de un volumen con -v en podman run
- Punto de montaje real en el host y permisos rootless

**Ejercicios prácticos**

- Escribe un archivo desde un contenedor y léelo desde otro distinto usando el mismo volumen.
- Compara el contenido de podman volume inspect con la ruta real que muestra en el host.

**Recursos**

- Página de manual podman-volume
- Documentación sobre almacenamiento de contenedores

### Lección 2: Redes y publicación de puertos

Podman crea una red por defecto y permite definir redes propias para aislar servicios. Los contenedores de una misma red se resuelven por nombre, y los puertos se publican hacia el host con -p indicando puerto_host:puerto_contenedor.

**Temas cubiertos**

- Red por defecto y resolución DNS interna entre contenedores
- Creación e inspección de redes personalizadas
- Publicación de puertos con -p y diferencias entre modos
- Cómo el firewall del host afecta el acceso a los puertos publicados

**Ejercicios prácticos**

- Crea dos contenedores en la misma red y haz que uno resuelva al otro por su nombre con ping.
- Publica un servicio en el puerto 9090 y compruébalo con curl desde el host.

**Recursos**

- Página de manual podman-network
- Documentación de redes CNI y Netavark

### Lección 3: Pods: varios contenedores como uno solo

Un pod es un grupo de contenedores que comparten red, namespace y puertos, igual que en Kubernetes. Es la forma natural de juntar una aplicación con su base de datos o su servidor de caché sin publicar puertos internos.

**Temas cubiertos**

- Qué comparte un pod: red, IP, espacio de nombres y puertos
- Creación de pods con podman pod create
- Añadir contenedores a un pod con --pod
- Inspección, parada y eliminación atómica del pod

**Ejercicios prácticos**

- Añade un segundo contenedor al pod y comprueba que comparte la dirección IP con el primero.
- Detén el pod completo y explica por qué no hace falta detener cada contenedor por separado.

**Recursos**

- Página de manual podman-pod
- Documentación de pods y Kubernetes
