# Video largo (Facebook / YouTube) — Lección 2

**Plan:** Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
**Módulo:** 2. Comandos esenciales de Linux (ls, cd, pwd, mkdir, rm)
**Lección:** 2. listar, crear y eliminar carpetas
**Duración estimada:** 3-8 minutos
**Audiencia:** principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular · **Nivel:** principiante a intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Listar con ls, -l (detalle) y -a (ocultos)» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (listar, crear y eliminar carpetas) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular suelen bloquearse con Listar con ls, -l (detalle) y -a (ocultos) porque falta el orden de pasos. ls lista, mkdir crea y rm elimina. Con esas tres herramientas se construye una estructura de proyectos, y con rm hay que actuar con cuidado porque no hay papelera. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Listar con ls, -l (detalle) y -a (ocultos)

Explica «Listar con ls, -l (detalle) y -a (ocultos)» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Crear carpetas con mkdir, también anidadas con -p

Explica «Crear carpetas con mkdir, también anidadas con -p» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Eliminar con rm y con rm -rf (usar con criterio)

Explica «Eliminar con rm y con rm -rf (usar con criterio)» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
mkdir -p proyectos/cursos
```

**Paso 2.** Ejecuta y muestra:

```
ls -la proyectos
```

**Paso 3.** Ejecuta y muestra:

```
touch proyectos/notas.txt
```

**Paso 4.** Ejecuta y muestra:

```
rm proyectos/notas.txt
```

**Paso 5.** Ejecuta y muestra:

```
rm -rf proyectos
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Listar con ls, -l (detalle) y -a (ocultos)».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel principiante a intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Termux desde Cero: Domina la terminal en tu Android (TERMUX-101), nivel principiante a intermedio, duración 4 semanas. El módulo 2 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
