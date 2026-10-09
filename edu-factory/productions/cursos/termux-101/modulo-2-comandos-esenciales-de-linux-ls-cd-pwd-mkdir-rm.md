# Módulo 2: Comandos esenciales de Linux (ls, cd, pwd, mkdir, rm)

Curso: Termux desde Cero: Domina la terminal en tu Android · Nivel: principiante a intermedio

### Lección 1: La jerarquía de directorios y el símbolo del sistema

El prompt `~ $` indica que Termux está en la carpeta personal. La raíz del sistema Termux es `$PREFIX` (normalmente /data/data/com.termux/files/usr), no `/`. Saber dónde estás es el primer paso para no borrar nada por accidente.

**Temas cubiertos**

- El prompt y la carpeta personal (~)
- pwd para saber el directorio actual
- cd para cambiar de carpeta y volver con cd ~

**Ejercicios prácticos**

- Recorre la jerarquía con cd y vuelve siempre a la carpeta personal con cd ~.
- Comprueba con pwd dónde estás en cada momento.

**Recursos**

- Referencia de comandos de Termux

### Lección 2: listar, crear y eliminar carpetas

ls lista, mkdir crea y rm elimina. Con esas tres herramientas se construye una estructura de proyectos, y con rm hay que actuar con cuidado porque no hay papelera.

**Temas cubiertos**

- Listar con ls, -l (detalle) y -a (ocultos)
- Crear carpetas con mkdir, también anidadas con -p
- Eliminar con rm y con rm -rf (usar con criterio)

**Ejercicios prácticos**

- Crea la estructura proyectos/cursos/python con mkdir -p.
- Lista el detalle con ls -la y elimina una prueba con rm.
- Haz una prueba con rm -rf en una carpeta que puedas borrar.

**Recursos**

- Manual de mkdir en la wiki de Termux

### Lección 3: mover, copiar y ver archivos

cp copia, mv mueve o renombra y cat muestra el contenido. Con estos comandos ya puedes organizar tus apuntes y tus scripts sin abrir un administrador de archivos.

**Temas cubiertos**

- Copiar con cp y sus variantes -r para carpetas
- Mover y renombrar con mv
- Ver archivos con cat y paginar con less

**Ejercicios prácticos**

- Crea un archivo, cópialo, renómbralo y muévelo a una carpeta backup.
- Abre un archivo con less y sal con q.

**Recursos**

- Referencia de cp y mv
