# Video largo (Facebook / YouTube) — Lección 3

**Plan:** Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
**Módulo:** 4. Instalación de entornos (Python, Node.js, Git)
**Lección:** 3. Git y configuración de identidad
**Duración estimada:** 3-8 minutos
**Audiencia:** principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular · **Nivel:** principiante a intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Instalar Git y comprobar la versión» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (Git y configuración de identidad) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular suelen bloquearse con Instalar Git y comprobar la versión porque falta el orden de pasos. Git es el control de versiones por defecto y viene listo en Termux. Lo único obligatorio antes de empezar es declarar tu nombre y correo, porque quedan grabados en cada commit. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Instalar Git y comprobar la versión

Explica «Instalar Git y comprobar la versión» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Configurar user.name y user.email a nivel global

Explica «Configurar user.name y user.email a nivel global» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Iniciar un repositorio e inspeccionarlo

Explica «Iniciar un repositorio e inspeccionarlo» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
pkg install git
```

**Paso 2.** Ejecuta y muestra:

```
git --version
```

**Paso 3.** Ejecuta y muestra:

```
git config --global user.name "Tu Nombre"
```

**Paso 4.** Ejecuta y muestra:

```
git config --global user.email "tu@correo.com"
```

**Paso 5.** Ejecuta y muestra:

```
git init
```

**Paso 6.** Ejecuta y muestra:

```
git status
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Instalar Git y comprobar la versión».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel principiante a intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Termux desde Cero: Domina la terminal en tu Android (TERMUX-101), nivel principiante a intermedio, duración 4 semanas. El módulo 4 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
