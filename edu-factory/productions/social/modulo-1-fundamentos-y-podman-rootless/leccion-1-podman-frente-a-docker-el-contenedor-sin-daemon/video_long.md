# Video largo (Facebook / YouTube) — Lección 1

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 1. Fundamentos y Podman rootless
**Lección:** 1. Podman frente a Docker: el contenedor sin daemon
**Duración estimada:** 3-8 minutos
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Modelo fork-exec frente al demonio dockerd» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (Podman frente a Docker: el contenedor sin daemon) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: desarrolladores y administradores de sistemas que quieren usar contenedores en Linux suelen bloquearse con Modelo fork-exec frente al demonio dockerd porque falta el orden de pasos. Podman ejecuta contenedores como procesos hijos del usuario, sin un demonio central en segundo plano. Esa diferencia reduce la superficie de ataque y elimina el grupo privilegiado que Docker necesita, a la vez que mantiene una interfaz de línea de comandos casi idéntica. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Modelo fork-exec frente al demonio dockerd

Explica «Modelo fork-exec frente al demonio dockerd» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Contenedores rootless: sin privilegios y sin grupo docker

Explica «Contenedores rootless: sin privilegios y sin grupo docker» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Compatibilidad de la CLI con los comandos de Docker

Explica «Compatibilidad de la CLI con los comandos de Docker» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

Tema extra (si el tiempo lo permite): El socket opcional podman.socket y cuándo conviene activarlo.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
podman --version
```

**Paso 2.** Ejecuta y muestra:

```
podman info --format '{{.Host.OS}} {{.Host.Arch}}'
```

**Paso 3.** Ejecuta y muestra:

```
podman info --format '{{.Host.Security.Rootless}}'
```

**Paso 4.** Ejecuta y muestra:

```
echo "UID: $(id -u) - usuario: $USER"
```

**Paso 5.** Ejecuta y muestra:

```
podman ps -a
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Modelo fork-exec frente al demonio dockerd».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01), nivel intermedio, duración 2 semanas. El módulo 1 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
