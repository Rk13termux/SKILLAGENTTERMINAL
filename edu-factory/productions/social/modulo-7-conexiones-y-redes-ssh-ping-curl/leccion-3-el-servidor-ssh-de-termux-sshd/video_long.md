# Video largo (Facebook / YouTube) — Lección 3

**Plan:** Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
**Módulo:** 7. Conexiones y redes (SSH, ping, curl)
**Lección:** 3. El servidor SSH de Termux (sshd)
**Duración estimada:** 3-8 minutos
**Audiencia:** principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular · **Nivel:** principiante a intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Arrancar el daemon con sshd» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (El servidor SSH de Termux (sshd)) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular suelen bloquearse con Arrancar el daemon con sshd porque falta el orden de pasos. Termux puede servir como servidor: con sshd cualquiera con tu IP y contraseña se conecta a tu teléfono. Se levanta bajo demanda y se detiene cuando ya no se necesita. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Arrancar el daemon con sshd

Explica «Arrancar el daemon con sshd» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Conocer tu IP local con ifconfig o ip addr

Explica «Conocer tu IP local con ifconfig o ip addr» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Detener el servicio con pkill sshd

Explica «Detener el servicio con pkill sshd» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
pkg install openssh
```

**Paso 2.** Ejecuta y muestra:

```
sshd
```

**Paso 3.** Ejecuta y muestra:

```
ip addr
```

**Paso 4.** Ejecuta y muestra:

```
whoami
```

**Paso 5.** Ejecuta y muestra:

```
pkill sshd
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Arrancar el daemon con sshd».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel principiante a intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Termux desde Cero: Domina la terminal en tu Android (TERMUX-101), nivel principiante a intermedio, duración 4 semanas. El módulo 7 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
