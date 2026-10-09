# Módulo 3: Gestión de archivos y permisos (chmod, chown, nano)

Curso: Termux desde Cero: Domina la terminal en tu Android · Nivel: principiante a intermedio

### Lección 1: Permisos de Linux y chmod

Cada archivo tiene permisos de lectura, escritura y ejecución para su dueño, su grupo y los demás. chmod (léase "change mode") los cambia; la forma con números, como 755, es la más legible.

**Temas cubiertos**

- Leer permisos con ls -l
- Cifras: 4 lectura, 2 escritura, 1 ejecución
- chmod 755 y chmod +x en la práctica

**Ejercicios prácticos**

- Crea script.sh vacío y hazlo ejecutable con chmod +x.
- Cambia permisos a 644 y observa el cambio en ls -l.

**Recursos**

- Guía de permisos de Linux en Termux

### Lección 2: Propietario y edición de texto con nano

chown cambia el propietario de un archivo y en Termux resulta útil al operar con archivos del almacenamiento compartido. nano es el editor más amigable para empezar: abre, edita y guarda sin aprender vi.

**Temas cubiertos**

- Qué es el propietario y para qué sirve chown
- Abrir, editar y guardar con nano
- Atajos: Ctrl-O guardar y Ctrl-X salir

**Ejercicios prácticos**

- Escribe tres líneas en nano y guárdalas con Ctrl-O y Ctrl-X.
- Comprueba qué propietario tiene un archivo recién creado con ls -l.

**Recursos**

- Manual de nano
