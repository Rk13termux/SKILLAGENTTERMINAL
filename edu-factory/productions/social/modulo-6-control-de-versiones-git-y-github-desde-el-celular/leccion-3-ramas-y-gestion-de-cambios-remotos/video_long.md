# Video largo (Facebook / YouTube) — Lección 3

**Plan:** Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
**Módulo:** 6. Control de versiones (Git y GitHub desde el celular)
**Lección:** 3. Ramas y gestión de cambios remotos
**Duración estimada:** 3-8 minutos
**Audiencia:** principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular · **Nivel:** principiante a intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Crear y cambiar de rama» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (Ramas y gestión de cambios remotos) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular suelen bloquearse con Crear y cambiar de rama porque falta el orden de pasos. Las ramas permiten trabajar sin romper la versión estable: se crea una rama, se comprueba con git branch, se publica y se fusiona con merge. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Crear y cambiar de rama

Explica «Crear y cambiar de rama» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Publicar una rama nueva

Explica «Publicar una rama nueva» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Fusionar cambios con merge

Explica «Fusionar cambios con merge» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
git branch readme
```

**Paso 2.** Ejecuta y muestra:

```
git checkout readme
```

**Paso 3.** Ejecuta y muestra:

```
git add . && git commit -m "Mejora el readme"
```

**Paso 4.** Ejecuta y muestra:

```
git checkout main
```

**Paso 5.** Ejecuta y muestra:

```
git merge readme
```

**Paso 6.** Ejecuta y muestra:

```
git push
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Crear y cambiar de rama».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel principiante a intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Termux desde Cero: Domina la terminal en tu Android (TERMUX-101), nivel principiante a intermedio, duración 4 semanas. El módulo 6 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
