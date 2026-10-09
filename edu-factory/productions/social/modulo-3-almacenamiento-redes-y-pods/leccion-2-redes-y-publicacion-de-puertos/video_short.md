# Video corto (TikTok / Reels / Shorts) — Lección 2

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 3. Almacenamiento, redes y pods
**Lección:** 2. Redes y publicación de puertos
**Duración máxima:** 60 segundos
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Guion con marcas de tiempo

### [0:00-0:03] GANCHO
- **Texto en pantalla:** «Red por defecto y resolución DNS interna entre contenedores» paso a paso, sin relleno (lección 2).
- **Hook visual:** Plano de pantalla ejecutando el primer comando: `podman network ls`. Sin zoom lento: el resultado debe verse desde el primer segundo.

### [0:03-0:15] CONTEXTO
Qué se resuelve: Red por defecto y resolución DNS interna entre contenedores. Podman crea una red por defecto y permite definir redes propias para aislar servicios. Los contenedores de una misma red se resuelven por nombre, y los puertos se publican hacia el host con -p indicando puerto_host:puerto_contenedor. Plantea el problema en una frase y di que el comando o el proceso de la lección lo cierra.

### [0:15-0:45] DEMO
1. Ejecuta en pantalla `podman network ls` y comenta en voz alta qué hace cada parte.
2. Ejecuta en pantalla `podman network create red-curso` y comenta en voz alta qué hace cada parte.
3. Ejecuta en pantalla `podman network inspect red-curso --format '{{range .Subnets}}{{.Subnet}}{{end}}'` y comenta en voz alta qué hace cada parte.
4. Menciona que hay 7 comandos en total y que el resto está en el material del curso.

### [0:45-0:55] RESULTADO
Cierre en pantalla: resultado correcto de «Red por defecto y resolución DNS interna entre contenedores» visible. Frase final: «esto es lo que hace falta para red por defecto y resolución dns interna entre contenedores; el resto es práctica».

### [0:55-1:00] CTA
«Guarda este video y practica esto hoy: Crea dos contenedores en la misma red y haz que uno resuelva al otro por su nombre con ping. Sígueme para el siguiente paso de Podman en Fedora: contenedores sin Docker».

## Voz en off (texto plano para Edge-TTS, ~130 palabras)

Lección 2 del módulo 3 de Podman en Fedora: contenedores sin Docker. Podman crea una red por defecto y permite definir redes propias para aislar servicios. Los contenedores de una misma red se resuelven por nombre, y los puertos se publican hacia el host con -p indicando puerto_host:puerto_contenedor. Primero vemos Red por defecto y resolución DNS interna entre contenedores, Creación e inspección de redes personalizadas, Publicación de puertos con -p y diferencias entre modos y después Cómo el firewall del host afecta el acceso a los puertos publicados. En pantalla ejecuto 7 comandos, empezando por `podman network ls`. Observa qué cambia antes y después. El resultado debe verse completo antes de cerrar; si algo falla, revisa el mensaje de error en lugar de repetir a ciegas. Para practicar: Crea dos contenedores en la misma red y haz que uno resuelva al otro por su nombre

## Hashtags

#redpordefectoyresoluciondnsinternaentrecontenedores #defecto #resolucion #interna #entre #contenedores #creacioneinspeccionderedespersonalizadas #creacion #inspeccion #redes #personalizadas #publicaciondepuertosconpydiferenciasentremodos #publicacion #puertos
