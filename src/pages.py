"""Contenu de toutes les pages du site.

Chaque page expose : slug, title (SEO), description (meta), et le corps HTML.
Les textes reprennent ceux fournis par l'association, réécrits pour le web
et le référencement (mots-clés, structure de titres, maillage interne).
"""

from components import (
    bullets, callout, cards, faq, faq_jsonld, feature_rows, gallery, hero,
    legal_note, modules, page_header, photo_strip, picture, section, stats, team,
)
from template import BASE_URL, ORG, e

PAGES = []


def page(**kw):
    PAGES.append(kw)
    return kw


# ==========================================================================
# ACCUEIL
# ==========================================================================

FORMATIONS_CARDS = [
    {
        "titre": "Cynotechnicien de Police Municipale",
        "texte": "Formation initiale et continue des agents appelés à servir en brigade canine, adaptée aux prérogatives de la voie publique.",
        "url": "/formations/police-municipale/",
        "image": "formation-police-municipale",
        "alt": "Briefing d'une équipe cynophile de Police Municipale lors d'une formation CEUC",
        "tag": "Professionnels",
    },
    {
        "titre": "Stage de perfectionnement",
        "texte": "Journées intensives pour cynotechniciens, hommes d'attaque et instructeurs : mordant opérationnel, frappe muselée, progression tactique.",
        "url": "/formations/perfectionnement/",
        "image": "stage-perfectionnement",
        "alt": "Atelier de mordant opérationnel lors d'un stage de perfectionnement",
        "tag": "Professionnels",
    },
    {
        "titre": "Olfaction &amp; recherche",
        "texte": "Créancement des équipes cynophiles en recherche de personnes : décombres, avalanches, questage.",
        "url": "/formations/olfaction-detection/",
        "image": "olfaction-detection",
        "alt": "Chien de détection au travail lors d'un exercice d'olfaction",
        "tag": "Professionnels",
    },
    {
        "titre": "Capture de chiens errants et dangereux",
        "texte": "Formation de technicien de capture pour les collectivités, en deux modules, et convention de capture avec les communes.",
        "url": "/formations/capture-chien-dangereux/",
        "image": "capture-chien",
        "alt": "Technicien de capture manipulant un chien errant avec le matériel adapté",
        "tag": "Collectivités",
    },
    {
        "titre": "Permis de détention chien catégorisé",
        "texte": "Formation obligatoire des maîtres de chiens dits dangereux ou mordeurs, tout au long de l'année sur rendez-vous.",
        "url": "/particuliers/permis-chien-categorise/",
        "image": "particuliers-education",
        "alt": "Chien de type molossoïde tenu en laisse en extérieur",
        "tag": "Particuliers",
    },
]

ACCUEIL_FAQ = [
    (
        "Qui peut suivre une formation cynophile au CEUC ?",
        "<p>Nos formations professionnelles s'adressent aux agents de la fonction publique "
        "territoriale (Police Municipale), aux services de police, de sécurité et de secours, "
        "ainsi qu'à tout personnel d'un service d'ordre français ou étranger souhaitant obtenir "
        "une qualification dans la spécialité cynophile. Les particuliers sont accueillis pour "
        "le permis de détention de chiens catégorisés.</p>",
    ),
    (
        "Où se déroulent les formations ?",
        "<p>Le centre dispose d'un terrain aménagé à Meximieux, dans l'Ain (01), avec salle de "
        "cours, véhicules et hangar dédiés aux exercices. Les mises en situation ont également "
        "lieu sur des sites extérieurs, en milieu urbain et rural, de jour comme de nuit. Nous "
        "nous déplaçons aussi sur l'ensemble du territoire national et à l'international.</p>",
    ),
    (
        "Les formations peuvent-elles être financées ?",
        "<p>Oui. Les formations destinées aux policiers municipaux peuvent être prises en charge "
        "par la mairie d'affectation dans le cadre du plan de formation. Le CEUC est enregistré "
        f"comme organisme de formation sous le numéro {ORG['of']}.</p>",
    ),
    (
        "Le centre fournit-il des chiens déjà formés ?",
        "<p>Oui, sur demande et selon cahier des charges : chiens d'intervention et de détection "
        "pour les institutions publiques et privées, en France comme à l'étranger. Nous "
        "accompagnons également l'acquisition d'un chiot destiné à un travail utilitaire.</p>",
    ),
]

page(
    slug="",
    title="Formation cynophile professionnelle & Police Municipale | CEUC",
    description=(
        "Centre d'entraînement des unités cynophiles à Meximieux (01) : formation de "
        "cynotechniciens de Police Municipale, olfaction, capture et permis de détention."
    ),
    breadcrumb=None,
    extra_jsonld=[faq_jsonld(ACCUEIL_FAQ)],
    body=(
        hero(
            eyebrow="Meximieux · Ain · France entière",
            title="Formation cynophile professionnelle<br><span class='hl'>pour les unités de Police Municipale</span>",
            lead=(
                "Le <strong>CEUC</strong> est un centre d'instruction cynophile dédié aux "
                "professionnels des unités cynotechniques des administrations — Police "
                "Municipale, services de secours, sécurité publique et privée. "
                "<strong>Encadré uniquement par des policiers municipaux en exercice.</strong>"
            ),
            image="hero-rassemblement",
            image_alt=(
                "Rassemblement de cynotechniciens de Police Municipale lors d'une "
                "session de formation au CEUC"
            ),
            primary=("Découvrir les formations", "/formations/"),
            secondary=("Nous contacter", "/contact/"),
            badges=[
                "Organisme de formation enregistré",
                "Habilité DDPP & Préfecture de l'Ain",
                "Formateurs en activité",
            ],
        )
        + section(
            cls="section--tight section--stats",
            content=stats([
                ("100 %", "formateurs policiers municipaux en activité"),
                ("5", "formations professionnelles"),
                ("France & étranger", "zone d'intervention"),
            ]),
        )
        + section(
            eyebrow="Nos domaines",
            title="Des formations calées sur les réalités opérationnelles",
            intro=(
                "Chaque module est construit avec des instructeurs qui exercent au quotidien "
                "en unité cynotechnique. Pas de théorie hors-sol : du cadre légal, des mises "
                "en situation et des résultats mesurables sur le binôme maître-chien."
            ),
            content=cards(FORMATIONS_CARDS),
        )
        + section(
            cls="section--dark",
            eyebrow="Pourquoi le CEUC",
            title="Plus que des mots… des résultats",
            content=feature_rows([
                {
                    "titre": "Une équipe issue du terrain",
                    "html": (
                        "<p>L'équipe technique et pédagogique est composée exclusivement de "
                        "policiers municipaux en activité, titulaires des certificats de "
                        "capacité au mordant et à l'élevage canin, formateurs CNFPT et "
                        "conseillers techniques cynophiles auprès de l'Administration.</p>"
                        "<p>Des intervenants spécialisés issus de grandes unités "
                        "opérationnelles complètent les sessions pour apporter une "
                        "plus-value directe aux stagiaires.</p>"
                    ),
                    "image": "equipe-unite-cynophile",
                    "alt": "Écusson Unité Cynophile porté par un cynotechnicien de Police Municipale",
                    "url": "/le-centre/",
                    "cta": "Découvrir l'équipe",
                },
                {
                    "titre": "Des structures pensées pour le travail opérationnel",
                    "html": (
                        "<p>Terrain entièrement aménagé, véhicules et hangar dévolus aux "
                        "exercices, salle de cours, parcours de dextérité spécifique pour le "
                        "binôme maître-chien.</p>"
                        "<p>Le matériel dédié aux cynotechniciens de police et de sécurité "
                        "(radios, blue gun, ceinturon, carnets de notes) est mis à disposition "
                        "lors des mises en situation, menées en milieu urbain et rural, de "
                        "jour comme de nuit.</p>"
                    ),
                    "image": "structures-terrain",
                    "alt": "Véhicules et structures du centre d'entraînement cynophile de Meximieux",
                    "url": "/le-centre/#structures",
                    "cta": "Voir nos structures",
                },
                {
                    "titre": "Un réseau inter-administrations",
                    "html": (
                        "<p>Le centre organise des entraînements réunissant Police Nationale "
                        "et Municipale, Gendarmerie, Douanes, ERIS, SUGE, sapeurs-pompiers et "
                        "Armée de Terre.</p>"
                        "<p>Ces rassemblements permettent aux équipes de confronter leurs "
                        "pratiques et d'élargir leur champ d'expérience opérationnelle.</p>"
                    ),
                    "image": "rassemblement-inter-adm",
                    "alt": "Rassemblement cynotechnique zonal inter-administrations organisé par le CEUC",
                    "url": "/galerie/",
                    "cta": "Voir la galerie",
                },
            ]),
        )
        + section(
            eyebrow="Au-delà de la formation",
            title="Chiens, cinéma et prestations annexes",
            content=cards([
                {
                    "titre": "Création de brigade canine &amp; audits",
                    "texte": "Accompagnement des collectivités qui montent une unité cynophile de Police Municipale, et audit des brigades déjà en service.",
                    "url": "/creation-brigade-canine/",
                    "image": "seminaires-audits",
                    "alt": "Rassemblement cynotechnique inter-administrations organisé par le CEUC",
                },
                {
                    "titre": "Vente de chiens",
                    "texte": "Chiens testés et validés par un vétérinaire, formés à l'intervention ou à l'olfaction, pour les institutions publiques et privées.",
                    "url": "/vente-chiens/",
                    "image": "selection-chiens",
                    "alt": "Jeune chien de travail sélectionné par le CEUC",
                },
                {
                    "titre": "Tournages &amp; cinéma",
                    "texte": "Fourniture de chiens spécialement dressés pour le cinéma, la publicité et les séries. Références : « À toute épreuve », « La Vallée ».",
                    "url": "/cinema/",
                    "image": "cinema-tournage",
                    "alt": "Équipe cynophile du CEUC sur un tournage de long-métrage",
                },
                {
                    "titre": "Matériel &amp; alimentation",
                    "texte": "Alimentation canine, accessoires et équipement opérationnel à tarifs préférentiels, via nos partenaires spécialisés.",
                    "url": "/prestations/",
                    "image": "secourisme-intervention",
                    "alt": "Cynotechnicien équipé lors d'un exercice de recherche en bâtiment",
                },
            ]),
        )
        + section(
            cls="section--muted",
            eyebrow="Questions fréquentes",
            title="Vous vous demandez…",
            content=faq(ACCUEIL_FAQ),
        )
        + callout(
            title="Un projet de brigade canine ou une demande de formation&nbsp;?",
            text=(
                "Écrivez-nous ou appelez directement le centre : nous étudions chaque demande "
                "selon votre cahier des charges, en France comme à l'étranger."
            ),
        )
    ),
)


