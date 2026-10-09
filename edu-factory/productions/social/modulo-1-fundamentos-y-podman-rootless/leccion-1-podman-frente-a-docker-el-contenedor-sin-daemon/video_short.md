# Video corto (TikTok / Reels / Shorts) — Lección 1

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 1. Fundamentos y Podman rootless
**Lección:** 1. Podman frente a Docker: el contenedor sin daemon
**Duración máxima:** 60 segundos
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Guion con marcas de tiempo

### [0:00-0:03] GANCHO
- **Texto en pantalla:** «Modelo fork-exec frente al demonio dockerd» paso a paso, sin relleno (lección 1).
- **Hook visual:** Plano de pantalla ejecutando el primer comando: `podman --version`. Sin zoom lento: el resultado debe verse desde el primer segundo.

### [0:03-0:15] CONTEXTO
Qué se resuelve: Modelo fork-exec frente al demonio dockerd. Podman ejecuta contenedores como procesos hijos del usuario, sin un demonio central en segundo plano. Esa diferencia reduce la superficie de ataque y elimina el grupo privilegiado que Docker necesita, a la vez que mantiene una interfaz de línea de comandos casi idéntica. Plantea el problema en una frase y di que el comando o el proceso de la lección lo cierra.

### [0:15-0:45] DEMO
1. Ejecuta en pantalla `podman --version` y comenta en voz alta qué hace cada parte.
2. Ejecuta en pantalla `podman info --format '{{.Host.OS}} {{.Host.Arch}}'` y comenta en voz alta qué hace cada parte.
3. Ejecuta en pantalla `podman info --format '{{.Host.Security.Rootless}}'` y comenta en voz alta qué hace cada parte.
4. Menciona que hay 5 comandos en total y que el resto está en el material del curso.

### [0:45-0:55] RESULTADO
Cierre en pantalla: resultado correcto de «Modelo fork-exec frente al demonio dockerd» visible. Frase final: «esto es lo que hace falta para modelo fork-exec frente al demonio dockerd; el resto es práctica».

### [0:55-1:00] CTA
«Guarda este video y practica esto hoy: Compara la salida de podman info con la de docker info y anota qué campos no existen en Podman. Sígueme para el siguiente paso de Podman en Fedora: contenedores sin Docker».

## Voz en off (texto plano para Edge-TTS, ~130 palabras)

Lección 1 del módulo 1 de Podman en Fedora: contenedores sin Docker. Podman ejecuta contenedores como procesos hijos del usuario, sin un demonio central en segundo plano. Esa diferencia reduce la superficie de ataque y elimina el grupo privilegiado que Docker necesita, a la vez que mantiene una interfaz de línea de comandos casi idéntica. Primero vemos Modelo fork-exec frente al demonio dockerd, Contenedores rootless: sin privilegios y sin grupo docker, Compatibilidad de la CLI con los comandos de Docker y después El socket opcional podman.socket y cuándo conviene activarlo. En pantalla ejecuto 5 comandos, empezando por `podman --version`. Observa qué cambia antes y después. El resultado debe verse completo antes de cerrar; si algo falla, revisa el mensaje de error en lugar de repetir a ciegas. Para practicar: Compara la salida de podman info con la de docker info y anota qué campos no

## Hashtags

#modeloforkexecfrentealdemoniodockerd #modelo #forkexec #frente #demonio #dockerd #contenedoresrootlesssinprivilegiosysingrupodocker #contenedores #rootless #privilegios #grupo #docker #compatibilidaddelacliconloscomandosdedocker #compatibilidad
