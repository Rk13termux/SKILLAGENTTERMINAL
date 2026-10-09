# Módulo 1: Configuración inicial y mitos de la Play Store

Curso: Termux desde Cero: Domina la terminal en tu Android · Nivel: principiante a intermedio

### Lección 1: Qué es Termux y por qué evitar la Play Store

Termux es un emulador de terminal para Android que trae una distribución Linux completa sin root. La versión de Google Play lleva años sin mantenimiento y se queda atascada en paquetes antiguos: hoy la vía recomendada es F-Droid o las compilaciones de GitHub.

**Temas cubiertos**

- Qué es Termux y qué puede hacer sin permisos de root
- El problema de la versión de la Play Store (abandonada)
- Instalar desde F-Droid o GitHub releases

**Ejercicios prácticos**

- Comprueba con termux-info la versión de Termux y de Android que usas.
- Confirma que pkg update y pkg upgrade terminan sin errores.

**Recursos**

- Guía oficial de instalación (F-Droid)

### Lección 2: Acceso al almacenamiento y primeros pasos

El comando termux-setup-storage concede a Termux permiso para leer y escribir en las carpetas compartidas de Android. Sin este paso, el terminal no ve fotos, descargas ni documentos.

**Temas cubiertos**

- La diferencia entre el almacenamiento interno de Termux y el de Android
- Conceder permisos con termux-setup-storage
- Localizar y verificar las carpetas compartidas

**Ejercicios prácticos**

- Ejecuta termux-setup-storage y acepta el diálogo de permisos de Android.
- Crea una carpeta de trabajo en el almacenamiento compartido y verifícala con ls.

**Recursos**

- Documentación de termux-setup-storage
