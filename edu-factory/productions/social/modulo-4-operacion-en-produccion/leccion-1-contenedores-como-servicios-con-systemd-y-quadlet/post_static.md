# Post estático (Instagram / LinkedIn) — Lección 1

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 4. Operación en producción
**Lección:** 1. Contenedores como servicios con systemd y Quadlet
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Copy para la publicación

Qué es Quadlet y cómo lo integra systemd --user es la parte que más se salta y la que más problemas provoca después. En la lección 1 de Podman en Fedora: contenedores sin Docker lo desarmamos en el orden correcto, con el proceso en pantalla.

En esta lección: Qué es Quadlet y cómo lo integra systemd --user; Estructura de un archivo .container en ~/.config/containers/systemd; Recarga, arranque y estado del servicio generado; Reinicio automático y dependencias entre unidades. Quadlet convierte un archivo .container en una unidad de systemd, de modo que Podman arranca, detiene y reinicia el contenedor junto con la sesión del usuario. Es la forma recomendada hoy, en lugar del antiguo podman generate systemd. Al terminar te llevas un ejercicio concreto para practicar: Añade la directiva WantedBy=default.target y habilita el servicio para que arranque con la sesión.

Guarda esta publicación para practicarla con calma y compártela con quien esté en el nivel intermedio de Podman en Fedora: contenedores sin Docker. El material completo del curso está en el perfil.

## Primer comentario

Cuéntanos: ¿en qué parte de «Qué es Quadlet y cómo lo integra systemd --user» te has atascado más hasta ahora? Describe el caso concreto y respondemos con el paso que falta.

## Hashtags

#queesquadletycomolointegrasystemduser #quadlet #integra #systemd #user #estructuradeunarchivocontainerenconfigcontainerssystemd #estructura #archivo #container #configcontainerssystemd #recargaarranqueyestadodelserviciogenerado #recarga #arranque #estado
