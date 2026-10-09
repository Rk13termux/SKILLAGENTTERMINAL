# Video largo (Facebook / YouTube) — Lección 2

**Plan:** Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
**Módulo:** 8. Proyecto final (crear y desplegar un Bot de Telegram)
**Lección:** 2. Escribir el bot con nano
**Duración estimada:** 3-8 minutos
**Audiencia:** principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular · **Nivel:** principiante a intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Estructura de un bot con python-telegram-bot» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (Escribir el bot con nano) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular suelen bloquearse con Estructura de un bot con python-telegram-bot porque falta el orden de pasos. El bot escucha mensajes y responde. El script pide el token por variable de entorno, define un manejador de /start y otro de texto libre, y arranca con polling. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Estructura de un bot con python-telegram-bot

Explica «Estructura de un bot con python-telegram-bot» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Leer el token desde el entorno y no desde el código

Explica «Leer el token desde el entorno y no desde el código» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Probar el bot en Telegram

Explica «Probar el bot en Telegram» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
export TELEGRAM_TOKEN="1200000000:AA-tu-token-real"
```

**Paso 2.** Ejecuta y muestra:

```
echo $TELEGRAM_TOKEN
```

**Paso 3.** Ejecuta y muestra:

```
nano bot.py
```

**Paso 4.** Ejecuta y muestra:

```
python bot.py
```

**Paso 5.** Ejecuta y muestra:

```
python -m py_compile bot.py
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Estructura de un bot con python-telegram-bot».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel principiante a intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Termux desde Cero: Domina la terminal en tu Android (TERMUX-101), nivel principiante a intermedio, duración 4 semanas. El módulo 8 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
