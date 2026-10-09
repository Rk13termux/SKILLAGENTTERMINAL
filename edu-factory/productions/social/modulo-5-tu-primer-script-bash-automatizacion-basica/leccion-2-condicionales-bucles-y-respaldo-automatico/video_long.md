# Video largo (Facebook / YouTube) — Lección 2

**Plan:** Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
**Módulo:** 5. Tu primer script Bash (automatización básica)
**Lección:** 2. Condicionales, bucles y respaldo automático
**Duración estimada:** 3-8 minutos
**Audiencia:** principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular · **Nivel:** principiante a intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Condicional if y comparaciones de archivo» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (Condicionales, bucles y respaldo automático) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular suelen bloquearse con Condicional if y comparaciones de archivo porque falta el orden de pasos. Con if, for, y variables posicionales ($1, $2) pasas de mostrar mensajes a resolver tareas: comprobar si existe una carpeta, recorrer archivos y guardar respaldos con fecha. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Condicional if y comparaciones de archivo

Explica «Condicional if y comparaciones de archivo» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Bucle for sobre listas de archivos

Explica «Bucle for sobre listas de archivos» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Respaldos con marca de fecha

Explica «Respaldos con marca de fecha» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
echo 'for archivo in *.sh; do echo "$archivo"; done' >> ~/bin/listar.sh
```

**Paso 2.** Ejecuta y muestra:

```
chmod +x ~/bin/listar.sh
```

**Paso 3.** Ejecuta y muestra:

```
mkdir -p ~/backups
```

**Paso 4.** Ejecuta y muestra:

```
echo 'cp notas.txt ~/backups/notas-$(date +%Y%m%d).txt' >> ~/bin/respaldar.sh
```

**Paso 5.** Ejecuta y muestra:

```
chmod +x ~/bin/respaldar.sh
```

**Paso 6.** Ejecuta y muestra:

```
~/bin/respaldar.sh
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Condicional if y comparaciones de archivo».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel principiante a intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Termux desde Cero: Domina la terminal en tu Android (TERMUX-101), nivel principiante a intermedio, duración 4 semanas. El módulo 5 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
