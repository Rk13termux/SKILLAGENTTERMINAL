# Post estático (Instagram / LinkedIn) — Lección 1

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 3. Almacenamiento, redes y pods
**Lección:** 1. Volúmenes y persistencia de datos
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Copy para la publicación

Diferencia entre capa de escritura, bind mount y volumen gestionado es la parte que más se salta y la que más problemas provoca después. En la lección 1 de Podman en Fedora: contenedores sin Docker lo desarmamos en el orden correcto, con el proceso en pantalla.

En esta lección: Diferencia entre capa de escritura, bind mount y volumen gestionado; Creación, listado e inspección de volúmenes; Montaje de un volumen con -v en podman run; Punto de montaje real en el host y permisos rootless. El sistema de archivos de un contenedor es efímero: al eliminarlo se pierde su contenido. Los volúmenes de Podman guardan datos fuera del contenedor y sobreviven a su borrado, lo que permite separar el estado de la aplicación de su imagen. Al terminar te llevas un ejercicio concreto para practicar: Escribe un archivo desde un contenedor y léelo desde otro distinto usando el mismo volumen.

Guarda esta publicación para practicarla con calma y compártela con quien esté en el nivel intermedio de Podman en Fedora: contenedores sin Docker. El material completo del curso está en el perfil.

## Primer comentario

Cuéntanos: ¿en qué parte de «Diferencia entre capa de escritura, bind mount y volumen gestionado» te has atascado más hasta ahora? Describe el caso concreto y respondemos con el paso que falta.

## Hashtags

#diferenciaentrecapadeescriturabindmountyvolumengestionado #diferencia #entre #escritura #mount #volumen #gestionado #creacionlistadoeinspecciondevolumenes #creacion #listado #inspeccion #volumenes #montajedeunvolumenconvenpodmanrun #montaje
