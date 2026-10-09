# Video largo (Facebook / YouTube) — Lección 1

**Plan:** Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
**Módulo:** 2. Comandos esenciales de Linux (ls, cd, pwd, mkdir, rm)
**Lección:** 1. La jerarquía de directorios y el símbolo del sistema
**Duración estimada:** 3-8 minutos
**Audiencia:** principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular · **Nivel:** principiante a intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«El prompt y la carpeta personal (~)» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (La jerarquía de directorios y el símbolo del sistema) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular suelen bloquearse con El prompt y la carpeta personal (~) porque falta el orden de pasos. El prompt `~ $` indica que Termux está en la carpeta personal. La raíz del sistema Termux es `$PREFIX` (normalmente /data/data/com.termux/files/usr), no `/`. Saber dónde estás es el primer paso para no borrar nada por accidente. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: El prompt y la carpeta personal (~)

Explica «El prompt y la carpeta personal (~)» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: pwd para saber el directorio actual

Explica «pwd para saber el directorio actual» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: cd para cambiar de carpeta y volver con cd ~

Explica «cd para cambiar de carpeta y volver con cd ~» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
pwd
```

**Paso 2.** Ejecuta y muestra:

```
echo $HOME
```

**Paso 3.** Ejecuta y muestra:

```
cd /
```

**Paso 4.** Ejecuta y muestra:

```
ls
```

**Paso 5.** Ejecuta y muestra:

```
cd ~
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «El prompt y la carpeta personal (~)».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel principiante a intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Termux desde Cero: Domina la terminal en tu Android (TERMUX-101), nivel principiante a intermedio, duración 4 semanas. El módulo 2 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
