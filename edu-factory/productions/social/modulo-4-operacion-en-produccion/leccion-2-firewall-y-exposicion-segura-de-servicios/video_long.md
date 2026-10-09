# Video largo (Facebook / YouTube) — Lección 2

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 4. Operación en producción
**Lección:** 2. Firewall y exposición segura de servicios
**Duración estimada:** 3-8 minutos
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Intro (0:00 - 0:30)

**Gancho:**
«Estado del firewall y zonas con firewall-cmd» es lo que separa un resultado reproducible de uno que depende de la suerte. En esta lección (Firewall y exposición segura de servicios) lo vemos completo, con el proceso en pantalla.

**Presentación del problema:**
Problema real: desarrolladores y administradores de sistemas que quieren usar contenedores en Linux suelen bloquearse con Estado del firewall y zonas con firewall-cmd porque falta el orden de pasos. Publicar un puerto en Podman no siempre basta: firewalld puede bloquear el acceso desde la red. Conocer las zonas, los servicios y los puertos abiertos permite exponer solo lo necesario y cerrar todo lo demás. Hoy cerramos ese hueco en pocos minutos.

## Desarrollo teórico (2-3 conceptos clave)

### Concepto 1: Estado del firewall y zonas con firewall-cmd

Explica «Estado del firewall y zonas con firewall-cmd» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 2: Consultar servicios y puertos ya abiertos

Explica «Consultar servicios y puertos ya abiertos» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

### Concepto 3: Abrir y cerrar puertos de forma permanente con --permanent y --reload

Explica «Abrir y cerrar puertos de forma permanente con --permanent y --reload» en una frase, sin jerga innecesaria. Conéctalo con un caso que desarrolladores y administradores de sistemas que quieren usar contenedores en Linux reconozca al instante. Muestra un ejemplo mínimo en pantalla y cierra con una frase que enlace al siguiente concepto.

Tema extra (si el tiempo lo permite): Zona public frente a interfaces concretas y buenas prácticas de exposición.

## Demostración práctica paso a paso

**Paso 1.** Ejecuta y muestra:

```
firewall-cmd --state
```

**Paso 2.** Ejecuta y muestra:

```
firewall-cmd --get-default-zone
```

**Paso 3.** Ejecuta y muestra:

```
firewall-cmd --list-services
```

**Paso 4.** Ejecuta y muestra:

```
firewall-cmd --list-ports
```

**Paso 5.** Ejecuta y muestra:

```
firewall-cmd --list-all
```

**Paso 6.** Ejecuta y muestra:

```
ss -tln
```

**Verificación.** Compara el resultado en pantalla con el esperado antes de avanzar.

## Errores comunes y cómo evitarlos

- **Saltarse «Estado del firewall y zonas con firewall-cmd».** Sin ese punto, el resto del proceso falla de forma silenciosa. Verifícalo antes de continuar.
- **Copiar comandos sin leerlos.** Revisa cada opción antes de ejecutar: un parámetro mal puesto cambia el resultado.
- **Practicar una sola vez.** En un nivel intermedio el proceso se consolida repitiéndolo hasta que salga sin guion.

## CTA al curso

«Esta lección es parte de Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01), nivel intermedio, duración 2 semanas. El módulo 4 completo, con ejercicios y revisión, está en el curso. Enlace en el perfil».
