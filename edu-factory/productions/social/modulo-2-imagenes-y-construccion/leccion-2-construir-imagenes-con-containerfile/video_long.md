# Video largo (Facebook / YouTube) — Lección 2

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 2. Imágenes y construcción
**Lección:** 2. Construir imágenes con Containerfile
**Duración estimada:** 3-8 minutos
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Estructura de un Containerfile: FROM, RUN, COPY, CMD» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (Construir imágenes con Containerfile) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: desarrolladores y administradores de sistemas que quieren usar contenedores en Linux suelen bloquearse con Estructura de un Containerfile: FROM, RUN, COPY, CMD porque falta el orden de pasos. El Containerfile es el mismo formato que el Dockerfile y se construye con podman build sin demonio. Cada instrucción genera una capa, de modo que el orden de las instrucciones afecta directamente la velocidad de reconstrucción. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Estructura de un Containerfile: FROM, RUN, COPY, CMD

Explica «Estructura de un Containerfile: FROM, RUN, COPY, CMD» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Construcción con podman build y contexto de directorio

Explica «Construcción con podman build y contexto de directorio» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Etiquetado de la imagen construida

Explica «Etiquetado de la imagen construida» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

Tema extra (si el tiempo lo permite): Ejecución y verificación de la imagen resultante.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
mkdir -p /tmp/podman-curso && cd /tmp/podman-curso
```

**Paso 2.** Ejecuta y muestra:

```
printf 'FROM docker.io/library/alpine:latest\nRUN echo "construido en Fedora" > /mensaje.txt\nCMD ["cat","/mensaje.txt"]\n' > Containerfile
```

**Paso 3.** Ejecuta y muestra:

```
cat Containerfile
```

**Paso 4.** Ejecuta y muestra:

```
podman build -t hola-podman .
```

**Paso 5.** Ejecuta y muestra:

```
podman run --rm hola-podman
```

**Paso 6.** Ejecuta y muestra:

```
podman images 'localhost/*'
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Estructura de un Containerfile: FROM, RUN, COPY, CMD».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01), nivel intermedio, duración 2 semanas. El módulo 2 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
