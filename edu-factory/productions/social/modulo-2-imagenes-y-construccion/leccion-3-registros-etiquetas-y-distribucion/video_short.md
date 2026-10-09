# Video corto (TikTok / Reels / Shorts) — Lección 3

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 2. Imágenes y construcción
**Lección:** 3. Registros, etiquetas y distribución
**Duración máxima:** 60 segundos
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Guion con marcas de tiempo

### [0:00-0:03] GANCHO
- **Texto en pantalla:** «Anatomía de un nombre de imagen: registro, repositorio, etiqueta, digest» paso a paso, sin relleno (lección 3).
- **Hook visual:** Plano de pantalla ejecutando el primer comando: `podman tag hola-podman localhost:5000/hola-podman:1.0`. Sin zoom lento: el resultado debe verse desde el primer segundo.

### [0:03-0:15] CONTEXTO
Qué se resuelve: Anatomía de un nombre de imagen: registro, repositorio, etiqueta, digest. Una imagen se identifica por su repositorio, su etiqueta y su digest. Para compartirla se etiqueta con el nombre del registro y se sube con podman push tras autenticarse, mientras skopeo permite inspeccionar imágenes remotas sin descargarlas. Plantea el problema en una frase y di que el comando o el proceso de la lección lo cierra.

### [0:15-0:45] DEMO
1. Ejecuta en pantalla `podman tag hola-podman localhost:5000/hola-podman:1.0` y comenta en voz alta qué hace cada parte.
2. Ejecuta en pantalla `podman images 'localhost:5000/*'` y comenta en voz alta qué hace cada parte.
3. Ejecuta en pantalla `skopeo inspect --format '{{.Digest}}' docker://docker.io/library/alpine:latest` y comenta en voz alta qué hace cada parte.
4. Menciona que hay 5 comandos en total y que el resto está en el material del curso.

### [0:45-0:55] RESULTADO
Cierre en pantalla: resultado correcto de «Anatomía de un nombre de imagen: registro, repositorio, etiqueta, digest» visible. Frase final: «esto es lo que hace falta para anatomía de un nombre de imagen: registro, repositorio, etiqueta, digest; el resto es práctica».

### [0:55-1:00] CTA
«Guarda este video y practica esto hoy: Crea una cuenta en Quay.io y publica tu imagen con podman push. Sígueme para el siguiente paso de Podman en Fedora: contenedores sin Docker».

## Voz en off (texto plano para Edge-TTS, ~130 palabras)

Lección 3 del módulo 2 de Podman en Fedora: contenedores sin Docker. Una imagen se identifica por su repositorio, su etiqueta y su digest. Para compartirla se etiqueta con el nombre del registro y se sube con podman push tras autenticarse, mientras skopeo permite inspeccionar imágenes remotas sin descargarlas. Primero vemos Anatomía de un nombre de imagen: registro, repositorio, etiqueta, digest, podman tag para preparar una imagen antes de publicarla, podman login y podman push hacia un registro y después Inspección remota con skopeo inspect. En pantalla ejecuto 5 comandos, empezando por `podman tag hola-podman localhost:5000/hola-podman:1.0`. Observa qué cambia antes y después. El resultado debe verse completo antes de cerrar; si algo falla, revisa el mensaje de error en lugar de repetir a ciegas. Para practicar: Crea una cuenta en Quay.io y publica tu imagen con podman push. En el material de Podman en Fedora:

## Hashtags

#anatomiadeunnombredeimagenregistrorepositorioetiquetadigest #anatomia #nombre #imagen #registro #repositorio #etiqueta #digest #podmantagparaprepararunaimagenantesdepublicarla #podman #preparar #antes #publicarla #podmanloginypodmanpushhaciaunregistro
