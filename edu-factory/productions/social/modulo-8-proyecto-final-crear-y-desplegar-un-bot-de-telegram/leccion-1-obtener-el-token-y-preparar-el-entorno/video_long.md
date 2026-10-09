# Video largo (Facebook / YouTube) — Lección 1

**Plan:** Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
**Módulo:** 8. Proyecto final (crear y desplegar un Bot de Telegram)
**Lección:** 1. Obtener el token y preparar el entorno
**Duración estimada:** 3-8 minutos
**Audiencia:** principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular · **Nivel:** principiante a intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Crear el bot con BotFather y anotar el token» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (Obtener el token y preparar el entorno) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular suelen bloquearse con Crear el bot con BotFather y anotar el token porque falta el orden de pasos. Los bots de Telegram se crean con BotFather, que entrega un token de API. En Termux se prepara el entorno: carpeta del proyecto, entorno virtual y dependencias con pip. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Crear el bot con BotFather y anotar el token

Explica «Crear el bot con BotFather y anotar el token» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Entorno virtual aislado para el proyecto

Explica «Entorno virtual aislado para el proyecto» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Instalar la librería python-telegram-bot

Explica «Instalar la librería python-telegram-bot» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
pkg install python
```

**Paso 2.** Ejecuta y muestra:

```
mkdir -p ~/telebot
```

**Paso 3.** Ejecuta y muestra:

```
cd ~/telebot
```

**Paso 4.** Ejecuta y muestra:

```
python -m venv venv
```

**Paso 5.** Ejecuta y muestra:

```
source venv/bin/activate
```

**Paso 6.** Ejecuta y muestra:

```
pip install python-telegram-bot
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Crear el bot con BotFather y anotar el token».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel principiante a intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Termux desde Cero: Domina la terminal en tu Android (TERMUX-101), nivel principiante a intermedio, duración 4 semanas. El módulo 8 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