# ==========================================================================
# LE CENTRE
# ==========================================================================

MEMBRES = [
    {
        "prenom": "Anthony",
        "fonction": "Instructeur et responsable cynotechnique Police Municipale",
        "roles": [
            "Référent et formateur cynotechnique CNFPT",
            "Certificat de capacité pour le dressage des chiens au mordant",
            "Certificat de capacité au dressage et à l'élevage canin",
            "Formateur des propriétaires de chiens dangereux habilité DDPP",
            "Conseiller technique cynophile au profit de l'Administration",
            "Consultant et rédacteur de presse spécialisée",
        ],
    },
    {
        "prenom": "David",
        "fonction": "Formateur et cynotechnicien de Police Municipale",
        "roles": [
            "Référent Police spécialité patrouille",
            "Référent recherche de personnes",
        ],
    },
    {
        "prenom": "Maxime",
        "fonction": "Formateur cynotechnicien de Police Municipale",
        "roles": [
            "Référent cellule opérationnelle",
            "Formateur secourisme opérationnel",
        ],
    },
]

page(
    slug="le-centre/",
    title="Le centre CEUC : équipe, structures et partenaires | Meximieux",
    description=(
        "Une équipe de formateurs policiers municipaux en activité et des structures "
        "dédiées au travail des équipes cynophiles, à Meximieux dans l'Ain."
    ),
    breadcrumb=[("Le centre", "/le-centre/")],
    og_image="/assets/img/equipe-unite-cynophile.jpg",
    body=(
        page_header(
            eyebrow="Le centre",
            title="Un centre d'instruction cynophile encadré par des policiers municipaux",
            lead=(
                "Le CEUC forme les professionnels de la sécurité publique ayant une "
                "spécialisation canine, avec des instructeurs diplômés et habilités par les "
                "instances étatiques, qui exercent eux-mêmes en unité cynotechnique."
            ),
            image="malinois-police",
            image_alt=(
                "Chien de Police Municipale en harnais lors d'un entraînement au centre CEUC"
            ),
        )
        + section(
            eyebrow="Mieux nous connaître",
            title="L'équipe technique et pédagogique",
            intro=(
                "Une équipe restreinte et spécialisée, complétée par de nombreux intervenants "
                "issus de l'administration et de grandes unités opérationnelles afin "
                "d'apporter une plus-value réelle aux stagiaires."
            ),
            content=team(MEMBRES)
            + photo_strip([
                ("equipe-ceuc", "L'équipe du CEUC sur le terrain d'entraînement de Meximieux"),
                ("equipe-formateurs", "Trois formateurs du CEUC réunis sur le terrain d'entraînement"),
            ]),
        )
        + section(
            id="structures",
            cls="section--dark",
            eyebrow="Nos structures",
            title="Un outil de travail adapté aux équipes cynophiles",
            content=feature_rows([
                {
                    "titre": "Terrain, véhicules et salle de cours",
                    "html": (
                        "<p>Nos structures sont spécialement adaptées pour le travail des "
                        "équipes cynophiles : un terrain entièrement étudié et aménagé, avec "
                        "véhicules et hangar, une salle de cours et un bureau pour la partie "
                        "administrative.</p>"
                        "<p>Le matériel dédié aux cynotechniciens de police et de sécurité "
                        "<em>(radios, carnets de notes, blue gun, ceinturon…)</em> est "
                        "également à disposition lors des exercices de mise en situation.</p>"
                    ),
                    "image": "structures-terrain",
                    "alt": "Hangar et véhicules d'unité cynophile sur le terrain du CEUC",
                },
                {
                    "titre": "Des mises en situation variées",
                    "html": (
                        "<p>Les exercices ont lieu sur différentes structures "
                        "<em>(bâtiments, domaine public…)</em>, en milieu urbain et rural, de "
                        "jour et de nuit, afin de varier au maximum l'environnement de travail "
                        "et de répondre aux réalités de terrain.</p>"
                        "<p>Un parcours de dextérité spécifique est en place sur le terrain "
                        "d'entraînement : le binôme maître-chien s'y confronte pour conserver "
                        "les aptitudes physiques nécessaires à une qualité opérationnelle "
                        "optimale en mission.</p>"
                        "<p><strong>Le travail technique seul sur le chien n'est pas une "
                        "finalité en soi</strong> : c'est l'ensemble du travail, sur le "
                        "conducteur comme sur le chien, qui est un gage de performance "
                        "opérationnelle.</p>"
                    ),
                    "image": "secourisme-intervention",
                    "alt": "Exercice de recherche en bâtiment désaffecté avec un chien de police",
                },
            ]),
        )
        + section(
            eyebrow="Nos partenaires",
            title="Ils travaillent avec le centre",
            content=cards([
                {
                    "titre": "Kraken Tactical",
                    "texte": "Matériel opérationnel de qualité, adapté aux missions quotidiennes des professionnels de la sécurité. <a href=\"https://kraken-tactical.fr\" rel=\"noopener nofollow\" target=\"_blank\">kraken-tactical.fr</a>",
                },
                {
                    "titre": "La Prairie d'Ain",
                    "texte": "Éducation canine, gestion et résolution des problématiques comportementales, dans le département de l'Ain. <a href=\"https://www.laprairiedain.fr\" rel=\"noopener nofollow\" target=\"_blank\">laprairiedain.fr</a>",
                },
                {
                    "titre": "Vétérinaire partenaire habilité",
                    "texte": "Pour l'évaluation comportementale prévue par la réglementation sur les chiens catégorisés et mordeurs, nous vous orientons vers un vétérinaire habilité.",
                },
            ]),
        )
        + section(
            cls="section--muted section--tight",
            title="Références administratives",
            content=(
                "<div class='refs'>"
                f"<div class='ref'><span>Préfecture de l'Ain / DDPP</span><strong>{ORG['prefecture']}</strong></div>"
                f"<div class='ref'><span>SIRET</span><strong>{ORG['siret']}</strong></div>"
                f"<div class='ref'><span>Organisme de formation</span><strong>{ORG['of']}</strong></div>"
                "</div>"
            ),
        )
        + callout(
            title="Envie de visiter le centre&nbsp;?",
            text="Le terrain se situe chemin du Mortaray, à Meximieux (01). Contactez-nous pour convenir d'un rendez-vous.",
        )
    ),
)


