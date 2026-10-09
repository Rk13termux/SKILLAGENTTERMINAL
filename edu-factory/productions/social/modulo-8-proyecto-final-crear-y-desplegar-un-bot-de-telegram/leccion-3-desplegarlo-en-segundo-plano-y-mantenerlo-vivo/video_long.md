# Video largo (Facebook / YouTube) — Lección 3

**Plan:** Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
**Módulo:** 8. Proyecto final (crear y desplegar un Bot de Telegram)
**Lección:** 3. Desplegarlo en segundo plano y mantenerlo vivo
**Duración estimada:** 3-8 minutos
**Audiencia:** principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular · **Nivel:** principiante a intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Lanzar en segundo plano con nohup y el operador &» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (Desplegarlo en segundo plano y mantenerlo vivo) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular suelen bloquearse con Lanzar en segundo plano con nohup y el operador & porque falta el orden de pasos. Un bot que se apaga cuando cierras la terminal no sirve de nada. nohup lo lanza en segundo plano ignorando señales, y termux-wake-lock impide que Android lo suspenda. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Lanzar en segundo plano con nohup y el operador &

Explica «Lanzar en segundo plano con nohup y el operador &» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Impedir el suspenso de Android con termux-wake-lock

Explica «Impedir el suspenso de Android con termux-wake-lock» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Ver los registros y detener el proceso

Explica «Ver los registros y detener el proceso» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
pkg install termux-api
```

**Paso 2.** Ejecuta y muestra:

```
termux-wake-lock
```

**Paso 3.** Ejecuta y muestra:

```
nohup python bot.py > bot.log 2>&1 &
```

**Paso 4.** Ejecuta y muestra:

```
tail -f bot.log
```

**Paso 5.** Ejecuta y muestra:

```
ps aux | grep bot.py
```

**Paso 6.** Ejecuta y muestra:

```
kill $(pgrep -f bot.py)
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Lanzar en segundo plano con nohup y el operador &».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel principiante a intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Termux desde Cero: Domina la terminal en tu Android (TERMUX-101), nivel principiante a intermedio, duración 4 semanas. El módulo 8 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
