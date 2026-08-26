#!/usr/bin/env bash
# Publie le site sur GitHub Pages (branche gh-pages).
#
# Deux modes, pilotés par les variables ci-dessous :
#
#   * Relecture (par défaut) — le site est servi depuis un sous-chemin
#     GitHub Pages et interdit à l'indexation, pour ne pas concurrencer le
#     futur site sur son vrai domaine.
#
#   * Production — dès qu'un nom de domaine est branché sur le dépôt :
#     mettre GH_USER/REPO à jour n'est plus nécessaire, il suffit de
#     renseigner DOMAINE et de passer STAGING à 0.
set -euo pipefail

cd "$(dirname "$0")"

# --- Réglages ---------------------------------------------------------------
# Organisation GitHub propriétaire du dépôt (celle de l'association).
GH_USER="${CEUC_GH_USER:-CEUCK9}"
# Nom du dépôt (sert de sous-chemin sur GitHub Pages).
REPO="${CEUC_REPO:-site-web}"
# Nom de domaine définitif, une fois réservé et branché (ex. "ceuc.fr").
# Laisser vide tant que le site tourne sur l'adresse github.io.
DOMAINE="${CEUC_DOMAINE:-}"
# 1 = version de relecture (non indexable) · 0 = site public définitif.
STAGING="${CEUC_STAGING:-1}"
# ----------------------------------------------------------------------------

if [ -n "$DOMAINE" ]; then
  # Avec un domaine propre, le site est servi à la racine : pas de sous-chemin.
  export CEUC_BASE_URL="https://$DOMAINE"
  export CEUC_BASE_PATH=""
  URL_PUBLIQUE="https://$DOMAINE/"
else
  # Le sous-domaine github.io est toujours en minuscules : on normalise pour
  # que les URL canoniques et le sitemap soient cohérents.
  GH_HOST="$(printf '%s' "$GH_USER" | tr '[:upper:]' '[:lower:]').github.io"
  export CEUC_BASE_URL="https://$GH_HOST"
  export CEUC_BASE_PATH="/$REPO"
  URL_PUBLIQUE="https://$GH_HOST/$REPO/"
fi
export CEUC_STAGING="$STAGING"

python3 build.py
python3 check.py

# GitHub Pages a besoin du fichier CNAME pour servir le domaine personnalisé.
if [ -n "$DOMAINE" ]; then
  echo "$DOMAINE" > dist/CNAME
fi

WORKTREE="$(mktemp -d)"
trap 'git worktree remove --force "$WORKTREE" 2>/dev/null || true; rm -rf "$WORKTREE"' EXIT

if git show-ref --quiet refs/heads/gh-pages; then
  git worktree add -q "$WORKTREE" gh-pages
else
  git worktree add -q --orphan -b gh-pages "$WORKTREE"
fi

find "$WORKTREE" -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
cp -r dist/. "$WORKTREE"/

git -C "$WORKTREE" add -A
if git -C "$WORKTREE" diff --cached --quiet; then
  echo "Aucun changement à publier."
  exit 0
fi
git -C "$WORKTREE" commit -q -m "Publication — $(date '+%d/%m/%Y %H:%M')"
git -C "$WORKTREE" push -q origin gh-pages

echo
if [ "$STAGING" = "1" ]; then
  echo "Publié (version de relecture, non indexable) : $URL_PUBLIQUE"
else
  echo "Publié (site public, indexable) : $URL_PUBLIQUE"
fi
