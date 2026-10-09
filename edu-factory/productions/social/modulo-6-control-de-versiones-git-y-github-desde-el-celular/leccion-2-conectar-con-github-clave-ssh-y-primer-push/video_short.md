# Video corto (TikTok / Reels / Shorts) — Lección 2

**Plan:** Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
**Módulo:** 6. Control de versiones (Git y GitHub desde el celular)
**Lección:** 2. Conectar con GitHub: clave SSH y primer push
**Duración máxima:** 60 segundos
**Audiencia:** principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular · **Nivel:** principiante a intermedio

## Guion con marcas de tiempo

### [0:00-0:03] GANCHO
- **Texto en pantalla:** «Generar una clave con ssh-keygen» paso a paso, sin relleno (lección 2).
- **Hook visual:** Plano de pantalla ejecutando el primer comando: `pkg install openssh`. Sin zoom lento: el resultado debe verse desde el primer segundo.

### [0:03-0:15] CONTEXTO
Qué se resuelve: Generar una clave con ssh-keygen. Con una clave SSH (ed25519), git habla con GitHub sin contraseña. La clave se copia en GitHub y luego el repositorio remoto se enlaza con git remote add. Plantea el problema en una frase y di que el comando o el proceso de la lección lo cierra.

### [0:15-0:45] DEMO
1. Ejecuta en pantalla `pkg install openssh` y comenta en voz alta qué hace cada parte.
2. Ejecuta en pantalla `ssh-keygen -t ed25519 -C "tu@correo.com"` y comenta en voz alta qué hace cada parte.
3. Ejecuta en pantalla `cat ~/.ssh/id_ed25519.pub` y comenta en voz alta qué hace cada parte.
4. Menciona que hay 7 comandos en total y que el resto está en el material del curso.

### [0:45-0:55] RESULTADO
Cierre en pantalla: resultado correcto de «Generar una clave con ssh-keygen» visible. Frase final: «esto es lo que hace falta para generar una clave con ssh-keygen; el resto es práctica».

### [0:55-1:00] CTA
«Guarda este video y practica esto hoy: Genera tu clave, cópiala en GitHub y haz tu primer push. Sígueme para el siguiente paso de Termux desde Cero: Domina la terminal en tu Android».

## Voz en off (texto plano para Edge-TTS, ~130 palabras)

Lección 2 del módulo 6 de Termux desde Cero: Domina la terminal en tu Android. Con una clave SSH (ed25519), git habla con GitHub sin contraseña. La clave se copia en GitHub y luego el repositorio remoto se enlaza con git remote add. Primero vemos Generar una clave con ssh-keygen, Añadir la clave pública a GitHub y después Enlazar, publicar (push) y descargar (clone). En pantalla ejecuto 7 comandos, empezando por `pkg install openssh`. Observa qué cambia antes y después. El resultado debe verse completo antes de cerrar; si algo falla, revisa el mensaje de error en lugar de repetir a ciegas. Para practicar: Genera tu clave, cópiala en GitHub y haz tu primer push. En el material de Termux desde Cero: Domina la terminal en tu Android encontrarás la lección completa con ejercicios y revisión.

## Hashtags

#generarunaclaveconsshkeygen #generar #clave #sshkeygen #anadirlaclavepublicaagithub #anadir #publica #github #enlazarpublicarpushydescargarclone #enlazar #publicar #descargar #clone #termuxdesdecerodominalaterminalentuandroid
