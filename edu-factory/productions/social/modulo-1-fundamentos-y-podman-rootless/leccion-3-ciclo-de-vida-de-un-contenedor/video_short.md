# Video corto (TikTok / Reels / Shorts) — Lección 3

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 1. Fundamentos y Podman rootless
**Lección:** 3. Ciclo de vida de un contenedor
**Duración máxima:** 60 segundos
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Guion con marcas de tiempo

### [0:00-0:03] GANCHO
- **Texto en pantalla:** «Ejecución en primer plano y en segundo plano (-d)» paso a paso, sin relleno (lección 3).
- **Hook visual:** Plano de pantalla ejecutando el primer comando: `podman run -d --name web -p 8080:80 docker.io/library/nginx:alpine`. Sin zoom lento: el resultado debe verse desde el primer segundo.

### [0:03-0:15] CONTEXTO
Qué se resuelve: Ejecución en primer plano y en segundo plano (-d). Un contenedor pasa por estados bien definidos: se crea, arranca, ejecuta, se detiene y se elimina. Dominar ese ciclo con run, ps, logs, exec, stop y rm es la base de toda operación diaria. Plantea el problema en una frase y di que el comando o el proceso de la lección lo cierra.

### [0:15-0:45] DEMO
1. Ejecuta en pantalla `podman run -d --name web -p 8080:80 docker.io/library/nginx:alpine` y comenta en voz alta qué hace cada parte.
2. Ejecuta en pantalla `podman ps` y comenta en voz alta qué hace cada parte.
3. Ejecuta en pantalla `podman logs web` y comenta en voz alta qué hace cada parte.
4. Menciona que hay 7 comandos en total y que el resto está en el material del curso.

### [0:45-0:55] RESULTADO
Cierre en pantalla: resultado correcto de «Ejecución en primer plano y en segundo plano (-d)» visible. Frase final: «esto es lo que hace falta para ejecución en primer plano y en segundo plano (-d); el resto es práctica».

### [0:55-1:00] CTA
«Guarda este video y practica esto hoy: Levanta un nginx en el puerto 8080 y compruébalo con curl -I http://localhost:8080. Sígueme para el siguiente paso de Podman en Fedora: contenedores sin Docker».

## Voz en off (texto plano para Edge-TTS, ~130 palabras)

Lección 3 del módulo 1 de Podman en Fedora: contenedores sin Docker. Un contenedor pasa por estados bien definidos: se crea, arranca, ejecuta, se detiene y se elimina. Dominar ese ciclo con run, ps, logs, exec, stop y rm es la base de toda operación diaria. Primero vemos Ejecución en primer plano y en segundo plano (-d), Nombres propios, publicación de puertos y reinicio automático, Lectura de registros con podman logs, Entrar en un contenedor en marcha con podman exec y después Detener y eliminar sin dejar residuos. En pantalla ejecuto 7 comandos, empezando por `podman run -d --name web -p 8080:80 docker.io/library/nginx:alpine`. Observa qué cambia antes y después. El resultado debe verse completo antes de cerrar; si algo falla, revisa el mensaje de error en lugar de repetir a ciegas. Para practicar: Levanta un nginx en el puerto 8080 y compruébalo con curl -I

## Hashtags

#ejecucionenprimerplanoyensegundoplanod #ejecucion #primer #plano #segundo #nombrespropiospublicaciondepuertosyreinicioautomatico #nombres #propios #publicacion #puertos #reinicio #automatico #lecturaderegistrosconpodmanlogs #lectura
