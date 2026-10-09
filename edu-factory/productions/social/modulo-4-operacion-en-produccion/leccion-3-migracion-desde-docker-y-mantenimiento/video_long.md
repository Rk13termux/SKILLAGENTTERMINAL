# Video largo (Facebook / YouTube) — Lección 3

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 4. Operación en producción
**Lección:** 3. Migración desde Docker y mantenimiento
**Duración estimada:** 3-8 minutos
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Alias docker=podman y variables de entorno compatibles» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (Migración desde Docker y mantenimiento) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: desarrolladores y administradores de sistemas que quieren usar contenedores en Linux suelen bloquearse con Alias docker=podman y variables de entorno compatibles porque falta el orden de pasos. Podman acepta casi todos los comandos de Docker, así que migrar suele empezar por un alias. Además conviene conocer las herramientas de mantenimiento: uso de disco, limpieza de imágenes y contenedores huérfanos, y el registro de eventos para diagnosticar problemas. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Alias docker=podman y variables de entorno compatibles

Explica «Alias docker=podman y variables de entorno compatibles» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Consumo de disco con podman system df

Explica «Consumo de disco con podman system df» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Limpieza controlada de contenedores, imágenes y volúmenes

Explica «Limpieza controlada de contenedores, imágenes y volúmenes» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

Tema extra (si el tiempo lo permite): Diagnóstico con podman events y revisión de la raíz de almacenamiento.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
podman --version
```

**Paso 2.** Ejecuta y muestra:

```
podman system df
```

**Paso 3.** Ejecuta y muestra:

```
podman images
```

**Paso 4.** Ejecuta y muestra:

```
podman ps -a
```

**Paso 5.** Ejecuta y muestra:

```
podman info --format '{{.Store.GraphRoot}}'
```

**Paso 6.** Ejecuta y muestra:

```
podman events --help | head -n 3
```

**Paso 7.** Ejecuta y muestra:

```
podman system connection ls
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Alias docker=podman y variables de entorno compatibles».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01), nivel intermedio, duración 2 semanas. El módulo 4 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