# ==========================================================================
# FORMATIONS — HUB
# ==========================================================================

page(
    slug="formations/",
    title="Formations cynophiles professionnelles | CEUC Ain",
    description=(
        "Cynotechnicien de Police Municipale, perfectionnement, olfaction, capture de "
        "chiens dangereux, séminaires et secourisme SST : toutes nos formations."
    ),
    breadcrumb=[("Formations", "/formations/")],
    body=(
        page_header(
            eyebrow="Formations",
            title="Nos formations cynophiles professionnelles",
            lead=(
                "Le CEUC propose un panel de formations en concordance avec les réalités "
                "opérationnelles, du premier pas en unité cynophile au maintien des acquis "
                "des équipes déjà constituées."
            ),
        )
        + section(
            title="Nos domaines de formation",
            intro=(
                "Formations destinées aux professionnels et aux collectivités, ainsi qu'aux "
                "particuliers pour le permis de détention. Pour la création ou l'audit "
                "d'une brigade canine, voir la rubrique "
                "<a href='/creation-brigade-canine/'>Brigade canine</a>."
            ),
            content=cards(FORMATIONS_CARDS + [
                {
                    "titre": "Secourisme SST",
                    "texte": "Sauveteur Secouriste du Travail, formation initiale et recyclage pour les professionnels de la sécurité. Sur devis.",
                    "url": "/formations/sst-secourisme/",
                    "image": "secourisme-sst",
                    "alt": "Prise en charge d'une victime lors d'un exercice de secourisme opérationnel",
                    "tag": "Sur devis",
                },
            ]),
        )
        + section(
            cls="section--muted",
            title="Une pédagogie commune à tous nos modules",
            content=bullets([
                "<strong>Cadre légal d'abord</strong> — chaque geste technique est replacé dans les prérogatives et responsabilités de l'agent.",
                "<strong>Mises en situation systématiques</strong> — bâtiments, domaine public, milieu urbain et rural, de jour comme de nuit.",
                "<strong>Travail sur le conducteur autant que sur le chien</strong> — condition physique, positionnements, progressions tactiques.",
                "<strong>Modules adaptables</strong> — le contenu et la durée sont ajustés au niveau du stagiaire et à votre cahier des charges.",
                "<strong>Encadrement par des professionnels en activité</strong> — policiers municipaux et intervenants issus d'unités opérationnelles.",
            ]),
        )
        + callout(
            title="Vous ne trouvez pas le module recherché&nbsp;?",
            text="Nos formations sont modulables selon votre cahier des charges. Décrivez-nous votre besoin, nous construisons la session correspondante.",
        )
    ),
)


# ==========================================================================
# FORMATIONS — PAGES DÉTAIL
# ==========================================================================

def formation_page(*, slug, title, description, eyebrow, h1, lead, image, image_alt,
                   body, course, faq_items=None, callout_block=None):
    from template import _course_jsonld  # import local : évite un cycle à l'import
    extra = [_course_jsonld(course, "/" + slug)]
    faq_block = ""
    if faq_items:
        extra.append(faq_jsonld(faq_items))
        faq_block = section(
            cls="section--muted", title="Questions fréquentes", content=faq(faq_items)
        )
    page(
        slug=slug,
        title=title,
        description=description,
        breadcrumb=[("Formations", "/formations/"), (eyebrow, "/" + slug)],
        og_image=f"/assets/img/{image}.jpg",
        extra_jsonld=extra,
        body=(
            page_header(eyebrow="Formation", title=h1, lead=lead,
                        image=image, image_alt=image_alt)
            + body
            + faq_block
            + (callout_block if callout_block is not None else callout(
                title="Intéressé par cette formation&nbsp;?",
                text="Contactez le centre pour connaître les prochaines sessions, les modalités et les possibilités de prise en charge.",
                cta_label="Demander un renseignement",
            ))
        ),
    )


