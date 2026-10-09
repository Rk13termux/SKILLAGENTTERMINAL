# Video largo (Facebook / YouTube) — Lección 1

**Plan:** Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
**Módulo:** 5. Tu primer script Bash (automatización básica)
**Lección:** 1. Estructura de un script Bash
**Duración estimada:** 3-8 minutos
**Audiencia:** principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular · **Nivel:** principiante a intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«El shebang de Termux y por qué difiere de Linux normal» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (Estructura de un script Bash) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular suelen bloquearse con El shebang de Termux y por qué difiere de Linux normal porque falta el orden de pasos. Un script es un archivo con la línea `#!/data/data/com.termux/files/usr/bin/bash` en la primera línea, comandos en las siguientes y permisos de ejecución. Crearlo en ~/bin permite ejecutarlo como un comando más. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: El shebang de Termux y por qué difiere de Linux normal

Explica «El shebang de Termux y por qué difiere de Linux normal» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Variables y echo

Explica «Variables y echo» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Hacer un script ejecutable

Explica «Hacer un script ejecutable» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
mkdir -p ~/bin
```

**Paso 2.** Ejecuta y muestra:

```
echo '#!/data/data/com.termux/files/usr/bin/bash' > ~/bin/mi-script.sh
```

**Paso 3.** Ejecuta y muestra:

```
echo 'echo "Hola desde Termux"' >> ~/bin/mi-script.sh
```

**Paso 4.** Ejecuta y muestra:

```
chmod +x ~/bin/mi-script.sh
```

**Paso 5.** Ejecuta y muestra:

```
~/bin/mi-script.sh
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «El shebang de Termux y por qué difiere de Linux normal».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel principiante a intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Termux desde Cero: Domina la terminal en tu Android (TERMUX-101), nivel principiante a intermedio, duración 4 semanas. El módulo 5 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
