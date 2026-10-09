# Video largo (Facebook / YouTube) — Lección 2

**Plan:** Termux desde Cero: Domina la terminal en tu Android (TERMUX-101)
**Módulo:** 6. Control de versiones (Git y GitHub desde el celular)
**Lección:** 2. Conectar con GitHub: clave SSH y primer push
**Duración estimada:** 3-8 minutos
**Audiencia:** principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular · **Nivel:** principiante a intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Generar una clave con ssh-keygen» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (Conectar con GitHub: clave SSH y primer push) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular suelen bloquearse con Generar una clave con ssh-keygen porque falta el orden de pasos. Con una clave SSH (ed25519), git habla con GitHub sin contraseña. La clave se copia en GitHub y luego el repositorio remoto se enlaza con git remote add. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Generar una clave con ssh-keygen

Explica «Generar una clave con ssh-keygen» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Añadir la clave pública a GitHub

Explica «Añadir la clave pública a GitHub» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Enlazar, publicar (push) y descargar (clone)

Explica «Enlazar, publicar (push) y descargar (clone)» en una frase, sin jerga innecesaria. Conéctalo con un caso que principiantes absolutos, estudiantes y entusiastas de la tecnología que quieren programar desde su celular reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
pkg install openssh
```

**Paso 2.** Ejecuta y muestra:

```
ssh-keygen -t ed25519 -C "tu@correo.com"
```

**Paso 3.** Ejecuta y muestra:

```
cat ~/.ssh/id_ed25519.pub
```

**Paso 4.** Ejecuta y muestra:

```
git remote add origin git@github.com:usuario/repositorio.git
```

**Paso 5.** Ejecuta y muestra:

```
git branch -M main
```

**Paso 6.** Ejecuta y muestra:

```
git push -u origin main
```

**Paso 7.** Ejecuta y muestra:

```
git clone git@github.com:usuario/repositorio.git
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Generar una clave con ssh-keygen».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel principiante a intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Termux desde Cero: Domina la terminal en tu Android (TERMUX-101), nivel principiante a intermedio, duración 4 semanas. El módulo 6 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