formation_page(
    slug="formations/police-municipale/",
    title="Formation cynotechnicien de Police Municipale | CEUC",
    description=(
        "Formation initiale et continue de cynotechnicien de Police Municipale : cadre "
        "légal, technicité et mises en situation, encadrées par des policiers municipaux."
    ),
    eyebrow="Cynotechnicien Police Municipale",
    h1="Formation cynotechnicien de Police Municipale",
    lead=(
        "Une formation spécifique aux policiers municipaux appelés à exercer au sein d'une "
        "brigade canine ou d'une unité cynophile, adaptée aux particularités de la voie "
        "publique et au cadre légal de leurs prérogatives."
    ),
    image="formation-police-municipale",
    image_alt="Briefing d'une équipe cynophile de Police Municipale lors d'une formation CEUC",
    course={
        "nom": "Formation cynotechnicien de Police Municipale",
        "description": (
            "Formation initiale et continue des policiers municipaux appelés à exercer en "
            "brigade canine : module théorique sur le cadre juridique de l'utilisation du "
            "chien et module pratique de mise en situation."
        ),
    },
    body=(
        section(
            title="Les trois niveaux de formation",
            intro=(
                "Nos formations sont adaptées spécifiquement aux particularités de la voie "
                "publique, dans le respect du cadre légal et des prérogatives des policiers "
                "municipaux, le tout dans un esprit qualitatif répondant aux exigences "
                "opérationnelles de terrain."
            ),
            content=modules([
                {
                    "numero": "01",
                    "titre": "Formation initiale",
                    "duree": "2 modules",
                    "html": (
                        "<p>Un <strong>module théorique</strong> pour apprendre les bases "
                        "juridiques sur l'utilisation d'un chien de service.</p>"
                        "<p>Un <strong>module pratique</strong> où le stagiaire apprend les "
                        "technicités de la spécialité à travers des mises en situation "
                        "réalistes.</p>"
                    ),
                },
                {
                    "numero": "02",
                    "titre": "Formation continue",
                    "duree": "Entraînements périodiques",
                    "html": (
                        "<p>Assure le suivi et le maintien opérationnel des maîtres-chiens "
                        "par le biais d'entraînements périodiques, en concordance avec les "
                        "réalités opérationnelles rencontrées sur le terrain.</p>"
                    ),
                },
                {
                    "numero": "03",
                    "titre": "Stage de perfectionnement",
                    "duree": "1 semaine intensive",
                    "html": (
                        "<p>Permet de consolider ses acquis et de progresser à travers un "
                        "stage intensif d'une semaine.</p>"
                        "<p><a href='/formations/perfectionnement/'>Voir le détail du stage "
                        "de perfectionnement →</a></p>"
                    ),
                },
            ]),
        )
        + section(
            cls="section--dark",
            title="Pré-requis",
            content=bullets([
                "Être titulaire d'un poste au sein de la Police Municipale",
                "Posséder un chien de service à jour administrativement",
                "Avoir une condition physique de niveau correct",
            ]),
        )
        + section(
            title="Ouverture et financement",
            content=(
                "<p>Cette formation est ouverte aux agents de la fonction publique "
                "territoriale ainsi qu'à tout personnel d'un service d'ordre et de police "
                "étranger souhaitant obtenir une qualification dans la spécialité cynophile.</p>"
                "<p>L'ensemble de ces formations peut être financé dans le cadre du plan de "
                "formation, avec une prise en charge par la mairie d'affectation.</p>"
                "<p class='accent-line'><strong>Encadrement assuré uniquement par des "
                "policiers municipaux en activité.</strong></p>"
                + legal_note(
                    "Références législatives : Loi n°99-291 du 15 avril 1999 · "
                    "Décret n°2004-102 du 30 janvier 2004 · Décret n°2012-2 du 2 janvier 2012 · "
                    "Décret n°2022-210 du 18 février 2022."
                )
            ),
        )
        + section(
            content=photo_strip([
                ("police-municipale-01",
                 "Briefing d'un instructeur cynotechnique avec une équipe de Police Municipale"),
                ("police-municipale-02",
                 "Mise en situation d'intervention en bâtiment de nuit"),
                ("police-municipale-03",
                 "Progression d'une équipe cynophile avec son chien en intérieur"),
            ], title="En images", captions=False),
            cls="section--tight",
        )
    ),
    faq_items=[
        (
            "Faut-il déjà posséder un chien pour suivre la formation ?",
            "<p>Oui, la formation initiale suppose que l'agent dispose d'un chien de service "
            "à jour administrativement. Si votre collectivité crée sa brigade canine, nous "
            "pouvons vous accompagner en amont sur la sélection du chien.</p>",
        ),
        (
            "Quelle est la durée de la formation initiale ?",
            "<p>La durée est adaptée au niveau du stagiaire et du binôme. Elle se compose "
            "d'un module théorique et d'un module pratique, dont le volume horaire est défini "
            "après échange sur votre situation.</p>",
        ),
        (
            "La formation est-elle ouverte aux agents étrangers ?",
            "<p>Oui. Elle est ouverte à tout personnel d'un service d'ordre et de police "
            "étranger souhaitant obtenir une qualification dans la spécialité cynophile.</p>",
        ),
    ],
)


formation_page(
    slug="formations/perfectionnement/",
    title="Stage de perfectionnement cynotechnique | CEUC",
    description=(
        "Stages pour cynotechniciens, hommes d'attaque et instructeurs : frappe muselée, "
        "mordant opérationnel, détection et progressions tactiques."
    ),
    eyebrow="Stage de perfectionnement",
    h1="Stage de perfectionnement cynotechnique",
    lead=(
        "Des journées de travail sur des thématiques spécifiques, dédiées exclusivement aux "
        "professionnels de la cynotechnie, dans une optique de perfectionnement opérationnel."
    ),
    image="stage-perfectionnement",
    image_alt="Atelier de mordant opérationnel lors d'un stage de perfectionnement au CEUC",
    course={
        "nom": "Stage de perfectionnement cynotechnique",
        "description": (
            "Stage destiné aux cynotechniciens, assistants, hommes d'attaque et instructeurs "
            "d'institutions publiques et privées : frappe muselée, mordant opérationnel, "
            "détection, parcours de dextérité, progressions tactiques et cadre légal."
        ),
    },
    body=(
        section(
            title="À qui s'adresse le stage",
            content=(
                "<p>Ces stages sont ouverts aux <strong>cynotechniciens, assistants, hommes "
                "d'attaque et instructeurs</strong> d'institutions privées et publiques, ainsi "
                "qu'aux chiens de service administratifs et personnels, à jour "
                "administrativement.</p>"
                "<p>Notre centre les organise <strong>tout au long de l'année</strong>, avec "
                "des thématiques choisies en lien avec la fonction du participant.</p>"
            ),
        )
        + section(
            cls="section--dark",
            title="Les domaines abordés",
            intro=(
                "Différents modules sont mis en place, en concordance avec les réalités de "
                "terrain rencontrées par les équipes en mission."
            ),
            content=bullets([
                "Atelier de <strong>frappe muselée</strong>",
                "<strong>Mordant opérationnel</strong>",
                "<strong>Détection</strong> et travail olfactif",
                "<strong>Parcours de dextérité</strong> pour le binôme maître-chien",
                "<strong>Positionnements</strong> et gestion de l'espace",
                "<strong>Progressions tactiques</strong>",
                "<strong>Cadre légal d'intervention</strong>",
            ]),
        )
        + section(
            title="Encadrement",
            content=(
                "<p>Les sessions sont encadrées par l'équipe technique et pédagogique du "
                "CEUC, composée uniquement de <strong>policiers municipaux disposant d'une "
                "forte expérience</strong> dans la formation et l'encadrement "
                "cynotechnique.</p>"
                "<p><a href='/le-centre/'>Découvrir l'équipe du centre →</a></p>"
            )
            + photo_strip([
                ("perfectionnement-03",
                 "Exercice de mordant opérationnel de nuit, sous hangar, lors d'un stage de perfectionnement"),
                ("perfectionnement-04",
                 "Séance théorique et briefing cartographique en salle lors d'un stage de perfectionnement"),
                ("perfectionnement-05",
                 "Mise en situation d'interpellation de nuit avec appui du chien lors d'un stage de perfectionnement"),
            ], title="En images", captions=False),
        )
    ),
)


formation_page(
    slug="formations/olfaction-detection/",
    title="Formation olfaction : recherche de personnes et détection | CEUC",
    description=(
        "Formation des équipes cynophiles à l'olfaction : recherche de personnes en "
        "décombres, avalanches et questage."
    ),
    eyebrow="Olfaction & recherche",
    h1="Formation olfaction, recherche et détection",
    lead=(
        "Le CEUC forme les équipes cynophiles et les chiens spécialisés dans les différentes "
        "spécialités olfactives, avec un créancement adapté à votre cahier des charges."
    ),
    image="olfaction-detection",
    image_alt="Chien de détection au travail lors d'un exercice d'olfaction encadré par le CEUC",
    course={
        "nom": "Formation olfaction et détection",
        "description": (
            "Formation des équipes cynophiles en recherche de personnes : décombres, "
            "avalanches et questage."
        ),
    },
    body=(
        section(
            title="Les spécialités enseignées",
            content=cards([
                {
                    "titre": "Recherche de personnes",
                    "texte": "Décombres, avalanches, questage — pour les équipes des services de secours et de sécurité publique.",
                },
                {
                    "titre": "Autres spécificités",
                    "texte": "Toute demande particulière peut être étudiée : créancement sur un ou plusieurs produits selon vos besoins.",
                },
                {
                    "titre": "Fourniture de chiens créancés",
                    "texte": "Sur demande, nous fournissons également des chiens formés dans toutes les spécialités olfactives. <a href=\"/vente-chiens/\">Voir la sélection →</a>",
                },
            ], cols=3),
        )
        + section(
            content=photo_strip([
                ("recherche-personne",
                 "Chien de recherche de personne au travail sur longe, en milieu naturel"),
            ], title="En images"),
            cls="section--tight",
        )
        + section(
            cls="section--dark section--tight",
            content=(
                "<p class='big-quote'>Toutes ces formations sont modulables en fonction de "
                "votre cahier des charges.</p>"
            ),
        )
    ),
)


