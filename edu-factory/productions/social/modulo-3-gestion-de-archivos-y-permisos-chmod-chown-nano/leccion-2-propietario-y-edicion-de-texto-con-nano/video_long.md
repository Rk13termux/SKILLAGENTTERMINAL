# Video largo (Facebook / YouTube) — Lección 2

**Plan:** Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
**Módulo:** 3. Gestión de archivos y permisos (chmod, chown, nano)
**Lección:** 2. Propietario y edición de texto con nano
**Duración estimada:** 3-8 minutos
**Audiencia:** principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular · **Nivel:** principiante a intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Qué es el propietario y para qué sirve chown» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (Propietario y edición de texto con nano) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular suelen bloquearse con Qué es el propietario y para qué sirve chown porque falta el orden de pasos. chown cambia el propietario de un archivo y en Termux resulta útil al operar con archivos del almacenamiento compartido. nano es el editor más amigable para empezar: abre, edita y guarda sin aprender vi. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Qué es el propietario y para qué sirve chown

Explica «Qué es el propietario y para qué sirve chown» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Abrir, editar y guardar con nano

Explica «Abrir, editar y guardar con nano» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Atajos: Ctrl-O guardar y Ctrl-X salir

Explica «Atajos: Ctrl-O guardar y Ctrl-X salir» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
pkg install nano
```

**Paso 2.** Ejecuta y muestra:

```
nano notas.txt
```

**Paso 3.** Ejecuta y muestra:

```
chown $(id -u):$(id -g) notas.txt
```

**Paso 4.** Ejecuta y muestra:

```
ls -l ~/storage/shared
```

**Paso 5.** Ejecuta y muestra:

```
file notas.txt
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Qué es el propietario y para qué sirve chown».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel principiante a intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Termux desde Cero: Domina la terminal en tu Android (TERMUX-101), nivel principiante a intermedio, duración 4 semanas. El módulo 3 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
