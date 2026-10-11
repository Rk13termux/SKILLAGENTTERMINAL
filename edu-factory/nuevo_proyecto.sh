#!/usr/bin/env bash
# Crea un proyecto nuevo autocontenido en WORKSPACETERMUX/<nombre>/
#   Uso: bash nuevo_proyecto.sh <nombre-del-proyecto> <ruta-al-plan.md>
#   Ej:  bash nuevo_proyecto.sh podman-fedora curriculum/master-lesson-podman-fedora.md
set -euo pipefail

WORKSPACE="${EDU_FACTORY_WORKSPACE:-/mnt/sdcard/WORKSPACETERMUX}"
RAIZ="/home/sebas/.local/share/edu-factory"
TPL="$RAIZ/plantillas-proyecto"

NOMBRE="${1:-}"
PLAN="${2:-}"

if [ -z "$NOMBRE" ] || [ -z "$PLAN" ]; then
  echo "Uso: bash $0 <nombre-del-proyecto> <ruta-al-plan.md>"
  echo "Ej:  bash $0 podman-fedora $RAIZ/curriculum/master-lesson-podman-fedora.md"
  exit 1
fi

PLAN_ABS="$(readlink -f "$PLAN" 2>/dev/null || echo "$PLAN")"
if [ ! -f "$PLAN_ABS" ]; then
  echo "No existe el plan: $PLAN_ABS"
  echo "Planes disponibles en $RAIZ/curriculum/:"
  ls "$RAIZ/curriculum/"*.md 2>/dev/null | sed 's|.*/|  |' || true
  exit 1
fi

DEST="$WORKSPACE/$NOMBRE"
if [ -d "$DEST" ]; then
  echo "El proyecto ya existe: $DEST"
  exit 1
fi

mkdir -p "$DEST"/{direccion,social,cursos}

# Scripts parametrizados con PLAN y BASE
sed "s|PLAN_DEFECTO_PLACEHOLDER|$PLAN_ABS|g" "$TPL/grabar_todas.sh" > "$DEST/grabar_todas.sh"
cp "$TPL/generar_videos.sh" "$DEST/generar_videos.sh"
chmod +x "$DEST/grabar_todas.sh" "$DEST/generar_videos.sh"

# Symlink cómodo
ln -sfn "$DEST" "$HOME/productions" 2>/dev/null || true

echo "Proyecto creado: $DEST"
echo "  · direccion/  social/  cursos/"
echo "  · grabar_todas.sh   (PLAN=$PLAN_ABS)"
echo "  · generar_videos.sh (mp4+gif dentro de cada módulo)"
echo
echo "Siguiente paso:"
echo "  cd $DEST && bash grabar_todas.sh && bash generar_videos.sh"
