# Módulo 2: Imágenes y construcción

Curso: Podman en Fedora: contenedores sin Docker · Nivel: intermedio

### Lección 1: Buscar, descargar y gestionar imágenes

Las imágenes son plantillas de solo lectura que Podman descarga de registros como Docker Hub o Quay. Antes de usarlas conviene buscarlas, inspeccionar su origen y entender las capas que las componen.

**Temas cubiertos**

- Búsqueda en registros con podman search
- Descarga explícita con podman pull y nombres completos de imagen
- Listado e inspección con podman images, inspect y history
- Capas, digests y por qué conviene fijar etiquetas

**Ejercicios prácticos**

- Inspecciona la imagen Alpine y localiza su digest con podman inspect.
- Descarga otra etiqueta de Alpine y compara el tamaño entre ambas con podman images.

**Recursos**

- Docker Hub oficial
- Página de manual podman-pull

### Lección 2: Construir imágenes con Containerfile

El Containerfile es el mismo formato que el Dockerfile y se construye con podman build sin demonio. Cada instrucción genera una capa, de modo que el orden de las instrucciones afecta directamente la velocidad de reconstrucción.

**Temas cubiertos**

- Estructura de un Containerfile: FROM, RUN, COPY, CMD
- Construcción con podman build y contexto de directorio
- Etiquetado de la imagen construida
- Ejecución y verificación de la imagen resultante

**Ejercicios prácticos**

- Añade una instrucción COPY a tu Containerfile y reconstruye la imagen.
- Cambia el CMD para que muestre la fecha con date y verifica el resultado.

**Recursos**

- Referencia de Containerfile (formato Dockerfile)
- Página de manual podman-build

### Lección 3: Registros, etiquetas y distribución

Una imagen se identifica por su repositorio, su etiqueta y su digest. Para compartirla se etiqueta con el nombre del registro y se sube con podman push tras autenticarse, mientras skopeo permite inspeccionar imágenes remotas sin descargarlas.

**Temas cubiertos**

- Anatomía de un nombre de imagen: registro, repositorio, etiqueta, digest
- podman tag para preparar una imagen antes de publicarla
- podman login y podman push hacia un registro
- Inspección remota con skopeo inspect

**Ejercicios prácticos**

- Crea una cuenta en Quay.io y publica tu imagen con podman push.
- Explica la diferencia entre etiqueta y digest y cuándo conviene usar cada uno.

**Recursos**

- Quay.io
- Página de manual skopeo-inspect
