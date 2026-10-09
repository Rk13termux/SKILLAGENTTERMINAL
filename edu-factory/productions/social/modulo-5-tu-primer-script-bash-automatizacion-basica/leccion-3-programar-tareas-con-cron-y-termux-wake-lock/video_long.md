# Video largo (Facebook / YouTube) — Lección 3

**Plan:** Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
**Módulo:** 5. Tu primer script Bash (automatización básica)
**Lección:** 3. Programar tareas con cron y termux-wake-lock
**Duración estimada:** 3-8 minutos
**Audiencia:** principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular · **Nivel:** principiante a intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Trabajar en segundo plano y no morir con termux-wake-lock» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (Programar tareas con cron y termux-wake-lock) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular suelen bloquearse con Trabajar en segundo plano y no morir con termux-wake-lock porque falta el orden de pasos. termux-services activa el daemon cron para ejecutar scripts a horas fijas, y termux-wake-lock evita que Android suspenda el proceso mientras la tarea corre en segundo plano. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Trabajar en segundo plano y no morir con termux-wake-lock

Explica «Trabajar en segundo plano y no morir con termux-wake-lock» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Instalar y activar servicios con termux-services

Explica «Instalar y activar servicios con termux-services» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Registrar una tarea con crontab

Explica «Registrar una tarea con crontab» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
pkg install termux-services
```

**Paso 2.** Ejecuta y muestra:

```
sv-enable crond
```

**Paso 3.** Ejecuta y muestra:

```
termux-wake-lock
```

**Paso 4.** Ejecuta y muestra:

```
crontab -e
```

**Paso 5.** Ejecuta y muestra:

```
printf '*/30 * * * * ~/bin/respaldar.sh\n' | crontab -
```

**Paso 6.** Ejecuta y muestra:

```
crontab -l
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Trabajar en segundo plano y no morir con termux-wake-lock».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel principiante a intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Termux desde Cero: Domina la terminal en tu Android (TERMUX-101), nivel principiante a intermedio, duración 4 semanas. El módulo 5 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
