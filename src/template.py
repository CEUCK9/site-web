"""Gabarit HTML commun à toutes les pages du site CEUC.

Tout le SEO structurel (title, description, canonical, Open Graph, JSON-LD,
fil d'Ariane) est centralisé ici pour qu'aucune page ne puisse l'oublier.
"""

import html
import json
import os

# --------------------------------------------------------------------------
# Configuration du site
# --------------------------------------------------------------------------

# Domaine définitif, à confirmer avec l'association avant la migration OVH.
PROD_URL = "https://ceuc-k9.fr"

# Pendant la phase de relecture, le site tourne sur un hébergement gratuit :
#   CEUC_BASE_URL   URL publique de cet hébergement
#   CEUC_BASE_PATH  sous-chemin éventuel (GitHub Pages projet = "/ceuc")
#   CEUC_STAGING    "1" pour interdire l'indexation de la version de test
BASE_URL = os.environ.get("CEUC_BASE_URL", PROD_URL).rstrip("/")
BASE_PATH = os.environ.get("CEUC_BASE_PATH", "").rstrip("/")
STAGING = os.environ.get("CEUC_STAGING") == "1"

SITE_NAME = "CEUC — Centre d'Entraînement des Unités Cynophiles"
SITE_SHORT = "CEUC"

ORG = {
    "nom": "Centre d'Entraînement des Unités Cynophiles",
    "sigle": "CEUC",
    "adresse": "Chemin du Mortaray",
    "code_postal": "01800",
    "ville": "Meximieux",
    "region": "Ain",
    "pays": "FR",
    "email": "ceuck9@yahoo.fr",
    "tel1": "06 62 20 60 13",
    "tel1_uri": "+33662206013",
    "tel2": "06 37 48 39 47",
    "tel2_uri": "+33637483947",
    "facebook": "https://www.facebook.com/ceuc.cyno",
    "instagram": "https://www.instagram.com/ceuc_k9/",
    "prefecture": "W012002577",
    "siret": "52506111500024",
    "of": "82010131101",
}

# --------------------------------------------------------------------------
# Navigation
# --------------------------------------------------------------------------

NAV = [
    ("Le centre", "/le-centre/", []),
    ("Formations", "/formations/", [
        ("Cynotechnicien Police Municipale", "/formations/police-municipale/"),
        ("Stage de perfectionnement", "/formations/perfectionnement/"),
        ("Olfaction & recherche", "/formations/olfaction-detection/"),
        ("Capture de chiens dangereux", "/formations/capture-chien-dangereux/"),
        ("Secourisme SST", "/formations/sst-secourisme/"),
    ]),
    ("Brigade canine", "/creation-brigade-canine/", []),
    ("Particuliers", "/particuliers/permis-chien-categorise/", []),
    ("Vente de chiens", "/vente-chiens/", []),
    ("Cinéma", "/cinema/", []),
    ("Galerie", "/galerie/", []),
]


def e(text):
    """Échappe le texte pour l'insertion en HTML."""
    return html.escape(text, quote=True)


# --------------------------------------------------------------------------
# Données structurées (JSON-LD)
# --------------------------------------------------------------------------

def _org_jsonld():
    return {
        "@type": ["LocalBusiness", "EducationalOrganization"],
        "@id": f"{BASE_URL}/#organisation",
        "name": ORG["nom"],
        "alternateName": ORG["sigle"],
        "url": BASE_URL + "/",
        "logo": f"{BASE_URL}/assets/img/logo-512.png",
        "image": f"{BASE_URL}/assets/img/hero-mordant.jpg",
        "email": ORG["email"],
        "telephone": ORG["tel1_uri"],
        "description": (
            "Centre de formation en cynotechnie professionnelle : formation de "
            "cynotechniciens de Police Municipale, stages de perfectionnement, "
            "olfaction, capture de chiens dangereux et permis de détention de "
            "chiens catégorisés."
        ),
        "address": {
            "@type": "PostalAddress",
            "streetAddress": ORG["adresse"],
            "postalCode": ORG["code_postal"],
            "addressLocality": ORG["ville"],
            "addressRegion": ORG["region"],
            "addressCountry": ORG["pays"],
        },
        "areaServed": {"@type": "Country", "name": "France"},
        "sameAs": [ORG["facebook"], ORG["instagram"]],
    }


