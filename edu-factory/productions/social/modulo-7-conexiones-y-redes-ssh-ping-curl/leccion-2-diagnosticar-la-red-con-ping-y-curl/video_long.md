# Video largo (Facebook / YouTube) — Lección 2

**Plan:** Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
**Módulo:** 7. Conexiones y redes (SSH, ping, curl)
**Lección:** 2. Diagnosticar la red con ping y curl
**Duración estimada:** 3-8 minutos
**Audiencia:** principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular · **Nivel:** principiante a intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Medir la conectividad con ping -c» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (Diagnosticar la red con ping y curl) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular suelen bloquearse con Medir la conectividad con ping -c porque falta el orden de pasos. ping comprueba si un host responde midiendo latencia, y curl hace peticiones HTTP. El trío ping, curl -I y curl -v da una imagen de si el problema es la red o el servidor. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Medir la conectividad con ping -c

Explica «Medir la conectividad con ping -c» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Ver cabeceras HTTP con curl -I

Explica «Ver cabeceras HTTP con curl -I» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Depurar con curl -v y --max-time

Explica «Depurar con curl -v y --max-time» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
ping -c 4 1.1.1.1
```

**Paso 2.** Ejecuta y muestra:

```
pkg install curl
```

**Paso 3.** Ejecuta y muestra:

```
curl -I https://example.com
```

**Paso 4.** Ejecuta y muestra:

```
curl -v --max-time 10 https://api.telegram.org
```

**Paso 5.** Ejecuta y muestra:

```
curl -s https://api.github.com/repos/termux/termux-packages
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Medir la conectividad con ping -c».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel principiante a intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Termux desde Cero: Domina la terminal en tu Android (TERMUX-101), nivel principiante a intermedio, duración 4 semanas. El módulo 7 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
