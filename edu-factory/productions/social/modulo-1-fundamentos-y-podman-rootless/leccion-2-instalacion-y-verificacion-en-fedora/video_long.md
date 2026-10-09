# Video largo (Facebook / YouTube) — Lección 2

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 1. Fundamentos y Podman rootless
**Lección:** 2. Instalación y verificación en Fedora
**Duración estimada:** 3-8 minutos
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Paquetes podman, buildah y skopeo en Fedora» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (Instalación y verificación en Fedora) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: desarrolladores y administradores de sistemas que quieren usar contenedores en Linux suelen bloquearse con Paquetes podman, buildah y skopeo en Fedora porque falta el orden de pasos. Fedora incluye Podman en sus repositorios, así que la instalación es una sola transacción de DNF. Tras instalarlo conviene verificar la versión, el backend de almacenamiento y que el entorno rootless esté operativo en la sesión del usuario. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Paquetes podman, buildah y skopeo en Fedora

Explica «Paquetes podman, buildah y skopeo en Fedora» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Verificación de versión y del cgroup v2 en modo rootless

Explica «Verificación de versión y del cgroup v2 en modo rootless» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Actualizaciones con dnf y reinicio de la sesión de usuario

Explica «Actualizaciones con dnf y reinicio de la sesión de usuario» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

Tema extra (si el tiempo lo permite): Diagnóstico rápido con podman info.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
rpm -q podman
```

**Paso 2.** Ejecuta y muestra:

```
dnf list --installed podman
```

**Paso 3.** Ejecuta y muestra:

```
podman info --format '{{.Version.Version}}'
```

**Paso 4.** Ejecuta y muestra:

```
podman run --rm docker.io/library/alpine:latest cat /etc/os-release
```

**Paso 5.** Ejecuta y muestra:

```
systemctl --user is-system-running
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Paquetes podman, buildah y skopeo en Fedora».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01), nivel intermedio, duración 2 semanas. El módulo 1 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
