# Post estático (Instagram / LinkedIn) — Lección 1

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 1. Fundamentos y Podman rootless
**Lección:** 1. Podman frente a Docker: el contenedor sin daemon
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Copy para la publicación

Modelo fork-exec frente al demonio dockerd es la parte que más se salta y la que más problemas provoca después. En la lección 1 de Podman en Fedora: contenedores sin Docker lo desarmamos en el orden correcto, con el proceso en pantalla.

En esta lección: Modelo fork-exec frente al demonio dockerd; Contenedores rootless: sin privilegios y sin grupo docker; Compatibilidad de la CLI con los comandos de Docker; El socket opcional podman.socket y cuándo conviene activarlo. Podman ejecuta contenedores como procesos hijos del usuario, sin un demonio central en segundo plano. Esa diferencia reduce la superficie de ataque y elimina el grupo privilegiado que Docker necesita, a la vez que mantiene una interfaz de línea de comandos casi idéntica. Al terminar te llevas un ejercicio concreto para practicar: Compara la salida de podman info con la de docker info y anota qué campos no existen en Podman.

Guarda esta publicación para practicarla con calma y compártela con quien esté en el nivel intermedio de Podman en Fedora: contenedores sin Docker. El material completo del curso está en el perfil.

## Primer comentario

Cuéntanos: ¿en qué parte de «Modelo fork-exec frente al demonio dockerd» te has atascado más hasta ahora? Describe el caso concreto y respondemos con el paso que falta.

## Hashtags

#modeloforkexecfrentealdemoniodockerd #modelo #forkexec #frente #demonio #dockerd #contenedoresrootlesssinprivilegiosysingrupodocker #contenedores #rootless #privilegios #grupo #docker #compatibilidaddelacliconloscomandosdedocker #compatibilidad
