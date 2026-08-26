# Site CEUC — Centre d'Entraînement Unités Cynophiles

Refonte du site de l'association CEUC (Meximieux, 01), centre de formation en
cynotechnie professionnelle. Générateur de site statique maison, sans dépendance
au moment du build.

## Utilisation

```bash
python3 build.py            # génère dist/
python3 build.py --serve    # génère puis sert sur http://localhost:8000
python3 check.py            # contrôle liens, SEO, structure de titres, JSON-LD
```

Les images sont préparées séparément (nécessite Pillow) :

```bash
CEUC_SRC=/chemin/vers/photos python3 src/images.py
```

## Variables d'environnement

| Variable | Rôle |
|---|---|
| `CEUC_BASE_URL` | URL publique du site (défaut : domaine de production) |
| `CEUC_BASE_PATH` | Sous-chemin de service, ex. `/ceuc` pour GitHub Pages projet |
| `CEUC_STAGING` | `1` pour bloquer l'indexation de la version de relecture |

## Organisation

```
build.py            génération du site
check.py            contrôles qualité (à lancer après chaque build)
src/template.py     gabarit HTML, SEO, JSON-LD, navigation
src/components.py   blocs de contenu réutilisables
src/pages.py        contenu de toutes les pages
src/gallery_data.py photos de la galerie et leurs légendes
src/images.py       préparation des images (WebP + JPEG)
src/style.css       feuille de style
src/script.js       menu mobile et visionneuse photo
assets/img/         images optimisées (versionnées)
dist/               site généré (non versionné)
```

Voir `CLAUDE.md` pour la méthodologie de travail avec l'association et
`NOTES.md` pour le détail du contenu collecté.

## Déploiement de la version de relecture

Le site de relecture est publié sur GitHub Pages depuis la branche `gh-pages` :

```bash
./deploy.sh
```

Le script regénère `dist/`, lance `check.py` et pousse le résultat sur la
branche `gh-pages`. Trois réglages en tête de fichier suffisent à couvrir tous
les cas :

| Réglage | Rôle |
|---|---|
| `GH_USER` | compte ou organisation propriétaire du dépôt (à changer après le transfert) |
| `DOMAINE` | nom de domaine définitif ; laissé vide tant qu'on est sur `github.io` |
| `STAGING` | `1` version de relecture non indexable · `0` site public |

Renseigner `DOMAINE` bascule automatiquement le site à la racine et écrit le
fichier `CNAME` attendu par GitHub Pages.

Une alternative existe sous forme d'action GitHub
(`.github/workflows-disponibles/deploy.yml.exemple`) : elle reconstruit et
publie automatiquement à chaque push. Pour l'activer, déplacer le fichier dans
`.github/workflows/deploy.yml` — cela nécessite un jeton disposant du scope
`workflow` (`gh auth refresh -s workflow`).
