# Temario — Podman en Fedora: contenedores sin Docker

- **Identificador:** PODMAN-FEDORA-01
- **Nivel:** intermedio
- **Duración:** 2 semanas
- **Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux

## Objetivos

- Comprender la arquitectura sin daemon de Podman y su modelo rootless.
- Instalar, verificar y diagnosticar Podman en Fedora.
- Ejecutar, inspeccionar y administrar el ciclo de vida de los contenedores.
- Construir imágenes propias con Containerfile y distribuirlas por registros.
- Gestionar persistencia con volúmenes y agrupar servicios con pods.
- Convertir contenedores en servicios de usuario con systemd y Quadlet.
- Exponer servicios de forma segura con firewalld.
- Migrar flujos de trabajo de Docker a Podman sin fricción.

## Estructura

### Módulo 1: Fundamentos y Podman rootless

1. Podman frente a Docker: el contenedor sin daemon — Podman ejecuta contenedores como procesos hijos del usuario, sin un demonio central en segundo plano. Esa diferencia reduce la superficie de ataque y elimina el grupo privilegiado que Docker necesita, a la vez que mantiene una interfaz de línea de comandos casi idéntica.
2. Instalación y verificación en Fedora — Fedora incluye Podman en sus repositorios, así que la instalación es una sola transacción de DNF. Tras instalarlo conviene verificar la versión, el backend de almacenamiento y que el entorno rootless esté operativo en la sesión del usuario.
3. Ciclo de vida de un contenedor — Un contenedor pasa por estados bien definidos: se crea, arranca, ejecuta, se detiene y se elimina. Dominar ese ciclo con run, ps, logs, exec, stop y rm es la base de toda operación diaria.

### Módulo 2: Imágenes y construcción

1. Buscar, descargar y gestionar imágenes — Las imágenes son plantillas de solo lectura que Podman descarga de registros como Docker Hub o Quay. Antes de usarlas conviene buscarlas, inspeccionar su origen y entender las capas que las componen.
2. Construir imágenes con Containerfile — El Containerfile es el mismo formato que el Dockerfile y se construye con podman build sin demonio. Cada instrucción genera una capa, de modo que el orden de las instrucciones afecta directamente la velocidad de reconstrucción.
3. Registros, etiquetas y distribución — Una imagen se identifica por su repositorio, su etiqueta y su digest. Para compartirla se etiqueta con el nombre del registro y se sube con podman push tras autenticarse, mientras skopeo permite inspeccionar imágenes remotas sin descargarlas.

### Módulo 3: Almacenamiento, redes y pods

1. Volúmenes y persistencia de datos — El sistema de archivos de un contenedor es efímero: al eliminarlo se pierde su contenido. Los volúmenes de Podman guardan datos fuera del contenedor y sobreviven a su borrado, lo que permite separar el estado de la aplicación de su imagen.
2. Redes y publicación de puertos — Podman crea una red por defecto y permite definir redes propias para aislar servicios. Los contenedores de una misma red se resuelven por nombre, y los puertos se publican hacia el host con -p indicando puerto_host:puerto_contenedor.
3. Pods: varios contenedores como uno solo — Un pod es un grupo de contenedores que comparten red, namespace y puertos, igual que en Kubernetes. Es la forma natural de juntar una aplicación con su base de datos o su servidor de caché sin publicar puertos internos.

### Módulo 4: Operación en producción

1. Contenedores como servicios con systemd y Quadlet — Quadlet convierte un archivo .container en una unidad de systemd, de modo que Podman arranca, detiene y reinicia el contenedor junto con la sesión del usuario. Es la forma recomendada hoy, en lugar del antiguo podman generate systemd.
2. Firewall y exposición segura de servicios — Publicar un puerto en Podman no siempre basta: firewalld puede bloquear el acceso desde la red. Conocer las zonas, los servicios y los puertos abiertos permite exponer solo lo necesario y cerrar todo lo demás.
3. Migración desde Docker y mantenimiento — Podman acepta casi todos los comandos de Docker, así que migrar suele empezar por un alias. Además conviene conocer las herramientas de mantenimiento: uso de disco, limpieza de imágenes y contenedores huérfanos, y el registro de eventos para diagnosticar problemas.
