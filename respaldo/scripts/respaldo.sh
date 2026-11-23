#!/bin/bash
# respaldo.sh — actualiza tu repo de respaldo en UN solo comando.
#
# Uso:  bash scripts/respaldo.sh
#
# CONFIGURA ANTES: edita REPO y SOURCES (origen -> destino dentro del repo).
# El ejemplo de abajo respalda identidad, memoria y skills de un asistente;
# adapta las rutas a tu caso. Lo que el .gitignore bloquea no se stagea
# aunque el rsync lo copie.
#
# Hace, en orden:
#   1. rsync idempotente de cada fuente a su carpeta del repo
#   2. git add -A
#   3. escaneo de secretos (scripts/escanear-secretos.sh) — ABORTA si falla
#   4. UN solo commit + UN solo push a origin/main (vía conector GitHub)
#
# Reglas que aplica: secretos jamás, media jamás, nada mayor a 5 MB.
set -euo pipefail

REPO="$HOME/workspace/mi-respaldo"
# SOURCES: "origen:destino", una por línea. El origen se copia tal cual.
SOURCES="
$HOME/AGENTS.md:core/
$HOME/MEMORY.md:core/
$HOME/memory/:memory/
$HOME/workspace/custom-skills/:skills/
"

cd "$REPO" || { echo "No existe $REPO"; exit 1; }

echo "=== 1. sincronizando fuentes ==="
while IFS= read -r line; do
  [ -z "$line" ] && continue
  src="${line%%:*}"; dst="${line##*:}"
  mkdir -p "$REPO/$dst"
  if [ -d "$src" ]; then
    rsync -a --delete --exclude '.git' --exclude '__pycache__/' "$src" "$REPO/$dst"
  else
    cp "$src" "$REPO/$dst" 2>/dev/null || echo "  (falta: $src)"
  fi
done <<< "$SOURCES"

echo "=== 2. stage ==="
git add -A
N=$(git status --short | wc -l)
echo "  archivos con cambios: $N"

echo "=== 3. escaneo de secretos (aborta si falla) ==="
bash "$REPO/scripts/escanear-secretos.sh"

echo "=== 4. commit + push (uno solo) ==="
if git diff --cached --quiet; then
  echo "Sin cambios: nada que commitear."
else
  MSG="respaldo: actualización integral $(date +%F-%H%M)"
  # push-files solo acepta UTF-8: se filtran binarios (fuentes, media).
  # Esos archivos se reinstalan desde su origen (ver README paso 3).
  git diff --cached --name-only --diff-filter=ACM -z | tr '\0' '\n' \
    | grep -vE '\.(ttf|otf|woff2?|gif|png|jpe?g|webp|mp4|zip)$' \
    | tr '\n' '\0' > /tmp/respaldo-paths.nul
  git commit -m "$MSG"
  echo "  commit local: $(git rev-parse --short HEAD)"
  # Un solo push al remoto vía conector GitHub (un push_files = un commit remoto).
  # En trabajo proactivo el conector NO pide tarjeta y deniega el push:
  # en ese caso queda el commit local y el push se hace en un turno pedido.
  /opt/hatch/bin/github push-files --owner <tu-usuario-o-org> --repo <tu-repo> \
    --branch main --message "$MSG" --source-dir "$REPO" --paths-file /tmp/respaldo-paths.nul
  echo "Push OK"
  rm -f /tmp/respaldo-paths.nul
fi

echo "=== tamaño final ==="
du -sh "$REPO"
echo "Listo."
