#!/usr/bin/env python3
"""Prépare les images du site à partir des sources récupérées sur l'ancien site.

Les sources (ancien site ceuc.free.fr) plafonnent à 800px de large : on ne
sur-échelonne jamais, on se contente d'optimiser et de recadrer. Le jour où
Maxime fournit des photos HD, il suffit de remplacer les fichiers dans SRC/
et de relancer ce script.
"""
import os
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.environ.get("CEUC_SRC", "")
OUT = os.path.join(ROOT, "assets", "img")

# Photos fournies par l'association (2025-2026), versionnées dans le dépôt :
# ce sont elles qui remplacent progressivement les visuels de l'ancien site.
PHOTOS_2026_DIR = os.path.join(ROOT, "assets", "photos-2026")

PHOTOS_2026 = {
    # Accueil — bandeau large, on garde le cadrage d'origine.
    "page_acceuil.jpg":        ("hero-rassemblement",       1400, None),
    # Le centre — photo d'équipe.
    "centre.jpg":              ("equipe-ceuc",               900, (4, 3)),
    # Stage de perfectionnement.
    "perfectionnement_1.jpg":  ("perfectionnement-01",       900, (3, 2)),
    "perfectionnement_2.jpg":  ("perfectionnement-02",       900, (3, 2)),
    # Olfaction / recherche de personnes.
    "recherche_personne.jpg":  ("recherche-personne",        900, (3, 2)),
    # Secourisme SST — portrait, on conserve un cadrage vertical doux.
    "secourisme.jpg":          ("secourisme-sst",            800, (4, 5)),
}

# Chaque entrée : fichier source -> (nom de sortie, largeur max, ratio de recadrage ou None)
PHOTOS = {
    # Hero et grandes images
    "ib_p028_1_7.jpg":   ("hero-mordant",            1000, (16, 9)),
    "ib_p028_1_6.jpg":   ("malinois-police",          900, (4, 3)),
    # Formations professionnelles
    "ib_p028_1_17.jpg":  ("formation-police-municipale", 800, (3, 2)),
    "ib_p028_1_1.jpg":   ("stage-perfectionnement",   800, (3, 2)),
    "ib_p028_1_39.png":  ("olfaction-detection",      800, (3, 2)),
    "ib_p036_0_31.jpg":  ("capture-chien",            800, (3, 2)),
    "ib_p028_1_30.png":  ("seminaires-audits",        800, (3, 2)),
    "ib_p028_1_35.png":  ("secourisme-intervention",  800, (3, 2)),
    # Particuliers / chiens / cinéma
    "ib_p028_1_23.png":  ("particuliers-education",   800, (3, 2)),
    "ib_p028_1_29.png":  ("selection-chiens",         800, (3, 2)),
    "ib_p017_0_14.jpg":  ("cinema-tournage",          800, (3, 2)),
    # Le centre
    "ib_p028_1_16.jpg":  ("structures-terrain",       800, (3, 2)),
    "ib_p041_0_9.png":   ("equipe-unite-cynophile",   800, (3, 2)),
    "ib_p028_1_5.png":   ("rassemblement-inter-adm",  900, (21, 9)),
}

# Galerie : la liste (source, légende) est partagée avec le générateur de pages.
from gallery_data import GALERIE  # noqa: E402


def crop_to_ratio(im, ratio):
    """Recadre au centre selon le ratio demandé, sans jamais agrandir."""
    if ratio is None:
        return im
    tw, th = ratio
    w, h = im.size
    target = tw / th
    current = w / h
    if abs(current - target) < 0.01:
        return im
    if current > target:  # trop large -> on rogne les côtés
        new_w = int(h * target)
        left = (w - new_w) // 2
        return im.crop((left, 0, left + new_w, h))
    new_h = int(w / target)  # trop haut -> on rogne haut/bas
    top = int((h - new_h) * 0.35)  # légèrement au-dessus du centre : garde les visages/chiens
    return im.crop((0, top, w, top + new_h))


