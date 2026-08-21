"""Blocs de contenu réutilisables pour composer les pages."""

from template import e


def picture(name, alt, *, cls="", width=None, height=None, lazy=True, sizes=None):
    """<picture> WebP + repli JPEG. `name` = nom de fichier sans extension."""
    loading = 'loading="lazy" decoding="async"' if lazy else 'decoding="async"'
    dims = ""
    if width and height:
        dims = f' width="{width}" height="{height}"'
    sz = f' sizes="{sizes}"' if sizes else ""
    return (
        f'<picture class="{cls}">'
        f'<source srcset="/assets/img/{name}.webp" type="image/webp"{sz}>'
        f'<img src="/assets/img/{name}.jpg" alt="{e(alt)}"{dims} {loading}>'
        f"</picture>"
    )


def hero(*, eyebrow, title, lead, image, image_alt, primary, secondary=None, badges=None):
    """Hero d'accueil : texte à gauche, photo à droite."""
    btns = f'<a class="btn btn--primary" href="{primary[1]}">{e(primary[0])}</a>'
    if secondary:
        btns += f'<a class="btn btn--ghost" href="{secondary[1]}">{e(secondary[0])}</a>'
    badge_html = ""
    if badges:
        items = "".join(f"<li>{e(b)}</li>" for b in badges)
        badge_html = f'<ul class="hero__badges">{items}</ul>'
    return f"""<section class="hero">
  <div class="wrap hero__inner">
    <div class="hero__text">
      <p class="eyebrow">{e(eyebrow)}</p>
      <h1 class="hero__title">{title}</h1>
      <p class="hero__lead">{lead}</p>
      <div class="btn-row">{btns}</div>
      {badge_html}
    </div>
    <div class="hero__media">
      {picture(image, image_alt, cls="hero__pic", lazy=False, width=1000, height=563)}
    </div>
  </div>
</section>"""


def page_header(*, eyebrow, title, lead, image=None, image_alt=""):
    """Bandeau de titre des pages intérieures."""
    media = ""
    if image:
        media = f'<div class="page-head__media">{picture(image, image_alt, lazy=False)}</div>'
    return f"""<section class="page-head{' page-head--with-media' if image else ''}">
  <div class="wrap page-head__inner">
    <div class="page-head__text">
      <p class="eyebrow">{e(eyebrow)}</p>
      <h1>{title}</h1>
      <p class="lead">{lead}</p>
    </div>
    {media}
  </div>
</section>"""


def section(*, title=None, intro=None, content="", cls="", id=None, eyebrow=None):
    head = ""
    if title:
        eb = f'<p class="eyebrow">{e(eyebrow)}</p>' if eyebrow else ""
        it = f'<p class="section__intro">{intro}</p>' if intro else ""
        head = f'<div class="section__head">{eb}<h2>{title}</h2>{it}</div>'
    attrs = f' id="{id}"' if id else ""
    return f'<section class="section {cls}"{attrs}><div class="wrap">{head}{content}</div></section>'


def cards(items, *, cols=3):
    """items : liste de dicts {titre, texte, url, image, alt, tag}"""
    out = []
    for it in items:
        img = ""
        if it.get("image"):
            img = f'<div class="card__media">{picture(it["image"], it.get("alt", ""))}</div>'
        tag = f'<span class="card__tag">{e(it["tag"])}</span>' if it.get("tag") else ""
        link = it.get("url")
        arrow = (
            '<span class="card__more">En savoir plus'
            '<svg width="14" height="10" viewBox="0 0 14 10" aria-hidden="true">'
            '<path d="M9 1l4 4-4 4M13 5H1" fill="none" stroke="currentColor" '
            'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>'
        ) if link else ""
        inner = (
            f'{img}<div class="card__body">{tag}<h3 class="card__title">{it["titre"]}</h3>'
            f'<p class="card__text">{it["texte"]}</p>{arrow}</div>'
        )
        if link:
            out.append(f'<a class="card" href="{link}">{inner}</a>')
        else:
            out.append(f'<article class="card">{inner}</article>')
    return f'<div class="grid grid--{cols}">{"".join(out)}</div>'


