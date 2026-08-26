#!/usr/bin/env python3
"""Génère le site statique CEUC dans dist/.

    python3 build.py            # génère dist/
    python3 build.py --serve    # génère puis sert sur http://localhost:8000

Les images sont préparées séparément par src/images.py (elles changent rarement).
"""

import argparse
import datetime
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
DIST = os.path.join(ROOT, "dist")
ASSETS = os.path.join(ROOT, "assets")

sys.path.insert(0, SRC)

from template import BASE_PATH, BASE_URL, STAGING, render  # noqa: E402
import pages  # noqa: E402  (l'import enregistre toutes les pages)


# Préfixe les URL internes absolues quand le site est servi depuis un
# sous-chemin (GitHub Pages projet, par exemple). Ne touche ni aux URL
# absolues externes, ni aux liens protocol-relative « // ».
# Les deux styles de guillemets sont gérés : le contenu des pages en mélange.
_ABS_URL = re.compile(r"""\b(href|src|srcset|content)=(["'])/(?!/)""")


def apply_base_path(html):
    if not BASE_PATH:
        return html
    return _ABS_URL.sub(rf"\1=\g<2>{BASE_PATH}/", html)


# Priorité et fréquence de mise à jour par page, pour le sitemap.
SITEMAP_HINTS = {
    "": (1.0, "monthly"),
    "formations/": (0.9, "monthly"),
    "formations/police-municipale/": (0.9, "monthly"),
    "creation-brigade-canine/": (0.9, "monthly"),
    "particuliers/permis-chien-categorise/": (0.9, "monthly"),
    "vente-chiens/": (0.8, "monthly"),
    "contact/": (0.8, "yearly"),
    "mentions-legales/": (0.2, "yearly"),
}


