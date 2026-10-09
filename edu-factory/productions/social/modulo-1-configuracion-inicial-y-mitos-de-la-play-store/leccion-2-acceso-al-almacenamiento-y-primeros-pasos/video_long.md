# Video largo (Facebook / YouTube) — Lección 2

**Plan:** Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
**Módulo:** 1. Configuración inicial y mitos de la Play Store
**Lección:** 2. Acceso al almacenamiento y primeros pasos
**Duración estimada:** 3-8 minutos
**Audiencia:** principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular · **Nivel:** principiante a intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«La diferencia entre el almacenamiento interno de Termux y el de Android» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (Acceso al almacenamiento y primeros pasos) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular suelen bloquearse con La diferencia entre el almacenamiento interno de Termux y el de Android porque falta el orden de pasos. El comando termux-setup-storage concede a Termux permiso para leer y escribir en las carpetas compartidas de Android. Sin este paso, el terminal no ve fotos, descargas ni documentos. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: La diferencia entre el almacenamiento interno de Termux y el de Android

Explica «La diferencia entre el almacenamiento interno de Termux y el de Android» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Conceder permisos con termux-setup-storage

Explica «Conceder permisos con termux-setup-storage» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Localizar y verificar las carpetas compartidas

Explica «Localizar y verificar las carpetas compartidas» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
termux-setup-storage
```

**Paso 2.** Ejecuta y muestra:

```
ls ~/storage/shared
```

**Paso 3.** Ejecuta y muestra:

```
termux-change-repo
```

**Paso 4.** Ejecuta y muestra:

```
pwd
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «La diferencia entre el almacenamiento interno de Termux y el de Android».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel principiante a intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Termux desde Cero: Domina la terminal en tu Android (TERMUX-101), nivel principiante a intermedio, duración 4 semanas. El módulo 1 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
