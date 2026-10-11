#!/usr/bin/env bash
# Genera UN video (mp4) + UN gif por módulo, dentro de cada carpeta de módulo.
#   direccion/modulo-X-.../video.mp4   (1080x1920, CRF 18, nítido)
#   direccion/modulo-X-.../video.gif
# Autocontenido: usa la carpeta donde vive este script como raíz del proyecto.
# Requiere: agg, ffmpeg.
set -euo pipefail

BASE="$(cd "$(dirname "$0")" && pwd)"
DIRECCION="$BASE/direccion"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

[ -d "$DIRECCION" ] || { echo "No existe $DIRECCION (ejecuta grabar_todas.sh primero)"; exit 1; }

# Render: alineado al cast (80x48), font grande para legibilidad en 9:16
AGG_COLS="${AGG_COLS:-80}"
AGG_ROWS="${AGG_ROWS:-48}"
AGG_FONT="${AGG_FONT:-22}"
AGG_FPS="${AGG_FPS:-30}"

# Pad 9:16 (Reels/TikTok/Shorts); el cast ya lleva su tema embebido (fondo negro)
PAD916="scale=1080:1920:force_original_aspect_ratio=decrease:flags=lanczos,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=black"
# Encode nítido: CRF 18 + medium (slow se cuelga en concat largos)
X264="-c:v libx264 -preset medium -crf 18 -profile:v high -pix_fmt yuv420p -movflags +faststart -r 30"

encontrados=0
for modulo in "$DIRECCION"/modulo-*/; do
  [ -d "$modulo" ] || continue
  nombre_mod=$(basename "$modulo")

  listacasts="$TMP/${nombre_mod}_casts.txt"
  find "$modulo" -maxdepth 2 -name 'leccion-*.cast' | sort -t. -k2 -n > "$listacasts" || true
  casts=()
  while IFS= read -r c; do
    [ -n "$c" ] && casts+=("$c")
  done < "$listacasts"
  if [ "${#casts[@]}" -eq 0 ]; then
    echo "— $nombre_mod: sin .cast, se omite"
    continue
  fi

  echo "=== $nombre_mod (${#casts[@]} lección/lecciones) ==="

  lista="$TMP/$nombre_mod.txt"
  : > "$lista"
  i=0
  for cast in "${casts[@]}"; do
    i=$((i + 1))
    gif="$TMP/${nombre_mod}_$i.gif"
    mp4="$TMP/${nombre_mod}_$i.mp4"
    echo "  · $(basename "$cast") -> gif -> mp4 9:16"
    # agg usa el tema embebido del cast (fondo negro), font grande = nítido al escalar
    agg --cols "$AGG_COLS" --rows "$AGG_ROWS" --font-size "$AGG_FONT" \
      --fps-cap "$AGG_FPS" "$cast" "$gif" >/dev/null 2>&1 || {
      echo "    ! fallo agg en $cast"; continue
    }
    ffmpeg -y -loglevel error -i "$gif" -vf "$PAD916" $X264 "$mp4"
    echo "file '$mp4'" >> "$lista"
  done
  [ -s "$lista" ] || { echo "  ! nada que concatenar"; continue; }

  concat="$TMP/${nombre_mod}_concat.mp4"
  ffmpeg -y -loglevel error -f concat -safe 0 -i "$lista" -c copy "$concat"

  # Salida DENTRO de la carpeta del módulo
  mp4_out="${modulo}video.mp4"
  gif_out="${modulo}video.gif"
  echo "  · generando MP4 9:16 del módulo (CRF 18)..."
  cp -f "$concat" "$mp4_out"

  echo "  · generando GIF 9:16..."
  # Intentar 1080x1920; si se queda sin RAM, bajar a 720x1280
  if ! ffmpeg -y -loglevel error -i "$concat" \
    -vf "fps=10,split[s0][s1];[s0]palettegen=max_colors=96:stats_mode=diff[p];[s1][p]paletteuse=dither=bayer:bayer_scale=3" \
    "$gif_out" 2>/dev/null; then
    echo "  · GIF full-res falló, reintentando 720x1280..."
    if ! ffmpeg -y -loglevel error -i "$concat" \
      -vf "scale=720:1280:flags=lanczos,fps=8,split[s0][s1];[s0]palettegen=max_colors=64:stats_mode=diff[p];[s1][p]paletteuse=dither=bayer:bayer_scale=3" \
      "$gif_out" 2>/dev/null; then
      echo "  ! GIF falló; el MP4 sí quedó bien"
      rm -f "$gif_out"
    fi
  fi

  encontrados=1
  echo "  ✓ $mp4_out"
  [ -f "$gif_out" ] && echo "  ✓ $gif_out"
done

if [ "$encontrados" -eq 0 ]; then
  echo "No hay .cast en direccion/. Graba antes con grabar_todas.sh"
  exit 1
fi

echo
echo "Listo. Videos en cada carpeta de módulo bajo: $DIRECCION"
