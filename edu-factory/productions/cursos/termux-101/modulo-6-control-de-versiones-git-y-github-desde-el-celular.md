# Módulo 6: Control de versiones (Git y GitHub desde el celular)

Curso: Termux desde Cero: Domina la terminal en tu Android · Nivel: principiante a intermedio

### Lección 1: El ciclo de trabajo de Git: commit y log

El flujo diario es ver (git status), preparar (git add) y guardar (git commit). git log registra la historia y git diff muestra qué cambió antes de confirmar.

**Temas cubiertos**

- El ciclo status > add > commit
- Mensajes de commit claros
- Leer el historial con git log

**Ejercicios prácticos**

- Crea dos commits con mensajes distintos sobre el mismo proyecto.
- Revisa el historial con git log --oneline y explícalo en voz alta.

**Recursos**

- Conceptos básicos de Git

### Lección 2: Conectar con GitHub: clave SSH y primer push

Con una clave SSH (ed25519), git habla con GitHub sin contraseña. La clave se copia en GitHub y luego el repositorio remoto se enlaza con git remote add.

**Temas cubiertos**

- Generar una clave con ssh-keygen
- Añadir la clave pública a GitHub
- Enlazar, publicar (push) y descargar (clone)

**Ejercicios prácticos**

- Genera tu clave, cópiala en GitHub y haz tu primer push.
- Clona el repositorio en otra carpeta y comprueba git log.

**Recursos**

- Conexión de GitHub con SSH

### Lección 3: Ramas y gestión de cambios remotos

Las ramas permiten trabajar sin romper la versión estable: se crea una rama, se comprueba con git branch, se publica y se fusiona con merge.

**Temas cubiertos**

- Crear y cambiar de rama
- Publicar una rama nueva
- Fusionar cambios con merge

**Ejercicios prácticos**

- Crea una rama, haz un cambio y fúndela en main.
- Publica el resultado y compara en GitHub.

**Recursos**

- Flujo de trabajo con ramas