def write(path, content, *, rewrite_urls=False):
    if rewrite_urls:
        content = apply_base_path(content)
    full = os.path.join(DIST, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


def build_pages():
    for p in pages.PAGES:
        html = render(
            slug=p["slug"],
            title=p["title"],
            description=p["description"],
            body=p["body"],
            breadcrumb=p.get("breadcrumb"),
            og_image=p.get("og_image", "/assets/img/hero-mordant.jpg"),
            extra_jsonld=p.get("extra_jsonld"),
            body_class=p.get("body_class", ""),
        )
        out = "index.html" if p["slug"] == "" else os.path.join(p["slug"], "index.html")
        write(out, html, rewrite_urls=True)
        print(f"  /{p['slug']}")


def build_404():
    from components import callout, page_header  # noqa: WPS433

    body = (
        '<section class="section err"><div class="wrap">'
        '<p class="err__code">404</p>'
        "<h1>Cette page n'existe pas (ou plus)</h1>"
        "<p class=\"lead\">Le site du CEUC a été entièrement refondu : certaines "
        "anciennes adresses ne sont plus valables.</p>"
        '<p class="btn-row" style="justify-content:center">'
        '<a class="btn btn--primary" href="/">Retour à l\'accueil</a>'
        '<a class="btn btn--ghost" href="/formations/">Voir les formations</a>'
        "</p></div></section>"
    )
    write("404.html", rewrite_urls=True, content=render(
        slug="404.html",
        title="Page introuvable | CEUC",
        description="La page demandée n'existe pas. Retrouvez les formations cynophiles du CEUC depuis l'accueil.",
        body=body,
    ))
    print("  /404.html")


def build_sitemap():
    today = datetime.date.today().isoformat()
    urls = []
    for p in pages.PAGES:
        prio, freq = SITEMAP_HINTS.get(p["slug"], (0.7, "monthly"))
        urls.append(
            "  <url>\n"
            f"    <loc>{BASE_URL}{BASE_PATH}/{p['slug']}</loc>\n"
            f"    <lastmod>{today}</lastmod>\n"
            f"    <changefreq>{freq}</changefreq>\n"
            f"    <priority>{prio}</priority>\n"
            "  </url>"
        )
    write("sitemap.xml",
          '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "\n".join(urls)
          + "\n</urlset>\n")
    print(f"  /sitemap.xml ({len(urls)} URL)")


def build_robots():
    if STAGING:
        # Version de relecture : surtout pas d'indexation, sinon elle entrerait en
        # concurrence avec le futur site sur les mêmes contenus.
        write("robots.txt", "User-agent: *\nDisallow: /\n")
        print("  /robots.txt (staging : indexation bloquée)")
        return
    write("robots.txt",
          "User-agent: *\n"
          "Allow: /\n\n"
          f"Sitemap: {BASE_URL}{BASE_PATH}/sitemap.xml\n")
    print("  /robots.txt")


def _redirect_mapping():
    """Anciennes URL du site free.fr → nouvelle arborescence.

    Le vieux site avait une trentaine de pages indexées : on préserve ce qui
    reste de leur référencement et surtout on évite d'envoyer les visiteurs
    sur une page introuvable.
    """
    return {
        "/index.html": "/",
        "/mieux_nous_connaitre.html": "/le-centre/",
        "/nos_structures.html": "/le-centre/#structures",
        "/partenaire_k9.html": "/le-centre/",
        "/presse.html": "/galerie/",
        "/formation_police_municipale.html": "/formations/police-municipale/",
        "/stage_perfectionnement.html": "/formations/perfectionnement/",
        "/olfaction.html": "/formations/olfaction-detection/",
        "/olfaction__recherche.html": "/formations/olfaction-detection/",
        "/capture_chiens_errants-dangereux.html": "/formations/capture-chien-dangereux/",
        "/stage_capture.html": "/formations/capture-chien-dangereux/",
        "/stage_capture-1.html": "/formations/capture-chien-dangereux/",
        "/seminaires_-_audits.html": "/creation-brigade-canine/",
        "/secourisme_operationnel_et_canin.html": "/formations/sst-secourisme/",
        "/conduite_operationnelle.html": "/formations/",
        "/stage_formateur.html": "/formations/",
        "/formation_chiens_dangereux.html": "/particuliers/permis-chien-categorise/",
        "/partenariat_education_canine.html": "/particuliers/permis-chien-categorise/",
        "/selection_chiens.html": "/vente-chiens/",
        "/vente_-_achats.html": "/vente-chiens/",
        "/tournage_-_cinema.html": "/cinema/",
        "/cinema.html": "/cinema/",
        "/cinema-1.html": "/cinema/",
        "/materiels_-_alimentation.html": "/prestations/",
        "/unites_cynophiles_-_brigade_canine.html": "/galerie/",
        "/brigade_canine_police.html": "/galerie/",
        "/debourrage_chiots.html": "/galerie/",
        "/demonstrations.html": "/galerie/",
        "/sport_et_gtpi.html": "/galerie/",
        "/projet_canin_reinsertion.html": "/galerie/",
        "/projet_reinsertion.html": "/galerie/",
        "/en_memoire_rip.html": "/galerie/",
        "/facebook.html": "/contact/",
        "/contact.html": "/contact/",
        "/imsitemap.html": "/",
        # URL de la première version de relecture, renommées après retour de
        # l'association : évite de casser les liens déjà partagés.
        "/chiens/": "/vente-chiens/",
        "/formations/seminaires-audits/": "/creation-brigade-canine/",
    }


def build_redirects():
    """Fichier de redirections au format Netlify / Cloudflare Pages."""
    mapping = _redirect_mapping()
    lines = [f"{old}  {new}  301" for old, new in mapping.items()]
    write("_redirects", "\n".join(lines) + "\n")
    print(f"  /_redirects ({len(mapping)} redirections)")


def build_htaccess():
    """Configuration Apache pour l'hébergement OVH.

    Sans ce fichier le site fonctionne, mais il est servi sans compression ni
    cache et reste accessible en HTTP simple — trois points que Google mesure
    et qui pèsent sur le référencement.
    """
    redirs = "\n".join(
        f"Redirect 301 {old} {new}" for old, new in _redirect_mapping().items()
        if old.endswith(".html")
    )
    write(".htaccess", f"""# Généré par build.py — ne pas modifier à la main.

# --- Page d'erreur maison plutôt que celle d'Apache ------------------------
ErrorDocument 404 /404.html

# --- Tout le trafic en HTTPS ----------------------------------------------
<IfModule mod_rewrite.c>
  RewriteEngine On
  RewriteCond %{{HTTPS}} !=on
  RewriteCond %{{HTTP:X-Forwarded-Proto}} !https
  RewriteRule ^(.*)$ https://%{{HTTP_HOST}}/$1 [R=301,L]
</IfModule>

# --- Compression : divise par trois le poids des pages et des styles ------
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html
  AddOutputFilterByType DEFLATE text/css
  AddOutputFilterByType DEFLATE text/plain
  AddOutputFilterByType DEFLATE text/xml
  AddOutputFilterByType DEFLATE application/javascript
  AddOutputFilterByType DEFLATE application/json
  AddOutputFilterByType DEFLATE image/svg+xml
</IfModule>

# --- Cache navigateur -----------------------------------------------------
<IfModule mod_expires.c>
  ExpiresActive On
  # Les images et polices ne changent pas de nom : cache court côté client,
  # mais suffisant pour éviter de les retélécharger à chaque page.
  ExpiresByType image/webp             "access plus 7 days"
  ExpiresByType image/jpeg             "access plus 7 days"
  ExpiresByType image/png              "access plus 7 days"
  ExpiresByType image/x-icon           "access plus 30 days"
  ExpiresByType text/css               "access plus 1 day"
  ExpiresByType application/javascript "access plus 1 day"
  ExpiresByType text/html              "access plus 0 seconds"
</IfModule>

# --- Anciennes adresses du site free.fr -----------------------------------
{redirs}
""")
    print("  /.htaccess (HTTPS, compression, cache, redirections)")


def copy_assets():
    dest = os.path.join(DIST, "assets")
    os.makedirs(dest, exist_ok=True)
    shutil.copy2(os.path.join(SRC, "style.css"), os.path.join(dest, "style.css"))
    shutil.copy2(os.path.join(SRC, "script.js"), os.path.join(dest, "script.js"))
    img_src = os.path.join(ASSETS, "img")
    if os.path.isdir(img_src):
        img_dest = os.path.join(dest, "img")
        if os.path.isdir(img_dest):
            shutil.rmtree(img_dest)
        shutil.copytree(img_src, img_dest)
        n = len(os.listdir(img_dest))
        print(f"  /assets ({n} images + css + js)")
    else:
        print("  /assets (css + js) — ATTENTION : aucune image, lancer src/images.py")
    # favicon.ico à la racine : certains crawlers ne lisent que celui-là
    fav = os.path.join(ASSETS, "img", "favicon.ico")
    if os.path.exists(fav):
        shutil.copy2(fav, os.path.join(DIST, "favicon.ico"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--serve", action="store_true", help="sert dist/ après le build")
    ap.add_argument("--port", type=int, default=8000)
    args = ap.parse_args()

    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)

    print("Génération du site :")
    build_pages()
    build_404()
    build_sitemap()
    build_robots()
    build_redirects()
    build_htaccess()
    write(".nojekyll", "")  # GitHub Pages : ne pas passer le site dans Jekyll
    copy_assets()
    print(f"\nSite généré dans {DIST}")

    if args.serve:
        import functools
        import http.server
        import socketserver

        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=DIST)
        socketserver.TCPServer.allow_reuse_address = True
        with socketserver.TCPServer(("", args.port), handler) as httpd:
            print(f"→ http://localhost:{args.port}  (Ctrl+C pour arrêter)")
            httpd.serve_forever()


if __name__ == "__main__":
    main()
