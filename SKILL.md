---
name: edu-factory
description: Genera contenido educativo completo (guiones para redes sociales, material de curso y scripts autoejecutables de grabación de terminal) a partir de un solo archivo maestro de lecciones en Markdown. Usar cuando el usuario quiera crear cursos, guiones de video, posts, temarios o grabaciones tutorrec desde un plan de estudios. Pásale el tema/plan o una ruta a un master-lesson.md.
---

# Edu-Factory

Fábrica de contenido educativo: lee un `master-lesson.md` (plan de estudios)
y produce tres familias de salida:

1. **Social** — guiones TikTok/Reels/Shorts (60 s), video largo FB/YT (3-8 min)
   y post estático IG/LinkedIn + primer comentario, con voz en off para Edge-TTS
   y hashtags.
2. **Curso** — temario, objetivos y una unidad por módulo en Markdown.
3. **Director** — por lección genera `tutorrec.py` (modo demo, simula el output)
   y `tutorrec_real.py` (modo real, ejecuta los comandos): escriben los comandos
   con velocidad humana variable, limpian la pantalla entre pasos y producen
   output realista para grabar pantalla como un programador real. Motor
   cinematográfico en `tutorrec/` (solo stdlib, compatible con Termux y Fedora).

## Ubicación del proyecto

`/home/RK13/RK13/SKILLAGENTERMUX/edu-factory/`

- `edu_factory.py` — CLI orquestador
- `curriculum/` — planes de entrada (`.md`)
- `productions/` — salidas generadas
- `templates/` — plantillas de los agentes
- `core/parser.py` — lee y valida el master-lesson
- `agents/social_agent.py`, `agents/course_agent.py`, `agents/director_agent.py`
- `tutorrec/` — motor cinematográfico:
  - `cinematic.py` — clase `CinematicTerminal` (demo/real, pausas, limpieza)
  - `human_typing.py` — escritura humana variable
  - `output_simulator.py` — output realista por tipo de comando
  - `cli.py` — CLI de pruebas (`python3 -m tutorrec.cli`)
  - `sequences/` — secuencias de ejemplo (termux, git, python)

## Formato del master-lesson.md

```markdown
# Título del curso

## Metadata
- id: MI-CURSO-01
- nivel: inicial
- duracion: 4 semanas
- audiencia: diseñadores
- idioma: español            # opcional

## Objetivos
- Objetivo 1
- Objetivo 2

## Módulo 1: Nombre del módulo

### Lección 1: Nombre de la lección

**Resumen:** Una o dos frases sobre la lección.

**Temas:**
- Tema 1
- Tema 2

**Comandos:**              # opcional; habilita el tutorrec.py del Director
- comando real exacto

**Ejercicios:**            # opcional
- Ejercicio 1

**Recursos:**              # opcional
- Recurso 1
```

Reglas de validación:

- Obligatorio: `Metadata` con `id`, `nivel`, `duracion`, `audiencia`; al menos
  1 objetivo, 1 módulo; cada lección con `Resumen` y al menos 1 `Temas`.
- `Comandos`, `Ejercicios`, `Recursos` opcionales.
- Lecciones sin `Comandos:` no generan tutorrec (el índice lo avisa).
- Los comandos se inyectan literales: `$USER`, `$(...)`, `"` y `&&` son seguros.
- Los comandos del plan deben ser reales y verificables para poder grabarse sin errores.

## Flujo de trabajo

1. Si el usuario da un tema (sin plan), propón/crea tú el `master-lesson.md`
   siguiendo el formato de arriba en `curriculum/master-lesson-<slug>.md`,
   con comandos reales y verificables en cada lección.
2. Valida:

   ```bash
   python3 edu_factory.py validate curriculum/master-lesson-<slug>.md
   ```

3. Genera todo:

   ```bash
   python3 edu_factory.py all curriculum/master-lesson-<slug>.md -s productions
   ```

   O por agente: `social`, `course`, `director`.

4. Informa las rutas de salida dentro de `productions/` y deja lista la próxima
   acción (grabar con `tutorrec.py`, grabar voz en off, etc.).

## Salidas por lección

- `productions/social/modulo-N-*/leccion-M-*/video_short.md`
- `productions/social/.../video_long.md`
- `productions/social/.../post_static.md`
- `productions/cursos/<slug>/temario.md` + `modulo-N-*.md`
- `productions/direccion/modulo-N-*/leccion-M-*/tutorrec.py` (demo)
- `productions/direccion/.../tutorrec_real.py` (real)

## Tutorrec cinematográfico (grabación)

