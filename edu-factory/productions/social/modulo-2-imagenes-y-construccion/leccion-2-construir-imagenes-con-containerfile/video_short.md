# Video corto (TikTok / Reels / Shorts) — Lección 2

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 2. Imágenes y construcción
**Lección:** 2. Construir imágenes con Containerfile
**Duración máxima:** 60 segundos
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Guion con marcas de tiempo

### [0:00-0:03] GANCHO
- **Texto en pantalla:** «Estructura de un Containerfile: FROM, RUN, COPY, CMD» paso a paso, sin relleno (lección 2).
- **Hook visual:** Plano de pantalla ejecutando el primer comando: `mkdir -p /tmp/podman-curso && cd /tmp/podman-curso`. Sin zoom lento: el resultado debe verse desde el primer segundo.

### [0:03-0:15] CONTEXTO
Qué se resuelve: Estructura de un Containerfile: FROM, RUN, COPY, CMD. El Containerfile es el mismo formato que el Dockerfile y se construye con podman build sin demonio. Cada instrucción genera una capa, de modo que el orden de las instrucciones afecta directamente la velocidad de reconstrucción. Plantea el problema en una frase y di que el comando o el proceso de la lección lo cierra.

### [0:15-0:45] DEMO
1. Ejecuta en pantalla `mkdir -p /tmp/podman-curso && cd /tmp/podman-curso` y comenta en voz alta qué hace cada parte.
2. Ejecuta en pantalla `printf 'FROM docker.io/library/alpine:latest\nRUN echo "construido en Fedora" > /mensaje.txt\nCMD ["cat","/mensaje.txt"]\n' > Containerfile` y comenta en voz alta qué hace cada parte.
3. Ejecuta en pantalla `cat Containerfile` y comenta en voz alta qué hace cada parte.
4. Menciona que hay 6 comandos en total y que el resto está en el material del curso.

### [0:45-0:55] RESULTADO
Cierre en pantalla: resultado correcto de «Estructura de un Containerfile: FROM, RUN, COPY, CMD» visible. Frase final: «esto es lo que hace falta para estructura de un containerfile: from, run, copy, cmd; el resto es práctica».

### [0:55-1:00] CTA
«Guarda este video y practica esto hoy: Añade una instrucción COPY a tu Containerfile y reconstruye la imagen. Sígueme para el siguiente paso de Podman en Fedora: contenedores sin Docker».

## Voz en off (texto plano para Edge-TTS, ~130 palabras)

Lección 2 del módulo 2 de Podman en Fedora: contenedores sin Docker. El Containerfile es el mismo formato que el Dockerfile y se construye con podman build sin demonio. Cada instrucción genera una capa, de modo que el orden de las instrucciones afecta directamente la velocidad de reconstrucción. Primero vemos Estructura de un Containerfile: FROM, RUN, COPY, CMD, Construcción con podman build y contexto de directorio, Etiquetado de la imagen construida y después Ejecución y verificación de la imagen resultante. En pantalla ejecuto 6 comandos, empezando por `mkdir -p /tmp/podman-curso && cd /tmp/podman-curso`. Observa qué cambia antes y después. El resultado debe verse completo antes de cerrar; si algo falla, revisa el mensaje de error en lugar de repetir a ciegas. Para practicar: Añade una instrucción COPY a tu Containerfile y reconstruye la imagen. En el material de Podman en Fedora: contenedores sin Docker encontrarás

## Hashtags

#estructuradeuncontainerfilefromruncopycmd #estructura #containerfile #construccionconpodmanbuildycontextodedirectorio #construccion #podman #build #contexto #directorio #etiquetadodelaimagenconstruida #etiquetado #imagen #construida #ejecucionyverificaciondelaimagenresultante
