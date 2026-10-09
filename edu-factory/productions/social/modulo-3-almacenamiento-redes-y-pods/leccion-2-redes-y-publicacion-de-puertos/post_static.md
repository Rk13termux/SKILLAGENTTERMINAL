# Post estático (Instagram / LinkedIn) — Lección 2

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 3. Almacenamiento, redes y pods
**Lección:** 2. Redes y publicación de puertos
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Copy para la publicación

Red por defecto y resolución DNS interna entre contenedores es la parte que más se salta y la que más problemas provoca después. En la lección 2 de Podman en Fedora: contenedores sin Docker lo desarmamos en el orden correcto, con el proceso en pantalla.

En esta lección: Red por defecto y resolución DNS interna entre contenedores; Creación e inspección de redes personalizadas; Publicación de puertos con -p y diferencias entre modos; Cómo el firewall del host afecta el acceso a los puertos publicados. Podman crea una red por defecto y permite definir redes propias para aislar servicios. Los contenedores de una misma red se resuelven por nombre, y los puertos se publican hacia el host con -p indicando puerto_host:puerto_contenedor. Al terminar te llevas un ejercicio concreto para practicar: Crea dos contenedores en la misma red y haz que uno resuelva al otro por su nombre con ping.

Guarda esta publicación para practicarla con calma y compártela con quien esté en el nivel intermedio de Podman en Fedora: contenedores sin Docker. El material completo del curso está en el perfil.

## Primer comentario

Cuéntanos: ¿en qué parte de «Red por defecto y resolución DNS interna entre contenedores» te has atascado más hasta ahora? Describe el caso concreto y respondemos con el paso que falta.

## Hashtags

#redpordefectoyresoluciondnsinternaentrecontenedores #defecto #resolucion #interna #entre #contenedores #creacioneinspeccionderedespersonalizadas #creacion #inspeccion #redes #personalizadas #publicaciondepuertosconpydiferenciasentremodos #publicacion #puertos
