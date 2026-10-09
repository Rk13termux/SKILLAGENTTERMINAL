# Video largo (Facebook / YouTube) — Lección 1

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 3. Almacenamiento, redes y pods
**Lección:** 1. Volúmenes y persistencia de datos
**Duración estimada:** 3-8 minutos
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Diferencia entre capa de escritura, bind mount y volumen gestionado» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (Volúmenes y persistencia de datos) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: desarrolladores y administradores de sistemas que quieren usar contenedores en Linux suelen bloquearse con Diferencia entre capa de escritura, bind mount y volumen gestionado porque falta el orden de pasos. El sistema de archivos de un contenedor es efímero: al eliminarlo se pierde su contenido. Los volúmenes de Podman guardan datos fuera del contenedor y sobreviven a su borrado, lo que permite separar el estado de la aplicación de su imagen. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Diferencia entre capa de escritura, bind mount y volumen gestionado

Explica «Diferencia entre capa de escritura, bind mount y volumen gestionado» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Creación, listado e inspección de volúmenes

Explica «Creación, listado e inspección de volúmenes» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Montaje de un volumen con -v en podman run

Explica «Montaje de un volumen con -v en podman run» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

Tema extra (si el tiempo lo permite): Punto de montaje real en el host y permisos rootless.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
podman volume create datos-web
```

**Paso 2.** Ejecuta y muestra:

```
podman volume ls
```

**Paso 3.** Ejecuta y muestra:

```
podman volume inspect datos-web --format '{{.Mountpoint}}'
```

**Paso 4.** Ejecuta y muestra:

```
podman run --rm -v datos-web:/data docker.io/library/alpine:latest sh -c 'echo hola > /data/saludo.txt'
```

**Paso 5.** Ejecuta y muestra:

```
podman run --rm -v datos-web:/data docker.io/library/alpine:latest cat /data/saludo.txt
```

**Paso 6.** Ejecuta y muestra:

```
podman volume rm datos-web
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Diferencia entre capa de escritura, bind mount y volumen gestionado».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01), nivel intermedio, duración 2 semanas. El módulo 3 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