def process(src_path, name, max_w, ratio):
    im = Image.open(src_path).convert("RGB")
    im = crop_to_ratio(im, ratio)
    if im.width > max_w:
        im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
    im.save(os.path.join(OUT, f"{name}.webp"), "WEBP", quality=82, method=6)
    im.save(os.path.join(OUT, f"{name}.jpg"), "JPEG", quality=80, optimize=True, progressive=True)
    return im.size


def make_logo(src_dir):
    """Détoure le fond blanc du logo et génère les déclinaisons."""
    from collections import deque

    im = Image.open(os.path.join(src_dir, "images", "home_1_00.jpg")).convert("RGBA")
    w, h = im.size
    px = im.load()
    seen = [[False] * h for _ in range(w)]
    q = deque()
    for x in range(w):
        q.extend([(x, 0), (x, h - 1)])
    for y in range(h):
        q.extend([(0, y), (w - 1, y)])
    while q:
        x, y = q.popleft()
        if x < 0 or y < 0 or x >= w or y >= h or seen[x][y]:
            continue
        seen[x][y] = True
        p = px[x, y]
        if not (p[0] > 225 and p[1] > 225 and p[2] > 225):
            continue
        px[x, y] = (255, 255, 255, 0)
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            q.append((x + dx, y + dy))

    side = max(im.size)
    square = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    square.paste(im, ((side - im.width) // 2, (side - im.height) // 2))
    square.save(os.path.join(OUT, "logo-ceuc.png"))
    for size in (32, 180, 512):
        square.resize((size, size), Image.LANCZOS).save(
            os.path.join(OUT, f"logo-{size}.png")
        )
    # favicon.ico multi-tailles
    square.resize((64, 64), Image.LANCZOS).save(
        os.path.join(OUT, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)]
    )
    print("logo -> logo-ceuc.png + déclinaisons")


def main():
    if not SRC or not os.path.isdir(SRC):
        sys.exit(
            "Définir CEUC_SRC vers le dossier contenant ib/ et images/ "
            "(photos récupérées sur l'ancien site)."
        )
    os.makedirs(OUT, exist_ok=True)
    ib = os.path.join(SRC, "ib")

    make_logo(SRC)

    for src, (name, max_w, ratio) in PHOTOS_2026.items():
        p = os.path.join(PHOTOS_2026_DIR, src)
        if not os.path.exists(p):
            print(f"  MANQUANT (2026) {src}")
            continue
        print(f"  {name} {process(p, name, max_w, ratio)}")

    for src, (name, max_w, ratio) in PHOTOS.items():
        p = os.path.join(ib, src)
        if not os.path.exists(p):
            print(f"  MANQUANT {src}")
            continue
        print(f"  {name} {process(p, name, max_w, ratio)}")

    for i, item in enumerate(GALERIE, 1):
        src = item["src"]
        base = PHOTOS_2026_DIR if item.get("recent") else ib
        p = os.path.join(base, src)
        if not os.path.exists(p):
            print(f"  MANQUANT galerie {src}")
            continue
        im = Image.open(p).convert("RGB")
        box = item.get("crop")
        if box:
            l, t, r, b = box
            im = im.crop((round(l * im.width), round(t * im.height),
                          round(r * im.width), round(b * im.height)))
        # vignette carrée pour la grille
        thumb = crop_to_ratio(im, (1, 1))
        if thumb.width > 600:
            thumb = thumb.resize((600, 600), Image.LANCZOS)
        thumb.save(os.path.join(OUT, f"galerie-{i:02d}-thumb.webp"), "WEBP", quality=80, method=6)
        thumb.save(os.path.join(OUT, f"galerie-{i:02d}-thumb.jpg"), "JPEG", quality=78, optimize=True)
        # version pleine taille pour la lightbox
        im.save(os.path.join(OUT, f"galerie-{i:02d}.webp"), "WEBP", quality=84, method=6)
        im.save(os.path.join(OUT, f"galerie-{i:02d}.jpg"), "JPEG", quality=82, optimize=True, progressive=True)
        print(f"  galerie-{i:02d} {im.size}")

    print(f"\nImages écrites dans {OUT}")


if __name__ == "__main__":
    main()
