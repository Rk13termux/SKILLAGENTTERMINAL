# Video largo (Facebook / YouTube) — Lección 3

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 2. Imágenes y construcción
**Lección:** 3. Registros, etiquetas y distribución
**Duración estimada:** 3-8 minutos
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Anatomía de un nombre de imagen: registro, repositorio, etiqueta, digest» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (Registros, etiquetas y distribución) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: desarrolladores y administradores de sistemas que quieren usar contenedores en Linux suelen bloquearse con Anatomía de un nombre de imagen: registro, repositorio, etiqueta, digest porque falta el orden de pasos. Una imagen se identifica por su repositorio, su etiqueta y su digest. Para compartirla se etiqueta con el nombre del registro y se sube con podman push tras autenticarse, mientras skopeo permite inspeccionar imágenes remotas sin descargarlas. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Anatomía de un nombre de imagen: registro, repositorio, etiqueta, digest

Explica «Anatomía de un nombre de imagen: registro, repositorio, etiqueta, digest» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: podman tag para preparar una imagen antes de publicarla

Explica «podman tag para preparar una imagen antes de publicarla» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: podman login y podman push hacia un registro

Explica «podman login y podman push hacia un registro» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

Tema extra (si el tiempo lo permite): Inspección remota con skopeo inspect.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
podman tag hola-podman localhost:5000/hola-podman:1.0
```

**Paso 2.** Ejecuta y muestra:

```
podman images 'localhost:5000/*'
```

**Paso 3.** Ejecuta y muestra:

```
skopeo inspect --format '{{.Digest}}' docker://docker.io/library/alpine:latest
```

**Paso 4.** Ejecuta y muestra:

```
podman login --help | head -n 3
```

**Paso 5.** Ejecuta y muestra:

```
podman push --help | head -n 3
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Anatomía de un nombre de imagen: registro, repositorio, etiqueta, digest».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01), nivel intermedio, duración 2 semanas. El módulo 2 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