formation_page(
    slug="formations/capture-chien-dangereux/",
    title="Formation capture de chiens errants et dangereux | CEUC",
    description=(
        "Formation de technicien de capture en deux modules (15 h et 7 h) et convention "
        "de capture pour les communes sans fourrière municipale."
    ),
    eyebrow="Capture de chiens dangereux",
    h1="Formation à la capture de chiens errants et dangereux",
    lead=(
        "Une formation destinée aux agents des collectivités confrontés à la divagation "
        "animale, complétée par une possibilité de convention de capture avec le centre."
    ),
    image="capture-chien",
    image_alt="Technicien de capture manipulant un chien errant avec le matériel adapté",
    course={
        "nom": "Formation technicien de capture de chiens errants et dangereux",
        "description": (
            "Formation élémentaire de technicien de capture (15 h) et stage de recyclage "
            "(7 h) : cadre de la détention des chiens, droits et obligations des "
            "propriétaires, technique de capture et manipulation du matériel."
        ),
    },
    body=(
        section(
            title="Deux modules possibles",
            content=modules([
                {
                    "numero": "01",
                    "titre": "Formation élémentaire de technicien de capture",
                    "duree": "15 heures",
                    "html": (
                        "<p>Formation relative à la détention des chiens <em>(dangereux ou "
                        "non)</em>, aux droits et obligations des propriétaires et au domaine "
                        "général de la cynotechnie.</p>"
                        "<p>Technique de capture, manipulation du matériel de capture et mises "
                        "en situation mettant en avant les différents cas de figure rencontrés "
                        "lors de divagations ou de réquisitions.</p>"
                    ),
                },
                {
                    "numero": "02",
                    "titre": "Stage de recyclage",
                    "duree": "7 heures",
                    "html": "<p>Remise à niveau des acquis du module n°1.</p>",
                },
            ]),
        )
        + section(
            cls="section--dark",
            title="Convention de capture avec les communes",
            content=(
                "<p>Les communes ne disposant pas de fourrière municipale ou de lieu de "
                "transit temporaire des animaux de compagnie <em>(article L.911-24 du Code "
                "Rural)</em> peuvent faire appel à notre centre cynotechnique.</p>"
                "<p>Une <strong>convention de capture</strong> peut être mise en place entre "
                "la commune et le centre <em>(article L.911-27 du Code Rural)</em>. Elle fait "
                "intervenir, selon ses modalités, un <strong>technicien de capture "
                "spécialement formé</strong>, assurant une prise en charge rapide et sécurisée "
                "de l'animal.</p>"
                + legal_note(
                    "Référence législative : Code Rural — Livre IX — Annexe II à "
                    "l'ordonnance n°2000-550 du 15 juin 2000."
                )
            ),
        )
    ),
    faq_items=[
        (
            "Notre commune n'a pas de fourrière, que faire en cas de divagation ?",
            "<p>Une convention de capture peut être signée entre votre commune et le centre, "
            "conformément à l'article L.911-27 du Code Rural. Un technicien de capture formé "
            "intervient alors selon les modalités définies dans la convention.</p>",
        ),
        (
            "Qui peut suivre la formation de technicien de capture ?",
            "<p>Elle s'adresse aux agents des collectivités territoriales amenés à intervenir "
            "sur des situations de divagation ou sur réquisition : police municipale, services "
            "techniques, agents de fourrière.</p>",
        ),
    ],
)


formation_page(
    slug="formations/sst-secourisme/",
    title="Formation SST et recyclage — sur devis | CEUC",
    description=(
        "Formation Sauveteur Secouriste du Travail et recyclage pour les professionnels "
        "de la sécurité publique et privée. Demandez votre devis au CEUC."
    ),
    eyebrow="Secourisme SST",
    h1="Formation SST et recyclage",
    lead=(
        "Sauveteur Secouriste du Travail, formation initiale et recyclage, pour les "
        "professionnels de la sécurité publique et privée ainsi que les utilisateurs de "
        "chiens de service."
    ),
    image="secourisme-sst",
    image_alt="Prise en charge d'une victime lors d'un exercice de secourisme opérationnel",
    course={
        "nom": "Formation SST — Sauveteur Secouriste du Travail et recyclage",
        "description": (
            "Formation Sauveteur Secouriste du Travail, initiale et recyclage, destinée "
            "aux professionnels de la sécurité publique et privée, sur devis."
        ),
    },
    body=(
        section(
            title="Deux formats",
            content=modules([
                {
                    "numero": "01",
                    "titre": "Formation initiale",
                    "duree": None,
                    "html": (
                        "<p>Gestes de premiers secours et rôle du sauveteur secouriste dans "
                        "le cadre professionnel, avec une approche adaptée aux contraintes "
                        "des métiers de la sécurité.</p>"
                    ),
                },
                {
                    "numero": "02",
                    "titre": "Recyclage",
                    "duree": None,
                    "html": (
                        "<p>Maintien et actualisation des compétences, avec révision des "
                        "gestes et mises en situation.</p>"
                    ),
                },
            ]),
        )
    ),
    callout_block=callout(
        title="Demandez votre devis SST",
        text=(
            "Indiquez-nous le nombre d'agents à former et le format souhaité "
            "(initiale ou recyclage) : nous vous adressons une proposition chiffrée."
        ),
        cta_label="Demander un devis",
    ),
)


# ==========================================================================
# BRIGADE CANINE (rubrique autonome, hors « Formations »)
# ==========================================================================

from template import _course_jsonld  # noqa: E402

BRIGADE_FAQ = [
    (
        "Par où commencer pour créer une brigade canine ?",
        "<p>Par un échange sur votre contexte : effectif de la Police Municipale, "
        "missions visées, moyens matériels et budget. Nous vous indiquons ensuite les "
        "étapes réglementaires, le profil de chien adapté et le parcours de formation "
        "de l'agent.</p>",
    ),
    (
        "Peut-on auditer une brigade canine déjà en service ?",
        "<p>Oui. L'audit porte sur les pratiques, le matériel, les procédures et la "
        "conformité au cadre légal, et se conclut par des préconisations concrètes.</p>",
    ),
    (
        "Intervenez-vous en dehors du département de l'Ain ?",
        "<p>Oui, sur l'ensemble du territoire national et à l'international. "
        "Déplacement toutes distances.</p>",
    ),
]

