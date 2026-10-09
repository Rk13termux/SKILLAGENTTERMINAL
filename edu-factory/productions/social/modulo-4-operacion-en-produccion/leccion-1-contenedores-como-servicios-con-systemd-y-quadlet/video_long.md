# Video largo (Facebook / YouTube) — Lección 1

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 4. Operación en producción
**Lección:** 1. Contenedores como servicios con systemd y Quadlet
**Duración estimada:** 3-8 minutos
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Qué es Quadlet y cómo lo integra systemd --user» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (Contenedores como servicios con systemd y Quadlet) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: desarrolladores y administradores de sistemas que quieren usar contenedores en Linux suelen bloquearse con Qué es Quadlet y cómo lo integra systemd --user porque falta el orden de pasos. Quadlet convierte un archivo .container en una unidad de systemd, de modo que Podman arranca, detiene y reinicia el contenedor junto con la sesión del usuario. Es la forma recomendada hoy, en lugar del antiguo podman generate systemd. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Qué es Quadlet y cómo lo integra systemd --user

Explica «Qué es Quadlet y cómo lo integra systemd --user» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Estructura de un archivo .container en ~/.config/containers/systemd

Explica «Estructura de un archivo .container en ~/.config/containers/systemd» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Recarga, arranque y estado del servicio generado

Explica «Recarga, arranque y estado del servicio generado» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

Tema extra (si el tiempo lo permite): Reinicio automático y dependencias entre unidades.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
mkdir -p ~/.config/containers/systemd
```

**Paso 2.** Ejecuta y muestra:

```
printf '[Unit]\nDescription=Nginx gestionado por Podman\n[Container]\nImage=docker.io/library/nginx:alpine\nPublishPort=8082:80\n[Install]\nWantedBy=default.target\n' > ~/.config/containers/systemd/nginx.container
```

**Paso 3.** Ejecuta y muestra:

```
systemctl --user daemon-reload
```

**Paso 4.** Ejecuta y muestra:

```
systemctl --user start nginx.service
```

**Paso 5.** Ejecuta y muestra:

```
systemctl --user status nginx.service --no-pager
```

**Paso 6.** Ejecuta y muestra:

```
curl -s -o /dev/null -w 'HTTP %{http_code}\n' http://localhost:8082
```

**Paso 7.** Ejecuta y muestra:

```
systemctl --user stop nginx.service
```

**Paso 8.** Ejecuta y muestra:

```
rm ~/.config/containers/systemd/nginx.container
```

**Paso 9.** Ejecuta y muestra:

```
systemctl --user daemon-reload
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Qué es Quadlet y cómo lo integra systemd --user».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01), nivel intermedio, duración 2 semanas. El módulo 4 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
