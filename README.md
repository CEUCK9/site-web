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
