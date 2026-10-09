# Video corto (TikTok / Reels / Shorts) — Lección 3

**Plan:** Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
**Módulo:** 8. Proyecto final (crear y desplegar un Bot de Telegram)
**Lección:** 3. Desplegarlo en segundo plano y mantenerlo vivo
**Duración máxima:** 60 segundos
**Audiencia:** principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular · **Nivel:** principiante a intermedio

## Guion con marcas de tiempo

### [0:00-0:03] GANCHO
- **Texto en pantalla:** «Lanzar en segundo plano con nohup y el operador &» paso a paso, sin relleno (lección 3).
- **Hook visual:** Plano de pantalla ejecutando el primer comando: `pkg install termux-api`. Sin zoom lento: el resultado debe verse desde el primer segundo.

### [0:03-0:15] CONTEXTO
Qué se resuelve: Lanzar en segundo plano con nohup y el operador &. Un bot que se apaga cuando cierras la terminal no sirve de nada. nohup lo lanza en segundo plano ignorando señales, y termux-wake-lock impide que Android lo suspenda. Plantea el problema en una frase y di que el comando o el proceso de la lección lo cierra.

### [0:15-0:45] DEMO
1. Ejecuta en pantalla `pkg install termux-api` y comenta en voz alta qué hace cada parte.
2. Ejecuta en pantalla `termux-wake-lock` y comenta en voz alta qué hace cada parte.
3. Ejecuta en pantalla `nohup python bot.py > bot.log 2>&1 &` y comenta en voz alta qué hace cada parte.
4. Menciona que hay 6 comandos en total y que el resto está en el material del curso.

### [0:45-0:55] RESULTADO
Cierre en pantalla: resultado correcto de «Lanzar en segundo plano con nohup y el operador &» visible. Frase final: «esto es lo que hace falta para lanzar en segundo plano con nohup y el operador &; el resto es práctica».

### [0:55-1:00] CTA
«Guarda este video y practica esto hoy: Despliega tu bot con nohup y verifica que responde. Sígueme para el siguiente paso de Termux desde Cero: Domina la terminal en tu Android».

## Voz en off (texto plano para Edge-TTS, ~130 palabras)

Lección 3 del módulo 8 de Termux desde Cero: Domina la terminal en tu Android. Un bot que se apaga cuando cierras la terminal no sirve de nada. nohup lo lanza en segundo plano ignorando señales, y termux-wake-lock impide que Android lo suspenda. Primero vemos Lanzar en segundo plano con nohup y el operador &, Impedir el suspenso de Android con termux-wake-lock y después Ver los registros y detener el proceso. En pantalla ejecuto 6 comandos, empezando por `pkg install termux-api`. Observa qué cambia antes y después. El resultado debe verse completo antes de cerrar; si algo falla, revisa el mensaje de error en lugar de repetir a ciegas. Para practicar: Despliega tu bot con nohup y verifica que responde. En el material de Termux desde Cero: Domina la terminal en tu Android encontrarás la lección completa con ejercicios y revisión.

## Hashtags

#lanzarensegundoplanoconnohupyeloperador #lanzar #segundo #plano #nohup #operador #impedirelsuspensodeandroidcontermuxwakelock #impedir #suspenso #android #termuxwakelock #verlosregistrosydetenerelproceso #registros #detener
