#!/usr/bin/env bash
# Publie une PRÉVERSION du site sur GitHub Pages.
#
# Le site public, lui, est servi par l'hébergement OVH de l'association :
# il est mis à jour automatiquement à chaque modification poussée sur
# `main` (voir .github/workflows-disponibles/deploy.yml.exemple).
#
# Ce script sert donc à regarder un changement avant de le publier, ou à
# dépanner si l'envoi automatique est en panne. La préversion est toujours
# interdite à l'indexation.
set -euo pipefail

cd "$(dirname "$0")"

# --- Réglages ---------------------------------------------------------------
# Organisation GitHub propriétaire du dépôt (celle de l'association).
GH_USER="${CEUC_GH_USER:-CEUCK9}"
# Nom du dépôt (sert de sous-chemin sur GitHub Pages).
REPO="${CEUC_REPO:-site-web}"
# Nom de domaine servi par GitHub Pages. Laissé vide : le site public vit
# sur l'hébergement OVH (voir .github/workflows), et cette adresse github.io
# ne sert plus que de préversion.
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

# On repart toujours de ce qui est réellement publié, jamais d'une copie
# locale : GitHub écrit lui-même sur cette branche (fichier CNAME ajouté
# quand on renseigne un domaine dans l'interface), et une branche locale
# obsolète ferait échouer la publication.
git fetch -q origin gh-pages 2>/dev/null || true
if git show-ref --quiet refs/remotes/origin/gh-pages; then
  git worktree add -q --detach "$WORKTREE" origin/gh-pages
elif git show-ref --quiet refs/heads/gh-pages; then
  git worktree add -q --detach "$WORKTREE" gh-pages
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
git -C "$WORKTREE" push -q origin HEAD:gh-pages

echo
if [ "$STAGING" = "1" ]; then
  echo "Publié (version de relecture, non indexable) : $URL_PUBLIQUE"
else
  echo "Publié (site public, indexable) : $URL_PUBLIQUE"
fi
