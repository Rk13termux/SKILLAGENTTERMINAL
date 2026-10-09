# Video largo (Facebook / YouTube) — Lección 3

**Plan:** Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
**Módulo:** 2. Comandos esenciales de Linux (ls, cd, pwd, mkdir, rm)
**Lección:** 3. mover, copiar y ver archivos
**Duración estimada:** 3-8 minutos
**Audiencia:** principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular · **Nivel:** principiante a intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Copiar con cp y sus variantes -r para carpetas» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (mover, copiar y ver archivos) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular suelen bloquearse con Copiar con cp y sus variantes -r para carpetas porque falta el orden de pasos. cp copia, mv mueve o renombra y cat muestra el contenido. Con estos comandos ya puedes organizar tus apuntes y tus scripts sin abrir un administrador de archivos. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Copiar con cp y sus variantes -r para carpetas

Explica «Copiar con cp y sus variantes -r para carpetas» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Mover y renombrar con mv

Explica «Mover y renombrar con mv» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Ver archivos con cat y paginar con less

Explica «Ver archivos con cat y paginar con less» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
cp notas.txt notas-copia.txt
```

**Paso 2.** Ejecuta y muestra:

```
mv notas-copia.txt apuntes.txt
```

**Paso 3.** Ejecuta y muestra:

```
cat apuntes.txt
```

**Paso 4.** Ejecuta y muestra:

```
mkdir -p ~/backup && mv apuntes.txt ~/backup
```

**Paso 5.** Ejecuta y muestra:

```
less apuntes.txt
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Copiar con cp y sus variantes -r para carpetas».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel principiante a intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Termux desde Cero: Domina la terminal en tu Android (TERMUX-101), nivel principiante a intermedio, duración 4 semanas. El módulo 2 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