page(
    slug="creation-brigade-canine/",
    title="Création de brigade canine de Police Municipale & audit | CEUC",
    description=(
        "Créer une brigade canine de Police Municipale conforme au cadre légal, auditer "
        "une unité existante, organiser un séminaire à thèmes."
    ),
    breadcrumb=[("Brigade canine", "/creation-brigade-canine/")],
    og_image="/assets/img/seminaires-audits.jpg",
    extra_jsonld=[
        _course_jsonld({
            "nom": "Création de brigade canine de Police Municipale et audit",
            "description": (
                "Accompagnement des collectivités dans la création d'une unité cynophile "
                "de Police Municipale, audit de brigade existante, séminaires à thèmes, "
                "colloques et démonstrations."
            ),
        }, "/creation-brigade-canine/"),
        faq_jsonld(BRIGADE_FAQ),
    ],
    body=(
        page_header(
            eyebrow="Brigade canine",
            title="Création de brigade canine de Police Municipale et audit",
            lead=(
                "Toute notre expérience et notre technicité au service de la collectivité, "
                "pour obtenir une brigade canine qui respecte le cadre légal et reste en "
                "adéquation avec la réalité opérationnelle."
            ),
            image="seminaires-audits",
            image_alt="Rassemblement cynotechnique inter-administrations organisé par le CEUC",
        )
        + section(
            title="Nos interventions",
            content=cards([
                {
                    "titre": "Création de brigade canine",
                    "texte": "Accompagnement de la collectivité de la réflexion initiale à la mise en service opérationnelle, dans le respect du cadre légal.",
                },
                {
                    "titre": "Audits d'unité existante",
                    "texte": "Analyse des pratiques, du matériel et des procédures d'une unité cynophile en place, avec préconisations concrètes.",
                },
                {
                    "titre": "Séminaires à thèmes",
                    "texte": "Olfaction, intervention… avec une étude spécifique construite en concordance avec votre demande.",
                },
                {
                    "titre": "Colloques et démonstrations",
                    "texte": "Interventions au sein de votre structure, en présence de collaborateurs privilégiés issus d'unités spécialisées.",
                },
            ], cols=2),
        )
        + section(
            cls="section--dark section--tight",
            content=(
                "<p class='big-quote'>Le CEUC intervient sur l'ensemble du territoire "
                "national mais aussi à l'international, au bénéfice des institutions "
                "publiques et privées — forces de l'ordre, services de sécurité, services "
                "de secours. <strong>Déplacement toutes distances.</strong></p>"
            ),
        )
        + section(
            title="Et ensuite ?",
            content=(
                "<p>Une fois la brigade créée, le centre assure la suite du parcours : "
                "<a href='/formations/police-municipale/'>formation du cynotechnicien</a>, "
                "<a href='/vente-chiens/'>sélection du chien de service</a> et "
                "<a href='/formations/perfectionnement/'>maintien opérationnel du "
                "binôme</a>.</p>"
            ),
        )
        + section(cls="section--muted", title="Questions fréquentes",
                  content=faq(BRIGADE_FAQ))
        + callout(
            title="Un projet de brigade canine dans votre commune&nbsp;?",
            text=(
                "Présentez-nous votre contexte et vos contraintes : nous étudions la "
                "faisabilité et construisons l'accompagnement correspondant."
            ),
            cta_label="Parler de votre projet",
        )
    ),
)


# ==========================================================================
# PARTICULIERS
# ==========================================================================

PARTICULIERS_FAQ = [
    (
        "Le stage est-il obligatoire ?",
        "<p>Oui. La formation des maîtres de chiens catégorisés est obligatoire pour "
        "l'obtention du permis de détention. Elle peut également être imposée par le maire ou "
        "le préfet au propriétaire d'un chien mordeur, quelle qu'en soit la race.</p>",
    ),
    (
        "Dois-je venir avec mon chien ?",
        "<p>Non, le stage peut être réalisé avec ou sans chien. Précisez-le simplement lors "
        "de la prise de rendez-vous.</p>",
    ),
    (
        "Quand ont lieu les sessions ?",
        "<p>La formation est dispensée tout au long de l'année, sur simple rendez-vous. "
        "Contactez le centre pour convenir d'une date.</p>",
    ),
    (
        "L'évaluation comportementale est-elle comprise ?",
        "<p>Non, elle est réalisée par un vétérinaire. Nous pouvons vous orienter vers un "
        "vétérinaire partenaire habilité pour cette étape complémentaire.</p>",
    ),
]

page(
    slug="particuliers/permis-chien-categorise/",
    title="Permis de détention chien catégorisé — formation | CEUC Ain",
    description=(
        "Formation obligatoire des maîtres de chiens catégorisés à Meximieux (01). "
        "Stage avec ou sans chien, toute l'année sur rendez-vous."
    ),
    breadcrumb=[("Particuliers", "/particuliers/permis-chien-categorise/")],
    og_image="/assets/img/particuliers-education.jpg",
    extra_jsonld=[faq_jsonld(PARTICULIERS_FAQ)],
    body=(
        page_header(
            eyebrow="Particuliers",
            title="Formation pour le permis de détention d'un chien catégorisé",
            lead=(
                "Le CEUC dispense la formation des maîtres de chiens catégorisés, "
                "<strong>obligatoire</strong> pour l'obtention du permis de détention des "
                "chiens dits « dangereux » et/ou « mordeurs »."
            ),
            image="particuliers-education",
            image_alt="Chien de type molossoïde tenu en laisse, concerné par la réglementation sur les chiens catégorisés",
        )
        + section(
            title="Ce que dit la réglementation",
            content=(
                "<p>Applicable depuis le 1<sup>er</sup> janvier 2010, ce stage d'aptitude est "
                "impératif. Il peut également être <strong>imposé par le maire ou le préfet</strong> "
                "à un propriétaire de chien mordeur, quelle qu'en soit la race, en complément "
                "de l'évaluation comportementale réalisée par le vétérinaire.</p>"
                + legal_note(
                    "Référence législative : Loi n°2008-582 du 20 juin 2008 venant renforcer "
                    "la Loi n°99-5 du 6 janvier 1999."
                )
            ),
        )
        + section(
            cls="section--dark",
            title="Comment se déroule le stage",
            content=bullets([
                "<strong>Avec ou sans votre chien</strong> — les deux formats sont possibles.",
                "<strong>Toute l'année sur simple rendez-vous</strong> — pas d'attente d'une session groupée.",
                "<strong>Encadré par un formateur habilité DDPP</strong> pour les propriétaires de chiens dangereux.",
                "<strong>Orientation vers un vétérinaire partenaire habilité</strong> pour l'évaluation comportementale.",
            ]),
        )
        + section(
            title="Besoin de cours d'éducation canine ?",
            content=(
                "<p>Pour toute demande de cours d'éducation canine — gestion et résolution "
                "des problématiques comportementales — nous vous invitons à contacter notre "
                "partenaire <strong>La Prairie d'Ain</strong>, des professionnels sérieux et "
                "compétents situés dans le département de l'Ain.</p>"
                "<p><a class='btn btn--ghost btn--sm' href='https://www.laprairiedain.fr' "
                "rel='noopener nofollow' target='_blank'>Visiter laprairiedain.fr</a></p>"
                "<p>N'hésitez pas à les contacter de notre part.</p>"
            ),
        )
        + section(cls="section--muted", title="Questions fréquentes",
                  content=faq(PARTICULIERS_FAQ))
        + callout(
            title="Prendre rendez-vous pour votre stage",
            text="Appelez le centre ou envoyez-nous un message : nous fixons une date adaptée à votre situation.",
        )
    ),
)


# ==========================================================================
# CHIENS
# ==========================================================================