def _breadcrumb_jsonld(breadcrumb):
    items = [{
        "@type": "ListItem",
        "position": 1,
        "name": "Accueil",
        "item": BASE_URL + "/",
    }]
    for i, (label, url) in enumerate(breadcrumb, start=2):
        items.append({
            "@type": "ListItem",
            "position": i,
            "name": label,
            "item": BASE_URL + url,
        })
    return {"@type": "BreadcrumbList", "itemListElement": items}


def _course_jsonld(course, url):
    return {
        "@type": "Course",
        "name": course["nom"],
        "description": course["description"],
        "url": BASE_URL + url,
        "provider": {"@id": f"{BASE_URL}/#organisation"},
        "inLanguage": "fr-FR",
        "courseMode": "onsite",
        "locationCreated": {
            "@type": "Place",
            "name": ORG["nom"],
            "address": {
                "@type": "PostalAddress",
                "addressLocality": ORG["ville"],
                "postalCode": ORG["code_postal"],
                "addressCountry": ORG["pays"],
            },
        },
    }


# --------------------------------------------------------------------------
# Fragments de mise en page
# --------------------------------------------------------------------------

def _nav_html(current_url):
    out = []
    for label, url, children in NAV:
        active = current_url == url or (children and current_url.startswith(url))
        cls = ' class="is-active"' if active else ""
        if children:
            sub = "".join(
                f'<li><a href="{u}"{" class=\'is-active\'" if current_url == u else ""}>{e(l)}</a></li>'
                for l, u in children
            )
            out.append(
                f'<li class="nav__item nav__item--has-sub">'
                f'<a href="{url}"{cls}>{e(label)}'
                f'<svg class="nav__chev" width="10" height="6" viewBox="0 0 10 6" aria-hidden="true">'
                f'<path d="M1 1l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.6" '
                f'stroke-linecap="round"/></svg></a>'
                f'<ul class="nav__sub">{sub}</ul></li>'
            )
        else:
            out.append(f'<li class="nav__item"><a href="{url}"{cls}>{e(label)}</a></li>')
    return "".join(out)


def _breadcrumb_html(breadcrumb):
    if not breadcrumb:
        return ""
    parts = ['<a href="/">Accueil</a>']
    for i, (label, url) in enumerate(breadcrumb):
        last = i == len(breadcrumb) - 1
        if last:
            parts.append(f'<span aria-current="page">{e(label)}</span>')
        else:
            parts.append(f'<a href="{url}">{e(label)}</a>')
    sep = '<span class="breadcrumb__sep" aria-hidden="true">/</span>'
    return (
        '<nav class="breadcrumb" aria-label="Fil d\'Ariane"><div class="wrap">'
        + sep.join(parts)
        + "</div></nav>"
    )


HEADER_TPL = """<a class="skip" href="#contenu">Aller au contenu</a>
<header class="site-header" id="site-header">
  <div class="wrap site-header__inner">
    <a class="brand" href="/">
      <img src="/assets/img/logo-180.png" width="52" height="52" alt="" class="brand__logo">
      <span class="brand__text">
        <strong>CEUC</strong>
        <span>Centre d'Entraînement des Unités Cynophiles</span>
      </span>
    </a>
    <button class="burger" type="button" aria-expanded="false" aria-controls="nav-principal"
            aria-label="Ouvrir le menu">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav" id="nav-principal" aria-label="Navigation principale">
      <ul class="nav__list">%(nav)s</ul>
      <a class="btn btn--sm btn--primary nav__cta" href="/contact/">Nous contacter</a>
    </nav>
  </div>
</header>"""


