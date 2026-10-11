#!/usr/bin/env bash
# Graba todas las lecciones del plan de este proyecto.
# Autocontenido: la raíz es la carpeta de este script.
#   env: TIMEOUT_LECCION (defecto 120s), LECCIONES (lista opcional override)
set -euo pipefail

BASE="$(cd "$(dirname "$0")" && pwd)"
RAIZ="/home/sebas/.local/share/edu-factory"
PLAN="${PLAN:-PLAN_DEFECTO_PLACEHOLDER}"
SALIDA="$BASE"
TIMEOUT_LECCION="${TIMEOUT_LECCION:-300}"

export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH}"
export TUTORREC_VELOCIDAD="0.04"
export TUTORREC_SHELL="/bin/zsh"
export TUTORREC_COLS="${TUTORREC_COLS:-80}"
export TUTORREC_ROWS="${TUTORREC_ROWS:-48}"
export TUTORREC_PAUSA_FINAL="${TUTORREC_PAUSA_FINAL:-5.0}"

if [ -z "${LECCIONES:-}" ]; then
  LECCIONES=(
    1.1 1.2 1.3
    2.1 2.2 2.3
    3.1 3.2 3.3
    4.1 4.2 4.3
    5.1 5.2 5.3
    6.1 6.2 6.3
  )
fi

cd "$RAIZ"
for L in $LECCIONES; do
  echo "=== Lección $L (asciinema, 0.04, timeout ${TIMEOUT_LECCION}s) ==="
  timeout "$TIMEOUT_LECCION" python3 edu_factory.py tutorrec "$PLAN" \
    -l "$L" \
    -m demo \
    --backend asciinema \
    -s "$SALIDA" || {
      code=$?
      if [ "$code" -eq 124 ]; then
        echo "  ! Lección $L cortada por timeout. Sube TIMEOUT_LECCION."
      else
        echo "  ! Lección $L terminó con código $code."
      fi
    }
done

echo "Listo. .cast en $SALIDA/direccion/."
echo "Generar videos por módulo: bash $BASE/generar_videos.sh"
