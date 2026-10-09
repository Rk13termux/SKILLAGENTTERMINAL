# Video corto (TikTok / Reels / Shorts) — Lección 3

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 3. Almacenamiento, redes y pods
**Lección:** 3. Pods: varios contenedores como uno solo
**Duración máxima:** 60 segundos
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Guion con marcas de tiempo

### [0:00-0:03] GANCHO
- **Texto en pantalla:** «Qué comparte un pod: red, IP, espacio de nombres y puertos» paso a paso, sin relleno (lección 3).
- **Hook visual:** Plano de pantalla ejecutando el primer comando: `podman pod create --name pod-web -p 8081:80`. Sin zoom lento: el resultado debe verse desde el primer segundo.

### [0:03-0:15] CONTEXTO
Qué se resuelve: Qué comparte un pod: red, IP, espacio de nombres y puertos. Un pod es un grupo de contenedores que comparten red, namespace y puertos, igual que en Kubernetes. Es la forma natural de juntar una aplicación con su base de datos o su servidor de caché sin publicar puertos internos. Plantea el problema en una frase y di que el comando o el proceso de la lección lo cierra.

### [0:15-0:45] DEMO
1. Ejecuta en pantalla `podman pod create --name pod-web -p 8081:80` y comenta en voz alta qué hace cada parte.
2. Ejecuta en pantalla `podman pod ls` y comenta en voz alta qué hace cada parte.
3. Ejecuta en pantalla `podman run -d --pod pod-web --name pod-nginx docker.io/library/nginx:alpine` y comenta en voz alta qué hace cada parte.
4. Menciona que hay 7 comandos en total y que el resto está en el material del curso.

### [0:45-0:55] RESULTADO
Cierre en pantalla: resultado correcto de «Qué comparte un pod: red, IP, espacio de nombres y puertos» visible. Frase final: «esto es lo que hace falta para qué comparte un pod: red, ip, espacio de nombres y puertos; el resto es práctica».

### [0:55-1:00] CTA
«Guarda este video y practica esto hoy: Añade un segundo contenedor al pod y comprueba que comparte la dirección IP con el primero. Sígueme para el siguiente paso de Podman en Fedora: contenedores sin Docker».

## Voz en off (texto plano para Edge-TTS, ~130 palabras)

Lección 3 del módulo 3 de Podman en Fedora: contenedores sin Docker. Un pod es un grupo de contenedores que comparten red, namespace y puertos, igual que en Kubernetes. Es la forma natural de juntar una aplicación con su base de datos o su servidor de caché sin publicar puertos internos. Primero vemos Qué comparte un pod: red, IP, espacio de nombres y puertos, Creación de pods con podman pod create, Añadir contenedores a un pod con --pod y después Inspección, parada y eliminación atómica del pod. En pantalla ejecuto 7 comandos, empezando por `podman pod create --name pod-web -p 8081:80`. Observa qué cambia antes y después. El resultado debe verse completo antes de cerrar; si algo falla, revisa el mensaje de error en lugar de repetir a ciegas. Para practicar: Añade un segundo contenedor al pod y comprueba que comparte la dirección IP con

## Hashtags

#quecomparteunpodredipespaciodenombresypuertos #comparte #espacio #nombres #puertos #creaciondepodsconpodmanpodcreate #creacion #podman #create #anadircontenedoresaunpodconpod #anadir #contenedores #pod #inspeccionparadayeliminacionatomicadelpod
