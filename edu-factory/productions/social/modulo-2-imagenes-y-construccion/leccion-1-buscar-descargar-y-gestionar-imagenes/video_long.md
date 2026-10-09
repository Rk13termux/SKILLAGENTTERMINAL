# Video largo (Facebook / YouTube) — Lección 1

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 2. Imágenes y construcción
**Lección:** 1. Buscar, descargar y gestionar imágenes
**Duración estimada:** 3-8 minutos
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Búsqueda en registros con podman search» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (Buscar, descargar y gestionar imágenes) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: desarrolladores y administradores de sistemas que quieren usar contenedores en Linux suelen bloquearse con Búsqueda en registros con podman search porque falta el orden de pasos. Las imágenes son plantillas de solo lectura que Podman descarga de registros como Docker Hub o Quay. Antes de usarlas conviene buscarlas, inspeccionar su origen y entender las capas que las componen. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Búsqueda en registros con podman search

Explica «Búsqueda en registros con podman search» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Descarga explícita con podman pull y nombres completos de imagen

Explica «Descarga explícita con podman pull y nombres completos de imagen» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Listado e inspección con podman images, inspect y history

Explica «Listado e inspección con podman images, inspect y history» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

Tema extra (si el tiempo lo permite): Capas, digests y por qué conviene fijar etiquetas.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
podman search docker.io/library/alpine --limit 3
```

**Paso 2.** Ejecuta y muestra:

```
podman pull docker.io/library/alpine:latest
```

**Paso 3.** Ejecuta y muestra:

```
podman images
```

**Paso 4.** Ejecuta y muestra:

```
podman history docker.io/library/alpine:latest
```

**Paso 5.** Ejecuta y muestra:

```
podman image tree docker.io/library/alpine:latest
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Búsqueda en registros con podman search».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01), nivel intermedio, duración 2 semanas. El módulo 2 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