page(
    slug="vente-chiens/",
    title="Vente de chiens de travail pour police et sécurité | CEUC",
    description=(
        "Vente de chiens formés à l'intervention et à l'olfaction pour les institutions "
        "publiques et privées, et accompagnement à l'acquisition d'un chiot utilitaire."
    ),
    breadcrumb=[("Vente de chiens", "/vente-chiens/")],
    og_image="/assets/img/selection-chiens.jpg",
    body=(
        page_header(
            eyebrow="Vente de chiens",
            title="Vente et sélection de chiens de travail",
            lead=(
                "Une sélection rigoureuse et adaptée à chaque demande des administrations : "
                "chien testé à plusieurs reprises et validé par un vétérinaire."
            ),
            image="selection-chiens",
            image_alt="Jeune chien de travail sélectionné par le CEUC",
        )
        + section(
            title="Pour les institutions publiques et privées",
            content=(
                "<p>Le CEUC propose, sur demande, des chiens formés aux différentes "
                "spécialités <em>(intervention, olfaction)</em> pour les institutions "
                "publiques et privées : services de police, de sécurité, de secours, armée.</p>"
                "<p>Un programme précis peut être mis en place par le biais d'un "
                "<strong>cahier des charges</strong> établi en fonction de vos souhaits.</p>"
            )
            + bullets([
                "Chiens issus de <strong>lignées de travail</strong>",
                "Testés à plusieurs reprises et <strong>validés par un vétérinaire</strong>",
                "Identifiés par tatouage ou transpondeur électronique, vaccins à jour",
                "Formés à l'intervention ou créancés en olfaction selon vos besoins",
                "Fourniture <strong>en France et à l'étranger</strong>",
            ]),
        )
        + section(
            cls="section--dark",
            title="Acquisition d'un chiot utilitaire",
            content=(
                "<p>Nous sommes également à votre disposition dans le cadre de l'acquisition "
                "d'un chiot destiné à un travail utilitaire, en le <strong>sélectionnant pour "
                "vous</strong> selon les critères de votre future mission.</p>"
                "<p>Cette sélection en amont évite les erreurs de casting coûteuses : un "
                "chiot mal orienté représente des mois de travail perdus pour l'unité.</p>"
            ),
        )
        + section(
            cls="section--muted",
            title="Chiens récemment placés",
            intro=(
                "Un aperçu des profils que nous sélectionnons et des structures qui nous font "
                "confiance."
            ),
            content=cards([
                {
                    "titre": "Berger Belge Malinois — 12 mois",
                    "texte": "LOF, origines 100 % travail, sélectionné auprès de l'élevage du « Petit Pic ». Idéal olfaction (stupéfiants, explosifs) et patrouille-intervention. Très joueur, très stable.",
                    "tag": "Vendu — usage professionnel",
                },
                {
                    "titre": "Berger Belge Malinois — 10 mois",
                    "texte": "Chien dynamique, dans la sollicitation, joueur, disposant de bonnes dispositions au travail et au sport.",
                    "tag": "Vendu — 132ᵉ Bataillon Cynophile de l'Armée de Terre",
                },
                {
                    "titre": "Berger Hollandais — 5 mois",
                    "texte": "LOF, issu de l'élevage des « Crocs de l'Olympe ». Inscrit au LOF, identifié, vaccins à jour. Destiné à un peloton cynotechnique de sapeurs-pompiers en recherche en décombres.",
                    "tag": "Vendu — pratique sportive en famille",
                },
            ]),
        )
        + callout(
            title="Un besoin précis en chien de travail&nbsp;?",
            text="Décrivez-nous la mission visée et vos contraintes : nous construisons le cahier des charges et lançons la recherche.",
            cta_label="Décrire mon besoin",
        )
    ),
)


# ==========================================================================
# CINÉMA
# ==========================================================================

page(
    slug="cinema/",
    title="Chiens dressés pour le cinéma et la publicité | CEUC",
    description=(
        "Chiens spécialement dressés pour les tournages de longs-métrages, publicités et "
        "séries. Références : « À toute épreuve » et « La Vallée »."
    ),
    breadcrumb=[("Cinéma", "/cinema/")],
    og_image="/assets/img/cinema-tournage.jpg",
    body=(
        page_header(
            eyebrow="Cinéma",
            title="Chiens dressés pour le cinéma, la publicité et les séries",
            lead=(
                "Le CEUC met son expérience du chien de travail au service des productions "
                "audiovisuelles ayant besoin de chiens spécialement dressés."
            ),
            image="cinema-tournage",
            image_alt="Équipe cynophile du CEUC sur un tournage de long-métrage",
        )
        + section(
            title="Nos références",
            content=cards([
                {
                    "titre": "« À toute épreuve »",
                    "texte": "Long-métrage réalisé par Antoine Blossier, avec la participation de chiens de notre structure.",
                    "tag": "Long-métrage",
                },
                {
                    "titre": "« La Vallée »",
                    "texte": "Tournage réalisé en Suisse, mettant en avant plusieurs scènes avec des chiens du centre.",
                    "tag": "Long-métrage",
                },
                {
                    "titre": "Court-métrage 2009",
                    "texte": "Première collaboration du centre à une réalisation, dans le cadre d'un reportage de lycée professionnel.",
                    "tag": "Court-métrage",
                },
            ]),
        )
        + section(
            cls="section--dark",
            title="Comment nous travaillons avec les productions",
            content=bullets([
                "<strong>Étude de la demande</strong> — scènes envisagées, comportements attendus, contraintes de plateau.",
                "<strong>Sélection du chien adapté</strong> — tempérament, morphologie, capacité à travailler sous projecteurs et en nocturne.",
                "<strong>Présence d'un cynotechnicien sur le tournage</strong> — sécurité de l'équipe et bien-être de l'animal.",
                "<strong>Déplacement France et étranger</strong> — comme lors du tournage de « La Vallée » en Suisse.",
            ]),
        )
        + callout(
            title="Un projet de tournage avec des chiens&nbsp;?",
            text="Notre équipe reste à votre disposition afin d'étudier toute demande spécifique, en France comme à l'étranger.",
            cta_label="Parler de votre projet",
        )
    ),
)


# ==========================================================================
# PRESTATIONS ANNEXES
# ==========================================================================

page(
    slug="prestations/",
    title="Alimentation canine, accessoires et matériel | CEUC",
    description=(
        "Vente d'alimentation canine (gamme Purina), d'accessoires canins et de matériel "
        "opérationnel à tarifs préférentiels pour les équipes cynophiles."
    ),
    breadcrumb=[("Prestations annexes", "/prestations/")],
    body=(
        page_header(
            eyebrow="Prestations annexes",
            title="Alimentation, accessoires et matériel opérationnel",
            lead=(
                "Le CEUC propose à ses clients et stagiaires un accès à l'alimentation "
                "canine, aux accessoires et au matériel de sécurité à tarifs préférentiels."
            ),
        )
        + section(
            title="Ce que nous proposons",
            content=cards([
                {
                    "titre": "Alimentation canine",
                    "texte": "Gamme Purina, adaptée aux besoins des chiens de travail soumis à des efforts intenses.",
                    "tag": "Tarifs préférentiels",
                },
                {
                    "titre": "Accessoires canins",
                    "texte": "Colliers, harnais, laisses, muselières — marques Difac, Scorpion et autres références du travail canin.",
                    "tag": "Tarifs préférentiels",
                },
                {
                    "titre": "Matériel opérationnel",
                    "texte": "Équipement de sécurité pour les professionnels, via notre partenaire <a href=\"https://kraken-tactical.fr\" rel=\"noopener nofollow\" target=\"_blank\">Kraken Tactical</a>.",
                    "tag": "Partenaire",
                },
            ]),
        )
        + callout(
            title="Besoin d'un devis matériel&nbsp;?",
            text="N'hésitez pas à nous consulter : nous vous orientons vers la référence adaptée à votre usage et à votre budget.",
            cta_label="Nous consulter",
        )
    ),
)


# ==========================================================================
# GALERIE
# ==========================================================================

from gallery_data import GALERIE as _GAL  # légendes partagées avec le pipeline images

