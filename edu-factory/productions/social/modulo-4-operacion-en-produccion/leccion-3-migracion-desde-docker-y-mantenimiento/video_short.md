# Video corto (TikTok / Reels / Shorts) — Lección 3

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 4. Operación en producción
**Lección:** 3. Migración desde Docker y mantenimiento
**Duración máxima:** 60 segundos
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Guion con marcas de tiempo

### [0:00-0:03] GANCHO
- **Texto en pantalla:** «Alias docker=podman y variables de entorno compatibles» paso a paso, sin relleno (lección 3).
- **Hook visual:** Plano de pantalla ejecutando el primer comando: `podman --version`. Sin zoom lento: el resultado debe verse desde el primer segundo.

### [0:03-0:15] CONTEXTO
Qué se resuelve: Alias docker=podman y variables de entorno compatibles. Podman acepta casi todos los comandos de Docker, así que migrar suele empezar por un alias. Además conviene conocer las herramientas de mantenimiento: uso de disco, limpieza de imágenes y contenedores huérfanos, y el registro de eventos para diagnosticar problemas. Plantea el problema en una frase y di que el comando o el proceso de la lección lo cierra.

### [0:15-0:45] DEMO
1. Ejecuta en pantalla `podman --version` y comenta en voz alta qué hace cada parte.
2. Ejecuta en pantalla `podman system df` y comenta en voz alta qué hace cada parte.
3. Ejecuta en pantalla `podman images` y comenta en voz alta qué hace cada parte.
4. Menciona que hay 7 comandos en total y que el resto está en el material del curso.

### [0:45-0:55] RESULTADO
Cierre en pantalla: resultado correcto de «Alias docker=podman y variables de entorno compatibles» visible. Frase final: «esto es lo que hace falta para alias docker=podman y variables de entorno compatibles; el resto es práctica».

### [0:55-1:00] CTA
«Guarda este video y practica esto hoy: Crea el alias docker=podman en tu shell y ejecuta docker ps para comprobar la compatibilidad. Sígueme para el siguiente paso de Podman en Fedora: contenedores sin Docker».

## Voz en off (texto plano para Edge-TTS, ~130 palabras)

Lección 3 del módulo 4 de Podman en Fedora: contenedores sin Docker. Podman acepta casi todos los comandos de Docker, así que migrar suele empezar por un alias. Además conviene conocer las herramientas de mantenimiento: uso de disco, limpieza de imágenes y contenedores huérfanos, y el registro de eventos para diagnosticar problemas. Primero vemos Alias docker=podman y variables de entorno compatibles, Consumo de disco con podman system df, Limpieza controlada de contenedores, imágenes y volúmenes y después Diagnóstico con podman events y revisión de la raíz de almacenamiento. En pantalla ejecuto 7 comandos, empezando por `podman --version`. Observa qué cambia antes y después. El resultado debe verse completo antes de cerrar; si algo falla, revisa el mensaje de error en lugar de repetir a ciegas. Para practicar: Crea el alias docker=podman en tu shell y ejecuta docker ps para comprobar la compatibilidad. En el material

## Hashtags

#aliasdockerpodmanyvariablesdeentornocompatibles #alias #dockerpodman #variables #entorno #compatibles #consumodediscoconpodmansystemdf #consumo #disco #podman #system #limpiezacontroladadecontenedoresimagenesyvolumenes #limpieza #controlada