def feature_rows(rows):
    """Alternance texte / image. rows : {titre, html, image, alt, url, cta}"""
    out = []
    for i, r in enumerate(rows):
        flip = " feature--flip" if i % 2 else ""
        cta = ""
        if r.get("url"):
            cta = f'<p class="feature__cta"><a class="btn btn--ghost btn--sm" href="{r["url"]}">{e(r.get("cta", "En savoir plus"))}</a></p>'
        out.append(f"""<div class="feature{flip}">
      <div class="feature__text"><h3>{r["titre"]}</h3>{r["html"]}{cta}</div>
      <div class="feature__media">{picture(r["image"], r.get("alt", ""))}</div>
    </div>""")
    return f'<div class="features">{"".join(out)}</div>'


def bullets(items, *, cls=""):
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f'<ul class="ticks {cls}">{lis}</ul>'


def stats(items):
    """items : liste de (valeur, libellé)"""
    out = "".join(
        f'<div class="stat"><span class="stat__value">{e(v)}</span>'
        f'<span class="stat__label">{e(l)}</span></div>'
        for v, l in items
    )
    return f'<div class="stats">{out}</div>'


def legal_note(text):
    return (
        f'<p class="legal-note"><span class="legal-note__icon" aria-hidden="true">§</span>'
        f"<span>{text}</span></p>"
    )


def callout(*, title, text, cta_label="Nous contacter", cta_url="/contact/", cls=""):
    return f"""<section class="callout {cls}">
  <div class="wrap callout__inner">
    <div>
      <h2>{title}</h2>
      <p>{text}</p>
    </div>
    <a class="btn btn--primary" href="{cta_url}">{e(cta_label)}</a>
  </div>
</section>"""


def modules(items):
    """Blocs « Module n°1 / n°2 » : {numero, titre, duree, html}"""
    out = []
    for m in items:
        duree = f'<span class="module__duree">{e(m["duree"])}</span>' if m.get("duree") else ""
        out.append(f"""<article class="module">
      <div class="module__head">
        <span class="module__num">{e(m["numero"])}</span>
        <h3 class="module__titre">{m["titre"]}</h3>
        {duree}
      </div>
      <div class="module__body">{m["html"]}</div>
    </article>""")
    return f'<div class="modules">{"".join(out)}</div>'


def team(members):
    out = []
    for m in members:
        roles = "".join(f"<li>{r}</li>" for r in m["roles"])
        out.append(f"""<article class="member">
      <div class="member__id">
        <span class="member__initial" aria-hidden="true">{e(m["prenom"][0])}</span>
        <div>
          <h3 class="member__nom">{e(m["prenom"])}</h3>
          <p class="member__fonction">{e(m["fonction"])}</p>
        </div>
      </div>
      <ul class="member__roles">{roles}</ul>
    </article>""")
    return f'<div class="team">{"".join(out)}</div>'


def photo_strip(items, *, title=None):
    """Bande de 2 ou 3 photos illustrant un thème.

    items : liste de (nom de fichier sans extension, légende).
    Les photos sont cliquables et rejoignent la visionneuse de la galerie.
    """
    figs = []
    for name, legende in items:
        figs.append(
            f'<figure class="strip__item">'
            f'<a href="/assets/img/{name}.jpg" class="gal__link" '
            f'aria-label="Agrandir : {e(legende)}">'
            f'{picture(name, legende, cls="strip__pic")}</a>'
            f'<figcaption class="strip__cap">{e(legende)}</figcaption></figure>'
        )
    head = f'<h3 class="strip__title">{title}</h3>' if title else ""
    return f'<div class="strip strip--{len(items)}">{head}{"".join(figs)}</div>'


def gallery(items):
    """items : liste de (index, légende)"""
    out = []
    for idx, legende in items:
        n = f"galerie-{idx:02d}"
        out.append(
            f'<figure class="gal__item">'
            f'<a href="/assets/img/{n}.jpg" class="gal__link" '
            f'aria-label="Agrandir : {e(legende)}">'
            f'{picture(n + "-thumb", legende, cls="gal__pic")}</a>'
            f'<figcaption class="gal__cap">{e(legende)}</figcaption></figure>'
        )
    return f'<div class="gal">{"".join(out)}</div>'


def faq(items):
    """items : liste de (question, réponse HTML). Génère aussi le JSON-LD associé."""
    out = "".join(
        f'<details class="faq__item"><summary>{e(q)}</summary><div class="faq__answer">{a}</div></details>'
        for q, a in items
    )
    return f'<div class="faq">{out}</div>'


def faq_jsonld(items):
    import re
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": re.sub(r"<[^>]+>", "", a).strip(),
                },
            }
            for q, a in items
        ],
    }