El director simula un programador real en la terminal:

- **Tecleo humano**: velocidad base 0.12 s/carácter (~8 letras/s, rango ±50%) con
  pausas extendidas en espacios, puntuación y saltos de línea; pausa "pensando" antes
  de cada comando y pausa post‑Enter. Ajustable con `--velocidad <s>` o
  `TUTORREC_VELOCIDAD`. Por defecto **solo se ve el comando y su
  salida** (sin línea de explicación); añade `--mostrar-descripcion` para ver
  la descripción de cada paso.
- **Limpieza**: la pantalla se limpia entre comandos (ANSI en Termux/Fedora/macOS,
  `cls` en Windows). Se omite automáticamente si stdout no es un TTY o con
  `TUTORREC_NO_LIMPIAR=1`.
- **Output realista**: en modo demo, `output_simulator` genera salida creíble
  según el comando (`pkg`, `git`, `termux-info`, `python --version`, `npm`,
  `ping`, `echo`, etc.). En modo real, los comandos se ejecutan de verdad.
- **Colores**: paleta ANSI con `NO_COLOR`/`TUTORREC_NO_COLOR` para texto plano.
- **Prompt real**: por defecto muestra el prompt del usuario real de la máquina
  (`usuario@hostname:carpeta$`), tomado de `LOGNAME`/`USER`, `socket.gethostname()`
  y el directorio actual. Se actualiza en cada `cd` para que parezca una
  terminal abierta de verdad. Opcional: `--prompt <texto>` o `TUTORREC_PROMPT`.
- **Bienvenida Termux**: opcional, desactivada por defecto. Añade `--banner`/
  `TUTORREC_BANNER=1` para mostrar "Welcome to Termux!" al inicio (útil para
  grabaciones que simulen la app de Termux).

### Backend asciinema (terminal real)

El backend ANSI simula colores; el backend **asciinema** graba tu terminal REAL
(Powerlevel10k, zsh, íconos, plugins) en un archivo `.cast`:

- Abre tu shell interactiva real (`$SHELL -i`, con `.zshrc` completo) dentro de
  un PTY controlado (_stdlib_ puro, sin asciinema instalado) y envía cada
  comando como teclas reales con el mismo tecleo humano cinematográfico.
- El `.cast` es compatible con `asciinema` (reproduce con `asciinema play`;
  convierte a GIF con `agg` o a MP4 con ffmpeg). Solo necesitas esos binarios
  para reproducir/convertir, no para grabar.
- Los comandos se ejecutan de verdad (es tu shell real; `--modo` es
  irrelevante), la pantalla se limpia entre pasos (Ctrl+L) y el prompt cambia
  con cada `cd`.
- El `.cast` se guarda junto al script de la lección
  (`.../leccion-N.M.cast`) o en `--output <archivo>`; configurable con
  `--backend asciinema`, `TUTORREC_BACKEND=asciinema` y `TUTORREC_OUTPUT`.

Grabar una lección con la terminal real:

```bash
python3 edu_factory.py tutorrec curriculum/<plan>.md -l 1.2 -m demo --backend asciinema
```

Probar las secuencias de ejemplo:

```bash
python3 -m tutorrec.cli --secuencia termux --modo demo
python3 -m tutorrec.cli --secuencia git    --modo demo --velocidad 0.05
```

Grabar una lección del plan:

```bash
# listar lecciones con comandos
python3 edu_factory.py tutorrec curriculum/<plan>.md

# grabar una (demo simula output; real ejecuta)
python3 edu_factory.py tutorrec curriculum/<plan>.md -l 1.2 -m demo
python3 edu_factory.py tutorrec curriculum/<plan>.md -l 6.2 -m real
```

O lanzar el script directo:

```bash
python3 productions/direccion/modulo-N-*/leccion-M-*/tutorrec.py
```

Consejos de grabación: para generar el video, ejecuta el tutorrec con la
grabadora de pantalla (o `asciinema`) activa; usa modo `real` solo si quieres
que los comandos se ejecuten en el dispositivo (prueba primero en demo).

## Notas

- No modifiques el código del proyecto salvo que el usuario lo pida.
- Escribe todo contenido (guiones, copy, resúmenes) en español neutro, sin
  regionalismos y sin voseo.
- Tono de los guiones: autoridad didáctica, serena, técnica. Prohibido clickbait
  engañoso o promesas vacías; los comandos/ejemplos deben ser reales.
- Aunque la skill se invoque desde cualquier carpeta, ejecuta los comandos con
  `workdir` = ruta del proyecto para que las rutas relativas funcionen.