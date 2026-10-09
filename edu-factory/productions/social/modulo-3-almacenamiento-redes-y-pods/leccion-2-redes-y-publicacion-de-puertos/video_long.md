# Video largo (Facebook / YouTube) — Lección 2

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 3. Almacenamiento, redes y pods
**Lección:** 2. Redes y publicación de puertos
**Duración estimada:** 3-8 minutos
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Red por defecto y resolución DNS interna entre contenedores» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (Redes y publicación de puertos) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: desarrolladores y administradores de sistemas que quieren usar contenedores en Linux suelen bloquearse con Red por defecto y resolución DNS interna entre contenedores porque falta el orden de pasos. Podman crea una red por defecto y permite definir redes propias para aislar servicios. Los contenedores de una misma red se resuelven por nombre, y los puertos se publican hacia el host con -p indicando puerto_host:puerto_contenedor. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Red por defecto y resolución DNS interna entre contenedores

Explica «Red por defecto y resolución DNS interna entre contenedores» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Creación e inspección de redes personalizadas

Explica «Creación e inspección de redes personalizadas» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Publicación de puertos con -p y diferencias entre modos

Explica «Publicación de puertos con -p y diferencias entre modos» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

Tema extra (si el tiempo lo permite): Cómo el firewall del host afecta el acceso a los puertos publicados.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
podman network ls
```

**Paso 2.** Ejecuta y muestra:

```
podman network create red-curso
```

**Paso 3.** Ejecuta y muestra:

```
podman network inspect red-curso --format '{{range .Subnets}}{{.Subnet}}{{end}}'
```

**Paso 4.** Ejecuta y muestra:

```
podman run -d --name api --network red-curso docker.io/library/alpine:latest sleep 300
```

**Paso 5.** Ejecuta y muestra:

```
podman inspect api --format '{{range $k,$v := .NetworkSettings.Networks}}{{$k}}{{end}}'
```

**Paso 6.** Ejecuta y muestra:

```
podman rm -f api
```

**Paso 7.** Ejecuta y muestra:

```
podman network rm red-curso
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Red por defecto y resolución DNS interna entre contenedores».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01), nivel intermedio, duración 2 semanas. El módulo 3 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
