# Módulo 4: Operación en producción

Curso: Podman en Fedora: contenedores sin Docker · Nivel: intermedio

### Lección 1: Contenedores como servicios con systemd y Quadlet

Quadlet convierte un archivo .container en una unidad de systemd, de modo que Podman arranca, detiene y reinicia el contenedor junto con la sesión del usuario. Es la forma recomendada hoy, en lugar del antiguo podman generate systemd.

**Temas cubiertos**

- Qué es Quadlet y cómo lo integra systemd --user
- Estructura de un archivo .container en ~/.config/containers/systemd
- Recarga, arranque y estado del servicio generado
- Reinicio automático y dependencias entre unidades

**Ejercicios prácticos**

- Añade la directiva WantedBy=default.target y habilita el servicio para que arranque con la sesión.
- Modifica la unidad para que reinicie el contenedor automáticamente y verifica con systemctl --user status.

**Recursos**

- Documentación de Quadlet en Podman
- Página de manual systemd.container

### Lección 2: Firewall y exposición segura de servicios

Publicar un puerto en Podman no siempre basta: firewalld puede bloquear el acceso desde la red. Conocer las zonas, los servicios y los puertos abiertos permite exponer solo lo necesario y cerrar todo lo demás.

**Temas cubiertos**

- Estado del firewall y zonas con firewall-cmd
- Consultar servicios y puertos ya abiertos
- Abrir y cerrar puertos de forma permanente con --permanent y --reload
- Zona public frente a interfaces concretas y buenas prácticas de exposición

**Ejercicios prácticos**

- Abre temporalmente el puerto 8080 con sudo firewall-cmd --add-port=8080/tcp y ciérralo después.
- Hazlo permanente con --permanent, recarga con --reload y confirma el cambio con --list-ports.

**Recursos**

- Fedora Docs: firewalld
- Página de manual firewall-cmd

### Lección 3: Migración desde Docker y mantenimiento

Podman acepta casi todos los comandos de Docker, así que migrar suele empezar por un alias. Además conviene conocer las herramientas de mantenimiento: uso de disco, limpieza de imágenes y contenedores huérfanos, y el registro de eventos para diagnosticar problemas.

**Temas cubiertos**

- Alias docker=podman y variables de entorno compatibles
- Consumo de disco con podman system df
- Limpieza controlada de contenedores, imágenes y volúmenes
- Diagnóstico con podman events y revisión de la raíz de almacenamiento

**Ejercicios prácticos**

- Crea el alias docker=podman en tu shell y ejecuta docker ps para comprobar la compatibilidad.
- Revisa el uso de disco, elimina una imagen sin usar y explica cómo liberar espacio de forma segura.

**Recursos**

- Guía de migración de Docker a Podman
- Página de manual podman-system
