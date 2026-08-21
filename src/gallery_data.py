"""Photos de la galerie : fichier source de l'ancien site + légende.

Les légendes servent à la fois d'attribut `alt` (référencement des images) et
de texte affiché sous chaque vignette. Partagé par le pipeline d'images
(src/images.py) et par le générateur de pages (src/pages.py) pour qu'ils ne
puissent pas diverger.

`crop` (optionnel) : (gauche, haut, droite, bas) en fractions de l'image, pour
écarter du cadre des personnes identifiables restées non floutées sur les
photos d'origine. À revoir avec l'association si elle dispose des
autorisations de diffusion.
"""

GALERIE = [
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
        "src": "ib_p028_1_26.jpg",
        "alt": "Chiens de patrouille en pleine course lors d'une démonstration",
        # Le public au second plan n'est pas flouté sur l'original : on recadre dessous.
        "crop": (0, 0.33, 1, 1),
    },
    {
        "src": "ib_p028_1_9.jpg",
        "alt": "Atelier de frappe muselée en stage de perfectionnement",
    },
    {
        "src": "ib_p028_1_25.png",
        "alt": "Chien de service en véhicule d'unité cynophile",
    },
    {
        "src": "ib_p028_1_31.png",
        "alt": "Recherche de personne en bâtiment désaffecté",
    },
    {
        "src": "ib_p028_1_36.png",
        "alt": "Binôme maître-chien en milieu urbain",
    },
    {
        "src": "ib_p028_1_12.jpg",
        "alt": "Interpellation encadrée lors d'une mise en situation",
    },
    {
        "src": "ib_p028_1_21.jpg",
        "alt": "Véhicule d'unité cynophile lors d'un exercice de patrouille",
    },
    {
        "src": "ib_p028_1_22.jpg",
        "alt": "Progression tactique en binôme lors d'un entraînement",
    },
    {
        "src": "ib_p028_1_38.png",
        "alt": "Écusson Unité Cynophile d'un cynotechnicien de Police Municipale",
    },
]
