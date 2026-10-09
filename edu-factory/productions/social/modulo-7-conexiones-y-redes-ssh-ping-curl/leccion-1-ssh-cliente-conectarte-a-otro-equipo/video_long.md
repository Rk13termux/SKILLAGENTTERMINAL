# Video largo (Facebook / YouTube) — Lección 1

**Plan:** Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
**Módulo:** 7. Conexiones y redes (SSH, ping, curl)
**Lección:** 1. SSH cliente: conectarte a otro equipo
**Duración estimada:** 3-8 minutos
**Audiencia:** principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular · **Nivel:** principiante a intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Conexión básica con ssh usuario@host» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (SSH cliente: conectarte a otro equipo) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular suelen bloquearse con Conexión básica con ssh usuario@host porque falta el orden de pasos. ssh abre una sesión remota segura. Con la clave que ya generaste puede funcionar sin contraseña añadiéndola a las autorizadas del equipo remoto con ssh-copy-id. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Conexión básica con ssh usuario@host

Explica «Conexión básica con ssh usuario@host» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Añadir tu clave para entrar sin contraseña

Explica «Añadir tu clave para entrar sin contraseña» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Trabajar dentro de la sesión remota

Explica «Trabajar dentro de la sesión remota» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
pkg install openssh
```

**Paso 2.** Ejecuta y muestra:

```
ssh usuario@192.168.1.10
```

**Paso 3.** Ejecuta y muestra:

```
ssh-copy-id usuario@192.168.1.10
```

**Paso 4.** Ejecuta y muestra:

```
ssh -p 8022 usuario@servidor.com
```

**Paso 5.** Ejecuta y muestra:

```
exit
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Conexión básica con ssh usuario@host».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel principiante a intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Termux desde Cero: Domina la terminal en tu Android (TERMUX-101), nivel principiante a intermedio, duración 4 semanas. El módulo 7 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
