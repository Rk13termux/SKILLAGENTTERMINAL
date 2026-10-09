# Post estático (Instagram / LinkedIn) — Lección 2

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 4. Operación en producción
**Lección:** 2. Firewall y exposición segura de servicios
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Copy para la publicación

Estado del firewall y zonas con firewall-cmd es la parte que más se salta y la que más problemas provoca después. En la lección 2 de Podman en Fedora: contenedores sin Docker lo desarmamos en el orden correcto, con el proceso en pantalla.

En esta lección: Estado del firewall y zonas con firewall-cmd; Consultar servicios y puertos ya abiertos; Abrir y cerrar puertos de forma permanente con --permanent y --reload; Zona public frente a interfaces concretas y buenas prácticas de exposición. Publicar un puerto en Podman no siempre basta: firewalld puede bloquear el acceso desde la red. Conocer las zonas, los servicios y los puertos abiertos permite exponer solo lo necesario y cerrar todo lo demás. Al terminar te llevas un ejercicio concreto para practicar: Abre temporalmente el puerto 8080 con sudo firewall-cmd --add-port=8080/tcp y ciérralo después.

Guarda esta publicación para practicarla con calma y compártela con quien esté en el nivel intermedio de Podman en Fedora: contenedores sin Docker. El material completo del curso está en el perfil.

## Primer comentario

Cuéntanos: ¿en qué parte de «Estado del firewall y zonas con firewall-cmd» te has atascado más hasta ahora? Describe el caso concreto y respondemos con el paso que falta.

## Hashtags

#estadodelfirewallyzonasconfirewallcmd #estado #firewall #zonas #firewallcmd #consultarserviciosypuertosyaabiertos #consultar #servicios #puertos #abiertos #abrirycerrarpuertosdeformapermanenteconpermanentyreload #abrir #cerrar #forma
