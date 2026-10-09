# Control de versiones con Git — Ejemplo técnico

## Metadata
- id: DEV-042
- nivel: inicial
- duracion: 2 semanas
- audiencia: desarrolladores que empiezan con control de versiones
- idioma: español

## Objetivos
- Entender qué resuelve el control de versiones en un equipo.
- Ejecutar el flujo diario de Git sin miedo a perder trabajo.

## Módulo 1: Flujo diario de Git

### Lección 1: Estado, área de preparación y commit

**Resumen:** El ciclo ver → preparar → guardar es la base de todo trabajo con Git: mirar el estado, seleccionar cambios y registrarlos con un mensaje claro.

**Temas:**
- Lectura de git status
- Qué va al área de preparación y qué no
- Mensajes de commit que el equipo entiende

**Comandos:**
- git status
- git add proyecto/notas.md
- git commit -m "Notas: corrige el ejemplo de instalacion"
- echo "Rama actual: $(git branch --show-current)"

**Ejercicios:**
- Haz dos commits con mensajes distintos sobre el mismo archivo.
- Lee el estado antes y después de cada operación y anota qué cambió.

**Recursos:**
- Documentación oficial de git-status

### Lección 2: Historial y recuperación

**Resumen:** git log y git restore permiten auditar qué cambió y deshacer sin pánico: el historial es el registro, no un archivo que se borra.

**Temas:**
- Historial legible con git log
- Diferencias entre restore y reset
- Recuperar un archivo descartado por accidente

**Comandos:**
- git log --oneline -5
- git restore proyecto/notas.md
- echo "Último commit de $USER: $(git log -1 --pretty=%s)"

**Ejercicios:**
- Descarta un archivo por error y recupéralo desde el historial.
- Explica con tus palabras la diferencia entre restore y reset.

**Recursos:**
- Documentación oficial de git-log
