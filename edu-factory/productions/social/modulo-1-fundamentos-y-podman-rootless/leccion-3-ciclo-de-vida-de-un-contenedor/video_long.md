# Video largo (Facebook / YouTube) — Lección 3

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 1. Fundamentos y Podman rootless
**Lección:** 3. Ciclo de vida de un contenedor
**Duración estimada:** 3-8 minutos
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Ejecución en primer plano y en segundo plano (-d)» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (Ciclo de vida de un contenedor) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: desarrolladores y administradores de sistemas que quieren usar contenedores en Linux suelen bloquearse con Ejecución en primer plano y en segundo plano (-d) porque falta el orden de pasos. Un contenedor pasa por estados bien definidos: se crea, arranca, ejecuta, se detiene y se elimina. Dominar ese ciclo con run, ps, logs, exec, stop y rm es la base de toda operación diaria. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Ejecución en primer plano y en segundo plano (-d)

Explica «Ejecución en primer plano y en segundo plano (-d)» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Nombres propios, publicación de puertos y reinicio automático

Explica «Nombres propios, publicación de puertos y reinicio automático» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Lectura de registros con podman logs

Explica «Lectura de registros con podman logs» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

Tema extra (si el tiempo lo permite): Entrar en un contenedor en marcha con podman exec, Detener y eliminar sin dejar residuos.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
podman run -d --name web -p 8080:80 docker.io/library/nginx:alpine
```

**Paso 2.** Ejecuta y muestra:

```
podman ps
```

**Paso 3.** Ejecuta y muestra:

```
podman logs web
```

**Paso 4.** Ejecuta y muestra:

```
podman port web
```

**Paso 5.** Ejecuta y muestra:

```
podman exec web hostname
```

**Paso 6.** Ejecuta y muestra:

```
podman stop web
```

**Paso 7.** Ejecuta y muestra:

```
podman rm web
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Ejecución en primer plano y en segundo plano (-d)».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01), nivel intermedio, duración 2 semanas. El módulo 1 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
