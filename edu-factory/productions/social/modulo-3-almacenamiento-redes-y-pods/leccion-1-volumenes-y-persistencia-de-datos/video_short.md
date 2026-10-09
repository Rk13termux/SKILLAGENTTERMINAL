# Video corto (TikTok / Reels / Shorts) — Lección 1

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 3. Almacenamiento, redes y pods
**Lección:** 1. Volúmenes y persistencia de datos
**Duración máxima:** 60 segundos
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Guion con marcas de tiempo

### [0:00-0:03] GANCHO
- **Texto en pantalla:** «Diferencia entre capa de escritura, bind mount y volumen gestionado» paso a paso, sin relleno (lección 1).
- **Hook visual:** Plano de pantalla ejecutando el primer comando: `podman volume create datos-web`. Sin zoom lento: el resultado debe verse desde el primer segundo.

### [0:03-0:15] CONTEXTO
Qué se resuelve: Diferencia entre capa de escritura, bind mount y volumen gestionado. El sistema de archivos de un contenedor es efímero: al eliminarlo se pierde su contenido. Los volúmenes de Podman guardan datos fuera del contenedor y sobreviven a su borrado, lo que permite separar el estado de la aplicación de su imagen. Plantea el problema en una frase y di que el comando o el proceso de la lección lo cierra.

### [0:15-0:45] DEMO
1. Ejecuta en pantalla `podman volume create datos-web` y comenta en voz alta qué hace cada parte.
2. Ejecuta en pantalla `podman volume ls` y comenta en voz alta qué hace cada parte.
3. Ejecuta en pantalla `podman volume inspect datos-web --format '{{.Mountpoint}}'` y comenta en voz alta qué hace cada parte.
4. Menciona que hay 6 comandos en total y que el resto está en el material del curso.

### [0:45-0:55] RESULTADO
Cierre en pantalla: resultado correcto de «Diferencia entre capa de escritura, bind mount y volumen gestionado» visible. Frase final: «esto es lo que hace falta para diferencia entre capa de escritura, bind mount y volumen gestionado; el resto es práctica».

### [0:55-1:00] CTA
«Guarda este video y practica esto hoy: Escribe un archivo desde un contenedor y léelo desde otro distinto usando el mismo volumen. Sígueme para el siguiente paso de Podman en Fedora: contenedores sin Docker».

## Voz en off (texto plano para Edge-TTS, ~130 palabras)

Lección 1 del módulo 3 de Podman en Fedora: contenedores sin Docker. El sistema de archivos de un contenedor es efímero: al eliminarlo se pierde su contenido. Los volúmenes de Podman guardan datos fuera del contenedor y sobreviven a su borrado, lo que permite separar el estado de la aplicación de su imagen. Primero vemos Diferencia entre capa de escritura, bind mount y volumen gestionado, Creación, listado e inspección de volúmenes, Montaje de un volumen con -v en podman run y después Punto de montaje real en el host y permisos rootless. En pantalla ejecuto 6 comandos, empezando por `podman volume create datos-web`. Observa qué cambia antes y después. El resultado debe verse completo antes de cerrar; si algo falla, revisa el mensaje de error en lugar de repetir a ciegas. Para practicar: Escribe un archivo desde un contenedor y léelo desde otro distinto usando

## Hashtags

#diferenciaentrecapadeescriturabindmountyvolumengestionado #diferencia #entre #escritura #mount #volumen #gestionado #creacionlistadoeinspecciondevolumenes #creacion #listado #inspeccion #volumenes #montajedeunvolumenconvenpodmanrun #montaje
