# Edu-Factory · Skill Agent Terminal

> Fábrica de contenido educativo a partir de un único plan maestro en Markdown.
> A partir de un `master-lesson.md` genera guiones para redes sociales, material
> de curso y **grabaciones cinematográficas de terminal** listas para reel.

[![Licencia](https://img.shields.io/badge/licencia-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-3776ab.svg)](https://www.python.org/)
[![Sin dependencias](https://img.shields.io/badge/solo-stdlib%20puro-2ea44f.svg)](#requisitos)
[![PRs bienvenidas](https://img.shields.io/badge/PRs-bienvenidas-brightgreen.svg)](https://github.com/Rk13termux/SKILLAGENTTERMINAL)

Edu-Factory es el motor que convierte una idea de curso en contenido publicado
y en vídeos de terminal tipo "programador en vivo", con un solo comando:

- **Guiones sociales**: TikTok/Reels/Shorts (60 s), vídeo largo Facebook/YouTube
  (3-8 min) y post estático Instagram/LinkedIn con primer comentario.
- **Material de curso**: temario, objetivos y una unidad por módulo en Markdown.
- **Grabación de terminal** (Director + motor `tutorrec`): escribe los comandos
  con velocidad humana variable, limpia la pantalla entre pasos y produce output
  realista, tanto simulándolo (demo) como ejecutándolo (real), o grabando tu
  terminal real a un `.cast` de asciinema compatible con `agg`/`ffmpeg`.

El proyecto funciona **solo con la librería estándar de Python** y es compatible
con Fedora, Termux, macOS y Windows.

---

## Contenido del repositorio

| Ruta | Descripción |
| --- | --- |
| `SKILL.md` | La skill instalable para agentes de IA (copia a `~/.claude/skills/edu-factory/`) |
| `edu-factory/` | El motor completo: CLI, agentes, plan de estudios y salidas |
| `edu-factory/curriculum/` | Planes maestros de entrada (`master-lesson-*.md`) |
| `edu-factory/productions/` | Salidas generadas (social, curso, dirección y grabaciones) |
| `edu-factory/templates/` | Plantillas de los agentes (`.tmpl`) |
| `edu-factory/tutorrec/` | Motor cinematográfico de grabación (stdlib puro) |

### Estructura del motor

```
edu-factory/
├── edu_factory.py            # CLI orquestador
├── agents/
│   ├── social_agent.py       # guiones + voz en off + hashtags
│   ├── course_agent.py       # temario y unidades del curso
│   └── director_agent.py     # tutorrec.py (demo y real) por lección
├── core/
│   └── parser.py             # lee y valida el master-lesson
├── curriculum/               # plan maestro (entrada)
├── productions/              # salidas generadas
├── templates/                # plantillas de los agentes
└── tutorrec/
    ├── cinematic.py          # CinematicTerminal (demo/real)
    ├── human_typing.py       # tecleo humano variable
    ├── output_simulator.py   # output realista por tipo de comando
    ├── cli.py                # pruebas: python3 -m tutorrec.cli
    ├── pty_recorder.py       # graba la terminal real a .cast
    └── sequences/            # secuencias de ejemplo (termux, git, python)
```

---

## Requisitos

- **Python 3.10+** (solo stdlib; no requiere `pip install`).
- Para el backend `asciinema` (reproducir/convertir, **no** para grabar):
  `asciinema` y `agg`, o `ffmpeg` para MP4.

Verifica que esté todo:

```bash
python3 --version
asciinema --version        # opcional
aggregate --version        # opcional (el agg real, 1.9+)
ffmpeg -version            # opcional
```

---

## Instalación

Clona y entra:

```bash
git clone https://github.com/Rk13termux/SKILLAGENTTERMINAL.git
cd SKILLAGENTTERMINAL
```

Para usar la **skill** con un agente (Claude/Claude Code/opencode):

```bash
mkdir -p ~/.claude/skills/edu-factory
cp SKILL.md ~/.claude/skills/edu-factory/SKILL.md
```

---

## Cómo se usa

### 1. Plan maestro (`master-lesson.md`)

El formato de entrada es un único archivo Markdown con metadatos, objetivos,
módulos y lecciones:

```markdown
# Título del curso

## Metadata
- id: MI-CURSO-01
- nivel: inicial
- duracion: 4 semanas
- audiencia: diseñadores
- idioma: español          # opcional

## Objetivos
- Objetivo 1
- Objetivo 2

## Módulo 1: Nombre del módulo

### Lección 1: Nombre de la lección

**Resumen:** Una o dos frases sobre la lección.

**Temas:**
- Tema 1

**Comandos:**              # opcional; habilita el tutorrec del Director
- comando real exacto

**Ejercicios:**            # opcional
- Ejercicio 1

**Recursos:**              # opcional
- Recurso 1
```

Reglas de validación:

- Obligatorio: `Metadata` con `id`, `nivel`, `duracion`, `audiencia`; al menos
  1 objetivo y 1 módulo; cada lección con `Resumen` y al menos 1 `Temas`.
- `Comandos`, `Ejercicios` y `Recursos` son opcionales.
- Las lecciones **sin** `Comandos:` no generan tutorrec.
- Los comandos se inyectan literales: `$USER`, `$(...)`, `"` y `&&` son seguros.
- Los comandos deben ser **reales y verificables** para poder grabarse.

### 2. Validar el plan

```bash
python3 edu_factory.py validate curriculum/master-lesson-<slug>.md
```

### 3. Generar todo el contenido

```bash
python3 edu_factory.py all curriculum/master-lesson-<slug>.md -s productions
```

O por agente independiente:

```bash
python3 edu_factory.py social   curriculum/master-lesson-<slug>.md -s productions
python3 edu_factory.py course   curriculum/master-lesson-<slug>.md -s productions
python3 edu_factory.py director curriculum/master-lesson-<slug>.md -s productions
```

Salidas generadas:

- `productions/social/.../video_short.md`, `video_long.md`, `post_static.md`
- `productions/cursos/<slug>/temario.md` + `modulo-N-*.md`
- `productions/direccion/.../tutorrec.py` (demo) y `tutorrec_real.py` (real)

### 4. Grabar las lecciones (terminal real → reel)

El Director genera un script por lección que simula un programador real.
Grábalo con tu terminal real (p10k, zsh, plugins) al formato asciinema:

```bash
# listar lecciones con comandos
python3 edu_factory.py tutorrec curriculum/master-lesson-<slug>.md

# grabar una lección (demo simula el output; real lo ejecuta)
PROMPT_EOL_MARK='' python3 edu_factory.py tutorrec \
  curriculum/master-lesson-<slug>.md -l 1.1 -m demo --backend asciinema
```

> **`PROMPT_EOL_MARK=''`** elimina la marca `%` que zsh/imprime al final de
> líneas sin salto de línea: deja grabaciones limpias.

Probablemente quieras definir la velocidad de tecleo y el tamaño de terminal:

```bash
TUTORREC_VELOCIDAD=0.12 COLUMNS=80 LINES=60 \
  python3 edu_factory.py tutorrec curriculum/<plan>.md -l 1.1 -m demo --backend asciinema
```

El `.cast` se guarda junto a la lección (`productions/direccion/.../leccion-N.M.cast`).

### 5. Convertir a GIF / MP4 (formato reel 9:16)

```bash
# GIF vertical "reel" con fondo negro y letra grande (60 columnas)
agg --theme 000000,c9d1d9,484f58,ff7b72,3fb950,d29922,58a6ff,bc8cff,39c5cf,e6edf3,6e7681,ffa198,56d364,e3b341,79c0ff,d2a8ff,56d4dd,ffffff \
    --cols 60 --rows 46 leccion-1.1.cast leccion-1.1.gif

# MP4 1080×1920 (H.264) para TikTok/Reels/Shorts
ffmpeg -y -loglevel error -i leccion-1.1.gif \
  -vf "scale=1080:-2,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=black" \
  -c:v libopenh264 -b:v 2500k -pix_fmt yuv420p -movflags +faststart leccion-1.1.mp4
```

> Sin `libopenh264` usa `-c:v libx264`. El tamaño de letra en el reel lo
> determina el número de columnas: `--cols 80` ≈ letra estándar; `--cols 46`
> ≈ 170 %; `--cols 60` ≈ 135 % (buen equilibrio entre legibilidad y comandos
> completos).

### Modo `ansi` (sin grabación real)

Para ver la secuencia en el momento, sin abrir un PTY:

```bash
python3 edu_factory.py tutorrec curriculum/<plan>.md -l 1.1 -m demo --backend ansi
```

### Probar las secuencias de ejemplo

```bash
python3 -m tutorrec.cli --secuencia termux --modo demo
python3 -m tutorrec.cli --secuencia git    --modo demo --velocidad 0.05
```

---

## Agentes

| Agente | Qué genera |
| --- | --- |
| `social` (`SocialAgent`) | Guiones TikTok/Reels/Shorts (60 s), vídeo largo, post estático + comentario |
| `course` (`CourseAgent`) | Temario, objetivos y unidades Markdown por módulo |
| `director` (`DirectorAgent`) | Scripts `tutorrec.py`/`tutorrec_real.py` cinematográficos por lección |

---

## Cursos incluidos en `curriculum/`

| Plan | id | Enfoque |
| --- | --- | --- |
| `master-lesson-termux.md` | `TERMUX-101` | Termux en Android, de cero a bot de Telegram desplegado |
| `master-lesson-podman-fedora.md` | `PODMAN-FEDORA-01` | Podman en Fedora: fundamentos, imágenes, almacenamiento y producción |
| `master-lesson-devops.md` | — | Tema base de DevOps |
| `master-lesson.md` | — | Plan por defecto (editorial) |

---

## Notas de estilo

- Todo el contenido generado (guiones, copy, resúmenes) se escribe en **español
  neutro** (sin regionalismos ni voseo).
- Tono didáctico, sereno y técnico; prohibido el clickbait engañoso y las
  promesas vacías.
- Los comandos de las lecciones deben ser reales y comprobables.

## Licencia

[MIT](LICENSE)