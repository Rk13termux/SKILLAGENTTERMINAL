# Video corto (TikTok / Reels / Shorts) — Lección 1

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 4. Operación en producción
**Lección:** 1. Contenedores como servicios con systemd y Quadlet
**Duración máxima:** 60 segundos
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Guion con marcas de tiempo

### [0:00-0:03] GANCHO
- **Texto en pantalla:** «Qué es Quadlet y cómo lo integra systemd --user» paso a paso, sin relleno (lección 1).
- **Hook visual:** Plano de pantalla ejecutando el primer comando: `mkdir -p ~/.config/containers/systemd`. Sin zoom lento: el resultado debe verse desde el primer segundo.

### [0:03-0:15] CONTEXTO
Qué se resuelve: Qué es Quadlet y cómo lo integra systemd --user. Quadlet convierte un archivo .container en una unidad de systemd, de modo que Podman arranca, detiene y reinicia el contenedor junto con la sesión del usuario. Es la forma recomendada hoy, en lugar del antiguo podman generate systemd. Plantea el problema en una frase y di que el comando o el proceso de la lección lo cierra.

### [0:15-0:45] DEMO
1. Ejecuta en pantalla `mkdir -p ~/.config/containers/systemd` y comenta en voz alta qué hace cada parte.
2. Ejecuta en pantalla `printf '[Unit]\nDescription=Nginx gestionado por Podman\n[Container]\nImage=docker.io/library/nginx:alpine\nPublishPort=8082:80\n[Install]\nWantedBy=default.target\n' > ~/.config/containers/systemd/nginx.container` y comenta en voz alta qué hace cada parte.
3. Ejecuta en pantalla `systemctl --user daemon-reload` y comenta en voz alta qué hace cada parte.
4. Menciona que hay 9 comandos en total y que el resto está en el material del curso.

### [0:45-0:55] RESULTADO
Cierre en pantalla: resultado correcto de «Qué es Quadlet y cómo lo integra systemd --user» visible. Frase final: «esto es lo que hace falta para qué es quadlet y cómo lo integra systemd --user; el resto es práctica».

### [0:55-1:00] CTA
«Guarda este video y practica esto hoy: Añade la directiva WantedBy=default.target y habilita el servicio para que arranque con la sesión. Sígueme para el siguiente paso de Podman en Fedora: contenedores sin Docker».

## Voz en off (texto plano para Edge-TTS, ~130 palabras)

Lección 1 del módulo 4 de Podman en Fedora: contenedores sin Docker. Quadlet convierte un archivo .container en una unidad de systemd, de modo que Podman arranca, detiene y reinicia el contenedor junto con la sesión del usuario. Es la forma recomendada hoy, en lugar del antiguo podman generate systemd. Primero vemos Qué es Quadlet y cómo lo integra systemd --user, Estructura de un archivo .container en ~/.config/containers/systemd, Recarga, arranque y estado del servicio generado y después Reinicio automático y dependencias entre unidades. En pantalla ejecuto 9 comandos, empezando por `mkdir -p ~/.config/containers/systemd`. Observa qué cambia antes y después. El resultado debe verse completo antes de cerrar; si algo falla, revisa el mensaje de error en lugar de repetir a ciegas. Para practicar: Añade la directiva WantedBy=default.target y habilita el servicio para que arranque con la sesión. En el material de Podman en Fedora: contenedores

## Hashtags

#queesquadletycomolointegrasystemduser #quadlet #integra #systemd #user #estructuradeunarchivocontainerenconfigcontainerssystemd #estructura #archivo #container #configcontainerssystemd #recargaarranqueyestadodelserviciogenerado #recarga #arranque #estado
