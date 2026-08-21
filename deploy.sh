#!/usr/bin/env bash
# Publie la version de relecture sur GitHub Pages (branche gh-pages).
#
# Le site est construit en mode « staging » : servi depuis /ceuc et interdit
# à l'indexation, pour ne pas concurrencer le futur site sur son vrai domaine.
set -euo pipefail

cd "$(dirname "$0")"

export CEUC_BASE_URL="https://avtplay.github.io"
export CEUC_BASE_PATH="/ceuc"
export CEUC_STAGING="1"

python3 build.py
python3 check.py

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
git -C "$WORKTREE" commit -q -m "Version de relecture — $(date '+%d/%m/%Y %H:%M')"
git -C "$WORKTREE" push -q origin gh-pages

echo
echo "Publié : https://avtplay.github.io/ceuc/"
