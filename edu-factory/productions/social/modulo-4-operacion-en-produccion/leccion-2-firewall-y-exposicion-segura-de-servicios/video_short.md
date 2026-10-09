# Video corto (TikTok / Reels / Shorts) — Lección 2

**Plan:** Podman en Fedora: contenedores sin Docker (PODMAN-FEDORA-01)
**Módulo:** 4. Operación en producción
**Lección:** 2. Firewall y exposición segura de servicios
**Duración máxima:** 60 segundos
**Audiencia:** desarrolladores y administradores de sistemas que quieren usar contenedores en Linux · **Nivel:** intermedio

## Guion con marcas de tiempo

### [0:00-0:03] GANCHO
- **Texto en pantalla:** «Estado del firewall y zonas con firewall-cmd» paso a paso, sin relleno (lección 2).
- **Hook visual:** Plano de pantalla ejecutando el primer comando: `firewall-cmd --state`. Sin zoom lento: el resultado debe verse desde el primer segundo.

### [0:03-0:15] CONTEXTO
Qué se resuelve: Estado del firewall y zonas con firewall-cmd. Publicar un puerto en Podman no siempre basta: firewalld puede bloquear el acceso desde la red. Conocer las zonas, los servicios y los puertos abiertos permite exponer solo lo necesario y cerrar todo lo demás. Plantea el problema en una frase y di que el comando o el proceso de la lección lo cierra.

### [0:15-0:45] DEMO
1. Ejecuta en pantalla `firewall-cmd --state` y comenta en voz alta qué hace cada parte.
2. Ejecuta en pantalla `firewall-cmd --get-default-zone` y comenta en voz alta qué hace cada parte.
3. Ejecuta en pantalla `firewall-cmd --list-services` y comenta en voz alta qué hace cada parte.
4. Menciona que hay 6 comandos en total y que el resto está en el material del curso.

### [0:45-0:55] RESULTADO
Cierre en pantalla: resultado correcto de «Estado del firewall y zonas con firewall-cmd» visible. Frase final: «esto es lo que hace falta para estado del firewall y zonas con firewall-cmd; el resto es práctica».

### [0:55-1:00] CTA
«Guarda este video y practica esto hoy: Abre temporalmente el puerto 8080 con sudo firewall-cmd --add-port=8080/tcp y ciérralo después. Sígueme para el siguiente paso de Podman en Fedora: contenedores sin Docker».

## Voz en off (texto plano para Edge-TTS, ~130 palabras)

Lección 2 del módulo 4 de Podman en Fedora: contenedores sin Docker. Publicar un puerto en Podman no siempre basta: firewalld puede bloquear el acceso desde la red. Conocer las zonas, los servicios y los puertos abiertos permite exponer solo lo necesario y cerrar todo lo demás. Primero vemos Estado del firewall y zonas con firewall-cmd, Consultar servicios y puertos ya abiertos, Abrir y cerrar puertos de forma permanente con --permanent y --reload y después Zona public frente a interfaces concretas y buenas prácticas de exposición. En pantalla ejecuto 6 comandos, empezando por `firewall-cmd --state`. Observa qué cambia antes y después. El resultado debe verse completo antes de cerrar; si algo falla, revisa el mensaje de error en lugar de repetir a ciegas. Para practicar: Abre temporalmente el puerto 8080 con sudo firewall-cmd --add-port=8080/tcp y ciérralo después. En el material de Podman en Fedora: contenedores

## Hashtags

#estadodelfirewallyzonasconfirewallcmd #estado #firewall #zonas #firewallcmd #consultarserviciosypuertosyaabiertos #consultar #servicios #puertos #abiertos #abrirycerrarpuertosdeformapermanenteconpermanentyreload #abrir #cerrar #forma
