#!/bin/bash
# escanear-secretos.sh — escanea los archivos stageados (git diff --cached)
# Skill propia de wekyt (MIT). Sale 0 si está limpio; sale 1 si hay hallazgos.
# en busca de secretos por nombre, por contenido y por tamaño (>5 MB).
# Uso: bash scripts/escanear-secretos.sh
# Sale 0 si está limpio; sale 1 con reporte si hay hallazgos (el push aborta).
set -uo pipefail

cd "$(dirname "$0")/.." || exit 1

STAGED=$(git diff --cached --name-only --diff-filter=ACM)
if [ -z "$STAGED" ]; then
  echo "escanear-secretos: nada stageado, limpio."
  exit 0
fi

FALLOS=0
reporte() { echo "  [HALLAZGO] $1"; FALLOS=$((FALLOS+1)); }

echo "escanear-secretos: revisando $(echo "$STAGED" | wc -l) archivos stageados..."

# 1. Patrones de nombre (secretos)
PATRON_NOMBRE='\.(env|pem|key|keystore|p12|pfx|kdbx)$|(^|/)\.env|credentials?|secrets?|\.netrc|id_rsa|id_ed25519|id_ecdsa|id_dsa|spend_ledger\.json$'
while IFS= read -r f; do
  if echo "$f" | grep -qiE "$PATRON_NOMBRE"; then
    reporte "nombre sospechoso: $f"
  fi
done <<< "$STAGED"

# 2. Tamaño >5 MB
while IFS= read -r f; do
  if [ -f "$f" ]; then
    bytes=$(stat -c%s "$f" 2>/dev/null || stat -f%z "$f" 2>/dev/null || echo 0)
    if [ "$bytes" -gt 5242880 ]; then
      reporte "supera 5 MB ($bytes bytes): $f"
    fi
  fi
done <<< "$STAGED"

# 3. Patrones de contenido (valores con pinta de clave)
# Se revisan archivos de texto razonablemente pequeños (<1 MB) para no colgar.
PATRON_CONTENIDO='sk-[a-zA-Z0-9]{16,}|ghp_[a-zA-Z0-9]{16,}|gho_[a-zA-Z0-9]{16,}|xox[bap]-[a-zA-Z0-9-]{8,}|AKIA[0-9A-Z]{16}|-----BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY-----|api[_-]?key["'\'']?[[:space:]]*[:=][[:space:]]*["'\''][^"'\''[:space:]]{16,}|password["'\'']?[[:space:]]*[:=][[:space:]]*["'\''][^"'\''[:space:]]{8,}|bearer [a-zA-Z0-9._-]{20,}'
while IFS= read -r f; do
  if [ -f "$f" ]; then
    bytes=$(stat -c%s "$f" 2>/dev/null || stat -f%z "$f" 2>/dev/null || echo 0)
    if [ "$bytes" -lt 1048576 ] && file -b "$f" | grep -qi "text"; then
      # Exclusión: este propio script documenta los patrones (falsos positivos).
      if [ "$f" = "scripts/escanear-secretos.sh" ]; then continue; fi
      if grep -qE "$PATRON_CONTENIDO" "$f" 2>/dev/null; then
        reporte "contenido con pinta de clave en: $f"
      fi
    fi
  fi
done <<< "$STAGED"

if [ "$FALLOS" -gt 0 ]; then
  echo "escanear-secretos: $FALLOS hallazgo(s). PUSH ABORTADO."
  echo "Excluye los archivos reportados y vuelve a correr bin/respaldo.sh."
  exit 1
fi
echo "escanear-secretos: limpio."
exit 0
