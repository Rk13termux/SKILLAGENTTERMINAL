# Video corto (TikTok / Reels / Shorts) — Lección 1

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 2. Imágenes y construcción
**Lección:** 1. Buscar, descargar y gestionar imágenes
**Duración máxima:** 60 segundos
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Guion con marcas de tiempo

### [0:00-0:03] GANCHO
- **Texto en pantalla:** «Búsqueda en registros con podman search» paso a paso, sin relleno (lección 1).
- **Hook visual:** Plano de pantalla ejecutando el primer comando: `podman search docker.io/library/alpine --limit 3`. Sin zoom lento: el resultado debe verse desde el primer segundo.

### [0:03-0:15] CONTEXTO
Qué se resuelve: Búsqueda en registros con podman search. Las imágenes son plantillas de solo lectura que Podman descarga de registros como Docker Hub o Quay. Antes de usarlas conviene buscarlas, inspeccionar su origen y entender las capas que las componen. Plantea el problema en una frase y di que el comando o el proceso de la lección lo cierra.

### [0:15-0:45] DEMO
1. Ejecuta en pantalla `podman search docker.io/library/alpine --limit 3` y comenta en voz alta qué hace cada parte.
2. Ejecuta en pantalla `podman pull docker.io/library/alpine:latest` y comenta en voz alta qué hace cada parte.
3. Ejecuta en pantalla `podman images` y comenta en voz alta qué hace cada parte.
4. Menciona que hay 5 comandos en total y que el resto está en el material del curso.

### [0:45-0:55] RESULTADO
Cierre en pantalla: resultado correcto de «Búsqueda en registros con podman search» visible. Frase final: «esto es lo que hace falta para búsqueda en registros con podman search; el resto es práctica».

### [0:55-1:00] CTA
«Guarda este video y practica esto hoy: Inspecciona la imagen Alpine y localiza su digest con podman inspect. Sígueme para el siguiente paso de Podman en Fedora: contenedores sin Docker».

## Voz en off (texto plano para Edge-TTS, ~130 palabras)

Lección 1 del módulo 2 de Podman en Fedora: contenedores sin Docker. Las imágenes son plantillas de solo lectura que Podman descarga de registros como Docker Hub o Quay. Antes de usarlas conviene buscarlas, inspeccionar su origen y entender las capas que las componen. Primero vemos Búsqueda en registros con podman search, Descarga explícita con podman pull y nombres completos de imagen, Listado e inspección con podman images, inspect y history y después Capas, digests y por qué conviene fijar etiquetas. En pantalla ejecuto 5 comandos, empezando por `podman search docker.io/library/alpine --limit 3`. Observa qué cambia antes y después. El resultado debe verse completo antes de cerrar; si algo falla, revisa el mensaje de error en lugar de repetir a ciegas. Para practicar: Inspecciona la imagen Alpine y localiza su digest con podman inspect. En el material de Podman en Fedora: contenedores sin Docker encontrarás

## Hashtags

#busquedaenregistrosconpodmansearch #busqueda #registros #podman #search #descargaexplicitaconpodmanpullynombrescompletosdeimagen #descarga #explicita #nombres #completos #imagen #listadoeinspeccionconpodmanimagesinspectyhistory #listado #inspeccion
