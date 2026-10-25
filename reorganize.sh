#!/usr/bin/env bash
# Reorganiza el repo sin borrar nada. Ejecutar desde la raíz del repo ETH.
set -u

mkdir -p docs data src baselines Agente_RL EDA

mv_safe() {  # origen destino
  if [ -e "$1" ] && [ ! -e "$2" ]; then
    git mv "$1" "$2" 2>/dev/null || mv "$1" "$2"
    echo "movido: $1 -> $2"
  else
    echo "omitido: $1 (no existe o el destino ya existe)"
  fi
}

mv_safe recolector.py src/recolector_v1.py
mv_safe mempool_sample.csv data/mempool_sample.csv
mv_safe "Recursos_investigación_DeepSearch" docs/recursos

echo "Listo. index.html se deja en su lugar. Revisa con: git status"