FOOTER_TPL = """<footer class="site-footer">
  <div class="wrap site-footer__grid">
    <div class="site-footer__brand">
      <img src="/assets/img/logo-180.png" width="72" height="72" alt="Logo du CEUC" loading="lazy">
      <p class="site-footer__baseline">
        Centre d'instruction cynophile dédié aux professionnels des unités
        cynotechniques, encadré uniquement par des policiers municipaux.
      </p>
      <div class="social">
        <a href="%(facebook)s" rel="noopener" target="_blank" aria-label="Facebook du CEUC">Facebook</a>
        <a href="%(instagram)s" rel="noopener" target="_blank" aria-label="Instagram du CEUC">Instagram</a>
      </div>
    </div>
    <div>
      <h2 class="site-footer__title">Formations</h2>
      <ul class="site-footer__list">
        <li><a href="/formations/police-municipale/">Cynotechnicien Police Municipale</a></li>
        <li><a href="/formations/perfectionnement/">Stage de perfectionnement</a></li>
        <li><a href="/formations/olfaction-detection/">Olfaction &amp; recherche</a></li>
        <li><a href="/formations/capture-chien-dangereux/">Capture de chiens dangereux</a></li>
                <li><a href="/formations/sst-secourisme/">Secourisme SST</a></li>
      </ul>
    </div>
    <div>
      <h2 class="site-footer__title">Le centre</h2>
      <ul class="site-footer__list">
        <li><a href="/le-centre/">Présentation &amp; équipe</a></li>
        <li><a href="/particuliers/permis-chien-categorise/">Permis chien catégorisé</a></li>
        <li><a href="/vente-chiens/">Vente de chiens</a></li>
        <li><a href="/creation-brigade-canine/">Création de brigade canine</a></li>
        <li><a href="/cinema/">Cinéma &amp; tournages</a></li>
        <li><a href="/prestations/">Prestations annexes</a></li>
        <li><a href="/galerie/">Galerie photos</a></li>
      </ul>
    </div>
    <div>
      <h2 class="site-footer__title">Contact</h2>
      <address class="site-footer__address">
        %(adresse)s<br>%(code_postal)s %(ville)s<br>
        <a href="tel:%(tel1_uri)s">%(tel1)s</a><br>
        <a href="tel:%(tel2_uri)s">%(tel2)s</a><br>
        <a href="mailto:%(email)s">%(email)s</a>
      </address>
    </div>
  </div>
  <div class="wrap site-footer__legal">
    <p>
      Préfecture de l'Ain n°%(prefecture)s · SIRET %(siret)s ·
      Organisme de formation n°%(of)s
    </p>
    <p>
      © <span id="annee">2026</span> CEUC — Tous droits réservés ·
      <a href="/mentions-legales/">Mentions légales</a>
    </p>
  </div>
</footer>"""


def render(
    *,
    slug,
    title,
    description,
    body,
    breadcrumb=None,
    og_image="/assets/img/hero-mordant.jpg",
    extra_jsonld=None,
    body_class="",
):
    """Assemble une page complète.

    slug        : "" pour l'accueil, sinon "le-centre/" (avec slash final)
    breadcrumb  : liste de (libellé, url) sans l'accueil
    """
    url = "/" + slug
    canonical = BASE_URL + url

    graph = [_org_jsonld(), {
        "@type": "WebSite",
        "@id": f"{BASE_URL}/#site",
        "url": BASE_URL + "/",
        "name": SITE_NAME,
        "inLanguage": "fr-FR",
        "publisher": {"@id": f"{BASE_URL}/#organisation"},
    }]
    if breadcrumb:
        graph.append(_breadcrumb_jsonld(breadcrumb))
    if extra_jsonld:
        graph.extend(extra_jsonld)
    jsonld = json.dumps(
        {"@context": "https://schema.org", "@graph": graph},
        ensure_ascii=False, separators=(",", ":"),
    )

    header = HEADER_TPL % {"nav": _nav_html(url)}
    footer = FOOTER_TPL % ORG
    crumbs = _breadcrumb_html(breadcrumb)
    cls = f' class="{body_class}"' if body_class else ""

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="{'noindex, nofollow' if STAGING else 'index, follow, max-image-preview:large'}">
<meta name="author" content="{e(ORG['nom'])}">
<meta name="theme-color" content="#12160f">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="{e(SITE_NAME)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{BASE_URL}{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(description)}">
<meta name="twitter:image" content="{BASE_URL}{og_image}">
<link rel="icon" href="/assets/img/favicon.ico" sizes="any">
<link rel="icon" href="/assets/img/logo-32.png" type="image/png">
<link rel="apple-touch-icon" href="/assets/img/logo-180.png">
<link rel="stylesheet" href="/assets/style.css">
<script type="application/ld+json">{jsonld}</script>
</head>
<body{cls}>
{header}
{crumbs}
<main id="contenu">
{body}
</main>
{footer}
<script src="/assets/script.js" defer></script>
</body>
</html>
"""
