# Módulo 8: Proyecto final (crear y desplegar un Bot de Telegram)

Curso: Termux desde Cero: Domina la terminal en tu Android · Nivel: principiante a intermedio

### Lección 1: Obtener el token y preparar el entorno

Los bots de Telegram se crean con BotFather, que entrega un token de API. En Termux se prepara el entorno: carpeta del proyecto, entorno virtual y dependencias con pip.

**Temas cubiertos**

- Crear el bot con BotFather y anotar el token
- Entorno virtual aislado para el proyecto
- Instalar la librería python-telegram-bot

**Ejercicios prácticos**

- Crea tu bot en BotFather y guarda el token en un lugar seguro.
- Deja el entorno virtual con la librería instalada.

**Recursos**

- Crear bots con BotFather

### Lección 2: Escribir el bot con nano

El bot escucha mensajes y responde. El script pide el token por variable de entorno, define un manejador de /start y otro de texto libre, y arranca con polling.

**Temas cubiertos**

- Estructura de un bot con python-telegram-bot
- Leer el token desde el entorno y no desde el código
- Probar el bot en Telegram

**Ejercicios prácticos**

- Completa bot.py con los manejadores /start y /ayuda.
- Ejecuta python bot.py y escribe a tu bot desde el teléfono.

**Recursos**

- Documentación de python-telegram-bot

### Lección 3: Desplegarlo en segundo plano y mantenerlo vivo

Un bot que se apaga cuando cierras la terminal no sirve de nada. nohup lo lanza en segundo plano ignorando señales, y termux-wake-lock impide que Android lo suspenda.

**Temas cubiertos**

- Lanzar en segundo plano con nohup y el operador &
- Impedir el suspenso de Android con termux-wake-lock
- Ver los registros y detener el proceso

**Ejercicios prácticos**

- Despliega tu bot con nohup y verifica que responde.
- Comprueba con tail -f que registra cada mensaje y deténlo al terminar.

**Recursos**

- Ejecutar procesos en segundo plano en Termux
