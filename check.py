#!/usr/bin/env python3
"""Contrôles de cohérence sur le site généré (liens, SEO, accessibilité).

    python3 check.py

À lancer après chaque build : c'est ce qui évite d'envoyer à l'association une
version avec des liens morts ou des balises SEO en double.
"""

import json
import os
import re
import sys
from collections import defaultdict
from html.parser import HTMLParser

DIST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")
# Même sous-chemin que le build (GitHub Pages projet, par exemple).
BASE_PATH = os.environ.get("CEUC_BASE_PATH", "").rstrip("/")

problems = []
warnings = []


class Doc(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.imgs = []
        self.h1 = []
        self.headings = []
        self.title = None
        self.description = None
        self.canonical = None
        self.jsonld = []
        self._in_title = False
        self._in_jsonld = False
        self._buf = []
        self._heading = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self._in_title = True
            self._buf = []
        elif tag == "a" and "href" in a:
            self.links.append(a["href"])
        elif tag == "img":
            self.imgs.append(a)
        elif tag == "meta" and a.get("name") == "description":
            self.description = a.get("content")
        elif tag == "link" and a.get("rel") == "canonical":
            self.canonical = a.get("href")
        elif tag == "script" and a.get("type") == "application/ld+json":
            self._in_jsonld = True
            self._buf = []
        elif tag in ("h1", "h2", "h3", "h4"):
            self._heading = tag
            self._buf = []

    def handle_endtag(self, tag):
        if tag == "title" and self._in_title:
            self.title = "".join(self._buf).strip()
            self._in_title = False
        elif tag == "script" and self._in_jsonld:
            self.jsonld.append("".join(self._buf))
            self._in_jsonld = False
        elif tag == self._heading:
            text = "".join(self._buf).strip()
            self.headings.append((tag, text))
            if tag == "h1":
                self.h1.append(text)
            self._heading = None

    def handle_data(self, d):
        if self._in_title or self._in_jsonld or self._heading:
            self._buf.append(d)


def url_to_file(url):
    """Traduit une URL du site vers le fichier attendu dans dist/."""
    path = url.split("#")[0].split("?")[0]
    if not path.startswith("/"):
        return None
    if BASE_PATH:
        if not path.startswith(BASE_PATH + "/") and path != BASE_PATH:
            return None  # lien absolu non préfixé : signalé plus bas
        path = path[len(BASE_PATH):] or "/"
    rel = path.lstrip("/")
    if rel == "" or rel.endswith("/"):
        return os.path.join(DIST, rel, "index.html")
    return os.path.join(DIST, rel)


def main():
    if not os.path.isdir(DIST):
        sys.exit("dist/ absent — lancer d'abord python3 build.py")

    docs = {}
    for root, _dirs, files in os.walk(DIST):
        for f in files:
            if not f.endswith(".html"):
                continue
            full = os.path.join(root, f)
            rel = "/" + os.path.relpath(full, DIST).replace(os.sep, "/")
            d = Doc()
            d.feed(open(full, encoding="utf-8").read())
            docs[rel] = d

    print(f"{len(docs)} pages analysées\n")

    titles = defaultdict(list)
    descs = defaultdict(list)

    for rel, d in sorted(docs.items()):
        # --- SEO de base
        if not d.title:
            problems.append(f"{rel} : <title> manquant")
        else:
            titles[d.title].append(rel)
            if len(d.title) > 65:
                warnings.append(f"{rel} : title de {len(d.title)} caractères (>65, risque de troncature)")
        if not d.description:
            problems.append(f"{rel} : meta description manquante")
        else:
            descs[d.description].append(rel)
            n = len(d.description)
            if n > 165:
                warnings.append(f"{rel} : description de {n} caractères (>165)")
            elif n < 70:
                warnings.append(f"{rel} : description de {n} caractères (<70, trop courte)")
        if not d.canonical:
            problems.append(f"{rel} : canonical manquant")

        # --- Structure de titres
        if len(d.h1) == 0:
            problems.append(f"{rel} : aucun <h1>")
        elif len(d.h1) > 1:
            problems.append(f"{rel} : {len(d.h1)} <h1> (un seul attendu)")

        levels = [int(t[1]) for t, _ in d.headings]
        for i in range(1, len(levels)):
            if levels[i] - levels[i - 1] > 1:
                warnings.append(
                    f"{rel} : saut de niveau h{levels[i-1]} → h{levels[i]}"
                )
                break

        # --- Images
        for img in d.imgs:
            if "alt" not in img:
                problems.append(f"{rel} : <img> sans attribut alt ({img.get('src')})")

        # --- JSON-LD
        for raw in d.jsonld:
            try:
                json.loads(raw)
            except json.JSONDecodeError as exc:
                problems.append(f"{rel} : JSON-LD invalide ({exc})")

        # --- Liens internes
        for href in d.links:
            if href.startswith(("http://", "https://", "mailto:", "tel:", "#")):
                continue
            target = url_to_file(href)
            if target is None:
                warnings.append(f"{rel} : lien relatif inattendu « {href} »")
            elif not os.path.exists(target):
                problems.append(f"{rel} : lien mort vers « {href} »")

    for title, urls in titles.items():
        if len(urls) > 1:
            problems.append(f"title dupliqué sur {urls} : « {title} »")
    for desc, urls in descs.items():
        if len(urls) > 1:
            problems.append(f"description dupliquée sur {urls}")

    # --- Fichiers SEO attendus
    for f in ("sitemap.xml", "robots.txt", "404.html"):
        if not os.path.exists(os.path.join(DIST, f)):
            problems.append(f"{f} manquant")

    # --- Le sitemap doit lister exactement les pages publiées
    sm = os.path.join(DIST, "sitemap.xml")
    if os.path.exists(sm):
        locs = re.findall(r"<loc>([^<]+)</loc>", open(sm, encoding="utf-8").read())
        published = {r for r in docs if r != "/404.html"}
        listed = set()
        for u in locs:
            path = "/" + u.split("/", 3)[3] if u.count("/") >= 3 else "/"
            if BASE_PATH and path.startswith(BASE_PATH):
                path = path[len(BASE_PATH):] or "/"
            listed.add(path + "index.html" if path.endswith("/") else path)
        missing = published - listed
        if missing:
            problems.append(f"absentes du sitemap : {sorted(missing)}")

    if warnings:
        print("AVERTISSEMENTS")
        for w in warnings:
            print(f"  · {w}")
        print()
    if problems:
        print("PROBLÈMES")
        for p in problems:
            print(f"  ✗ {p}")
        print(f"\n{len(problems)} problème(s), {len(warnings)} avertissement(s)")
        sys.exit(1)

    print(f"Aucun problème bloquant. {len(warnings)} avertissement(s).")


if __name__ == "__main__":
    main()
