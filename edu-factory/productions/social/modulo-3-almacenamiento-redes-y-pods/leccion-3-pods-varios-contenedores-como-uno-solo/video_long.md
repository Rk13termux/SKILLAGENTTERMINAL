# Video largo (Facebook / YouTube) — Lección 3

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 3. Almacenamiento, redes y pods
**Lección:** 3. Pods: varios contenedores como uno solo
**Duración estimada:** 3-8 minutos
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Qué comparte un pod: red, IP, espacio de nombres y puertos» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (Pods: varios contenedores como uno solo) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: desarrolladores y administradores de sistemas que quieren usar contenedores en Linux suelen bloquearse con Qué comparte un pod: red, IP, espacio de nombres y puertos porque falta el orden de pasos. Un pod es un grupo de contenedores que comparten red, namespace y puertos, igual que en Kubernetes. Es la forma natural de juntar una aplicación con su base de datos o su servidor de caché sin publicar puertos internos. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Qué comparte un pod: red, IP, espacio de nombres y puertos

Explica «Qué comparte un pod: red, IP, espacio de nombres y puertos» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Creación de pods con podman pod create

Explica «Creación de pods con podman pod create» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Añadir contenedores a un pod con --pod

Explica «Añadir contenedores a un pod con --pod» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

Tema extra (si el tiempo lo permite): Inspección, parada y eliminación atómica del pod.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
podman pod create --name pod-web -p 8081:80
```

**Paso 2.** Ejecuta y muestra:

```
podman pod ls
```

**Paso 3.** Ejecuta y muestra:

```
podman run -d --pod pod-web --name pod-nginx docker.io/library/nginx:alpine
```

**Paso 4.** Ejecuta y muestra:

```
podman ps --pod
```

**Paso 5.** Ejecuta y muestra:

```
podman pod inspect pod-web --format '{{.Name}} {{.NumContainers}}'
```

**Paso 6.** Ejecuta y muestra:

```
podman pod stop pod-web
```

**Paso 7.** Ejecuta y muestra:

```
podman pod rm -f pod-web
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Qué comparte un pod: red, IP, espacio de nombres y puertos».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01), nivel intermedio, duración 2 semanas. El módulo 3 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
