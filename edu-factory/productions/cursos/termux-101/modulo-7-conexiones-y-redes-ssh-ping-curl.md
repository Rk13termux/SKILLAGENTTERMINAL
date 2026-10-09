# Módulo 7: Conexiones y redes (SSH, ping, curl)

Curso: Termux desde Cero: Domina la terminal en tu Android · Nivel: principiante a intermedio

### Lección 1: SSH cliente: conectarte a otro equipo

ssh abre una sesión remota segura. Con la clave que ya generaste puede funcionar sin contraseña añadiéndola a las autorizadas del equipo remoto con ssh-copy-id.

**Temas cubiertos**

- Conexión básica con ssh usuario@host
- Añadir tu clave para entrar sin contraseña
- Trabajar dentro de la sesión remota

**Ejercicios prácticos**

- Conecta a un equipo de prueba y revisa pwd en la sesión remota.
- Configura la autenticación por clave con ssh-copy-id.

**Recursos**

- Manual de OpenSSH

### Lección 2: Diagnosticar la red con ping y curl

ping comprueba si un host responde midiendo latencia, y curl hace peticiones HTTP. El trío ping, curl -I y curl -v da una imagen de si el problema es la red o el servidor.

**Temas cubiertos**

- Medir la conectividad con ping -c
- Ver cabeceras HTTP con curl -I
- Depurar con curl -v y --max-time

**Ejercicios prácticos**

- Diagnostica tu conexión haciendo ping a 1.1.1.1.
- Compara la salida de curl -I frente a curl -v para entender los tiempos.

**Recursos**

- Manual de curl

### Lección 3: El servidor SSH de Termux (sshd)

Termux puede servir como servidor: con sshd cualquiera con tu IP y contraseña se conecta a tu teléfono. Se levanta bajo demanda y se detiene cuando ya no se necesita.

**Temas cubiertos**

- Arrancar el daemon con sshd
- Conocer tu IP local con ifconfig o ip addr
- Detener el servicio con pkill sshd

**Ejercicios prácticos**

- Levanta sshd, localiza tu IP y conéctate desde otro dispositivo.
- Termina la sesión del servidor con pkill sshd.

**Recursos**

- OpenSSH en Termux (wiki)
