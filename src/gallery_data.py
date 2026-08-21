"""Photos de la galerie : fichier source + légende.

Les légendes servent à la fois d'attribut `alt` (référencement des images) et
de texte affiché sous chaque vignette. Partagé par le pipeline d'images
(src/images.py) et par le générateur de pages (src/pages.py) pour qu'ils ne
puissent pas diverger.

Clés :
  src     nom du fichier source
  alt     légende / texte alternatif
  recent  True  → photo 2025-2026 fournie par l'association (assets/photos-2026)
          absent → visuel récupéré sur l'ancien site
  crop    (gauche, haut, droite, bas) en fractions, pour écarter du cadre des
          personnes identifiables restées non floutées sur les photos d'origine
"""

GALERIE = [
    # --- Photos 2025-2026 fournies par l'association ---
    {
        "src": "galerie_1.jpg",
        "recent": True,
        "alt": "Interpellation de nuit lors d'une mise en situation avec chien d'intervention",
    },
    {
        "src": "galerie_2.jpg",
        "recent": True,
        "alt": "Équipes cynophiles de Police Municipale rassemblées avec leurs chiens de service",
    },
    {
        "src": "galerie_3.jpg",
        "recent": True,
        "alt": "Progression tactique en binôme dans une cage d'escalier lors d'un exercice",
    },
    {
        "src": "perfectionnement_2.jpg",
        "recent": True,
        "alt": "Exercice d'interpellation en stage de perfectionnement cynotechnique",
    },
    {
        "src": "recherche_personne.jpg",
        "recent": True,
        "alt": "Chien de recherche de personne au travail sur longe en fin de journée",
    },
    {
        "src": "secourisme.jpg",
        "recent": True,
        "alt": "Prise en charge d'une victime lors d'un exercice de secourisme opérationnel",
    },
    # --- Visuels conservés de l'ancien site ---
    {
        "src": "ib_p028_1_6.jpg",
        "alt": "Malinois de la Police Municipale en action lors d'un entraînement CEUC",
    },
    {
        "src": "ib_p028_1_13.jpg",
        "alt": "Exercice de mordant opérationnel encadré par le CEUC",
    },
    {
        "src": "ib_p028_1_33.png",
        "alt": "Chien d'intervention en progression urbaine avec son conducteur",
    },
    {
        "src": "ib_p028_1_9.jpg",
        "alt": "Atelier de frappe muselée en stage de perfectionnement",
    },
    {
        "src": "ib_p028_1_31.png",
        "alt": "Recherche de personne en bâtiment désaffecté",
    },
    {
        "src": "ib_p028_1_38.png",
        "alt": "Écusson Unité Cynophile d'un cynotechnicien de Police Municipale",
    },
]
