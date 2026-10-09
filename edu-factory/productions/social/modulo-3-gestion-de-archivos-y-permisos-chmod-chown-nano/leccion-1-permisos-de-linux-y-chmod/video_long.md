# Video largo (Facebook / YouTube) — Lección 1

**Plan:** Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
**Módulo:** 3. Gestión de archivos y permisos (chmod, chown, nano)
**Lección:** 1. Permisos de Linux y chmod
**Duración estimada:** 3-8 minutos
**Audiencia:** principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular · **Nivel:** principiante a intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Leer permisos con ls -l» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (Permisos de Linux y chmod) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular suelen bloquearse con Leer permisos con ls -l porque falta el orden de pasos. Cada archivo tiene permisos de lectura, escritura y ejecución para su dueño, su grupo y los demás. chmod (léase "change mode") los cambia; la forma con números, como 755, es la más legible. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Leer permisos con ls -l

Explica «Leer permisos con ls -l» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Cifras: 4 lectura, 2 escritura, 1 ejecución

Explica «Cifras: 4 lectura, 2 escritura, 1 ejecución» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: chmod 755 y chmod +x en la práctica

Explica «chmod 755 y chmod +x en la práctica» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
ls -l
```

**Paso 2.** Ejecuta y muestra:

```
chmod 644 notas.txt
```

**Paso 3.** Ejecuta y muestra:

```
chmod 755 script.sh
```

**Paso 4.** Ejecuta y muestra:

```
chmod +x script.sh
```

**Paso 5.** Ejecuta y muestra:

```
stat notas.txt
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Leer permisos con ls -l».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel principiante a intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Termux desde Cero: Domina la terminal en tu Android (TERMUX-101), nivel principiante a intermedio, duración 4 semanas. El módulo 3 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