page(
    slug="galerie/",
    title="Galerie photos — entraînements et unités cynophiles | CEUC",
    description=(
        "Photos des entraînements du CEUC : mordant opérationnel, recherche en bâtiment, "
        "patrouille, rassemblements inter-administrations et binômes maître-chien en action."
    ),
    breadcrumb=[("Galerie", "/galerie/")],
    og_image="/assets/img/galerie-01.jpg",
    body=(
        page_header(
            eyebrow="Galerie",
            title="Les équipes cynophiles en action",
            lead=(
                "Un aperçu des entraînements, mises en situation et rassemblements organisés "
                "par le centre. Suivez également notre actualité au quotidien sur Facebook et "
                "Instagram."
            ),
        )
        + section(
            content=gallery([(i, item["alt"]) for i, item in enumerate(_GAL, 1)], captions=False)
        )
        + callout(
            title="Toute notre actualité sur les réseaux",
            text="Actualités, vidéos et photos des sessions : retrouvez le CEUC sur Facebook « ceuc cyno » et Instagram « ceuc_k9 ».",
            cta_label="Voir la page Facebook",
            cta_url=ORG["facebook"],
        )
    ),
)


# ==========================================================================
# CONTACT
# ==========================================================================

page(
    slug="contact/",
    title="Contact — CEUC Meximieux (01) | Formation cynophile",
    description=(
        "Contactez le Centre d'Entraînement Unités Cynophiles : chemin du Mortaray, "
        "01800 Meximieux. Téléphone, e-mail et informations pratiques."
    ),
    breadcrumb=[("Contact", "/contact/")],
    body=(
        page_header(
            eyebrow="Contact",
            title="Contacter le centre",
            lead=(
                "Une question sur une formation, un projet de brigade canine, une demande de "
                "chien de travail ou un tournage&nbsp;? Toute notre équipe reste à votre "
                "disposition."
            ),
        )
        + section(
            content=f"""<div class="contact">
    <div class="contact__block">
      <h2>Coordonnées</h2>
      <p class="contact__note">CEUC — département 01 <em>(siège social)</em></p>
      <ul class="contact__list">
        <li>
          <span class="contact__label">Terrain &amp; bureau</span>
          <address>{ORG['adresse']}<br>{ORG['code_postal']} {ORG['ville']}</address>
        </li>
        <li>
          <span class="contact__label">Téléphone</span>
          <a href="tel:{ORG['tel1_uri']}">{ORG['tel1']}</a><br>
          <a href="tel:{ORG['tel2_uri']}">{ORG['tel2']}</a>
        </li>
        <li>
          <span class="contact__label">E-mail</span>
          <a href="mailto:{ORG['email']}">{ORG['email']}</a>
        </li>
        <li>
          <span class="contact__label">Réseaux sociaux</span>
          <a href="{ORG['facebook']}" rel="noopener" target="_blank">Facebook « ceuc cyno »</a><br>
          <a href="{ORG['instagram']}" rel="noopener" target="_blank">Instagram « ceuc_k9 »</a>
        </li>
      </ul>
    </div>
    <div class="contact__block contact__block--map">
      <h2>Nous situer</h2>
      <p>Le terrain d'entraînement et le bureau se trouvent chemin du Mortaray, à
      Meximieux, dans l'Ain (01).</p>
      <div class="map-placeholder" role="img"
           aria-label="Emplacement du centre : chemin du Mortaray, 01800 Meximieux">
        <strong>{ORG['ville']} ({ORG['code_postal']})</strong>
        <span>{ORG['adresse']}</span>
        <a class="btn btn--ghost btn--sm"
           href="https://www.google.com/maps/search/?api=1&amp;query=Chemin+du+Mortaray+01800+Meximieux"
           rel="noopener" target="_blank">Ouvrir dans Google Maps</a>
      </div>
    </div>
  </div>""",
        )
        + section(
            cls="section--muted section--tight",
            title="Qui contacter selon votre demande",
            content=cards([
                {
                    "titre": "Collectivités &amp; administrations",
                    "texte": "Formation de vos agents, création ou audit de brigade canine, convention de capture : présentez-nous votre contexte et vos contraintes budgétaires.",
                },
                {
                    "titre": "Particuliers",
                    "texte": "Permis de détention d'un chien catégorisé : appelez directement le centre pour fixer un rendez-vous, la formation a lieu toute l'année.",
                },
                {
                    "titre": "Productions audiovisuelles",
                    "texte": "Décrivez les scènes envisagées et les dates de tournage pour que nous puissions étudier la faisabilité et la sélection du chien.",
                },
            ]),
        )
    ),
)


# ==========================================================================
# MENTIONS LÉGALES
# ==========================================================================

page(
    slug="mentions-legales/",
    title="Mentions légales | CEUC",
    description=(
        "Mentions légales du site du Centre d'Entraînement Unités Cynophiles : éditeur, "
        "hébergement, propriété intellectuelle et données personnelles."
    ),
    breadcrumb=[("Mentions légales", "/mentions-legales/")],
    body=(
        page_header(
            eyebrow="Informations légales",
            title="Mentions légales",
            lead="Informations relatives à l'éditeur du site et à son utilisation.",
        )
        + section(
            cls="section--prose",
            content=f"""<h2>Éditeur du site</h2>
    <p>
      {ORG['nom']} ({ORG['sigle']})<br>
      {ORG['adresse']}, {ORG['code_postal']} {ORG['ville']}<br>
      E-mail : <a href="mailto:{ORG['email']}">{ORG['email']}</a><br>
      Téléphone : <a href="tel:{ORG['tel1_uri']}">{ORG['tel1']}</a>
    </p>
    <p>
      Association enregistrée et habilitée auprès de la DDPP et de la Préfecture de l'Ain
      sous le numéro <strong>{ORG['prefecture']}</strong>.<br>
      SIRET : <strong>{ORG['siret']}</strong>.<br>
      Enregistrement en qualité d'organisme de formation sous le numéro
      <strong>{ORG['of']}</strong>.
    </p>

    <h2>Hébergement</h2>
    <p>
      Ce site est hébergé sur une infrastructure dédiée. Les coordonnées complètes de
      l'hébergeur seront précisées lors de la mise en ligne définitive.
    </p>

    <h2>Propriété intellectuelle</h2>
    <p>
      L'ensemble des contenus présents sur ce site (textes, photographies, logo) est la
      propriété du {ORG['sigle']}, sauf mention contraire.
      <strong>Toute reproduction du contenu du site internet, même partielle, est
      formellement interdite.</strong> Tous droits réservés.
    </p>

    <h2>Photographies</h2>
    <p>
      Les photographies publiées sur ce site sont issues des sessions de formation et des
      démonstrations organisées par le centre. Les visages des personnes présentes sont
      floutés lorsque leur identification n'est pas souhaitée. Toute personne apparaissant
      sur une photographie et souhaitant son retrait peut en faire la demande à l'adresse
      <a href="mailto:{ORG['email']}">{ORG['email']}</a>.
    </p>

    <h2>Données personnelles</h2>
    <p>
      Ce site ne dépose aucun cookie de mesure d'audience ni de traceur publicitaire. Les
      informations que vous transmettez par e-mail ou par téléphone sont utilisées
      uniquement pour répondre à votre demande et ne font l'objet d'aucune cession à des
      tiers.
    </p>
    <p>
      Conformément au Règlement général sur la protection des données, vous disposez d'un
      droit d'accès, de rectification et de suppression des données vous concernant. Pour
      l'exercer, écrivez à <a href="mailto:{ORG['email']}">{ORG['email']}</a>.
    </p>

    <h2>Liens externes</h2>
    <p>
      Ce site comporte des liens vers des sites partenaires. Le {ORG['sigle']} ne saurait
      être tenu responsable du contenu de ces sites tiers.
    </p>""",
        )
    ),
)
