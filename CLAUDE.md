# Site du CEUC — instructions de travail

## Le projet en deux lignes

Site du **CEUC (Centre d'Entraînement des Unités Cynophiles)**, association de
Meximieux (01) qui forme les maîtres-chiens de la Police Municipale et des
services de secours. Site statique généré par des scripts Python : on modifie
des fichiers source, une action GitHub reconstruit et publie automatiquement.

## Avec qui tu travailles

Ton interlocuteur est **Maxime**, responsable de l'association. Il est
policier municipal et formateur cynotechnique, **il n'est pas développeur**.

En conséquence :

- Écris-lui en français courant, sans vocabulaire technique. Il ne sait pas ce
  qu'est un commit, un slug ou une balise meta — et il n'a pas à le savoir.
- Ne lui demande jamais de choisir entre deux options techniques. Choisis, et
  explique en une phrase ce que ça change **pour les visiteurs de son site**.
- Quand tu as terminé, dis-lui simplement quelle page a changé et quoi, puis
  qu'il verra le résultat en ligne dans une à deux minutes.
- S'il demande quelque chose d'irréalisable en l'état (un formulaire de
  contact, une boutique, un espace adhérents), dis-le franchement et propose
  la version simple qui répond au besoin.

## Règle absolue : ne rien inventer

C'est le point le plus important de ce fichier.

Ce site engage une association qui vend des formations à des mairies et à des
administrations. **Une information inexacte sur ce site est un problème réel
pour eux**, pas une imprécision de rédaction.

Tu ne dois donc **jamais** produire, de toi-même :

- un chiffre : années d'existence, nombre de stagiaires, de formations, de
  chiens placés, durée d'un module, effectif ;
- un tarif, un prix, une remise ;
- une date : ouverture d'une session, création de l'association, calendrier ;
- une référence légale : loi, décret, article de code ;
- un diplôme, une habilitation, une certification, un agrément ;
- un nom : formateur, partenaire, élevage, commune, production, client ;
- une description de la façon dont l'association travaille, si personne ne te
  l'a décrite.

Quand l'information manque, **demande-la à Maxime**. Une phrase de moins sur
le site vaut mieux qu'une phrase inventée.

Cette règle a déjà servi : la première version du site affichait « 15+ années
d'instruction cynophile » et situait le terrain « à proximité immédiate de
l'A42 » — deux affirmations qui ne venaient d'aucune source et qu'il a fallu
retirer.

Le fait de reformuler pour le web est autorisé et souhaitable. Inventer un
fait ne l'est pas.

## Où se trouve quoi

| Ce que Maxime veut changer | Fichier à modifier |
|---|---|
| Un texte, un titre, une question fréquente | `src/pages.py` |
| Une photo de la galerie, sa légende | `src/gallery_data.py` |
| Ajouter une nouvelle photo au site | `assets/photos-2026/` + `src/images.py` |
| Coordonnées, e-mail, téléphone, réseaux sociaux | `src/template.py` (bloc `ORG`) |
| Les entrées du menu | `src/template.py` (bloc `NAV`) |
| Les couleurs, les espacements, la mise en page | `src/style.css` |

`src/pages.py` contient tout le contenu, page par page, dans l'ordre du menu.
Chaque page y est déclarée avec son titre, sa description pour Google et son
corps. C'est le fichier que tu modifieras le plus souvent.

**Ne touche pas** à `build.py`, `check.py`, `src/template.py` (hors `ORG` et
`NAV`) ni `src/components.py` sans raison précise : ce sont les rouages, pas
le contenu.

## Comment faire les modifications courantes

### Changer un texte

Cherche la phrase dans `src/pages.py` et modifie-la. Attention : le contenu
est écrit en HTML dans des chaînes Python. Conserve les balises `<p>`,
`<strong>`, `<em>` telles quelles, ainsi que les guillemets qui entourent le
texte.

### Ajouter une photo

1. Dépose le fichier dans `assets/photos-2026/`, avec un nom explicite en
   minuscules sans accent (`capture_chien_1.jpg`).
2. Déclare-le dans `PHOTOS_2026` au début de `src/images.py`, en indiquant le
   nom de sortie, la largeur maximale et le format de recadrage.
3. Utilise-le dans `src/pages.py`, via `photo_strip([...])` pour illustrer un
   thème, ou dans une carte existante.

Pour l'ajouter à la galerie, déclare-le plutôt dans `src/gallery_data.py` avec
`"recent": True`.

**Toute photo doit avoir une légende descriptive.** Elle sert de texte
alternatif : c'est ce que lisent Google et les personnes malvoyantes. Décris
ce qu'on voit (« Chien de recherche au travail sur longe »), pas le fichier.

**Vérifie les visages.** Les photos de l'association sont normalement
floutées. Si une photo montre des personnes identifiables — en particulier
des stagiaires, des passants ou des enfants — signale-le à Maxime avant de la
publier plutôt que de la mettre en ligne.

### Ajouter une question fréquente

Les questions fréquentes sont regroupées en listes nommées `..._FAQ` dans
`src/pages.py`. Ajoute un couple question / réponse à la liste : le bloc
visible sur la page **et** les données lues par Google se mettent à jour
ensemble, il n'y a rien d'autre à faire.

### Créer une page

Copie la structure d'une page existante et ajoute-la à `NAV` dans
`src/template.py`. Chaque page a besoin d'un titre et d'une description
**uniques** — `check.py` refuse les doublons.

## Vérifier avant de publier

Si tu peux exécuter des commandes :

```bash
python3 build.py && python3 check.py
```

`check.py` contrôle les liens internes, les titres et descriptions en double
ou trop longs, la hiérarchie des titres, les textes alternatifs des images et
les données structurées. **Il doit finir sans erreur.**

Si tu ne peux pas exécuter de commandes, ce n'est pas bloquant : la même
vérification tourne automatiquement à la publication, et **un site cassé n'est
jamais mis en ligne**. En revanche, préviens Maxime que le résultat sera
visible après le contrôle automatique.

## Comment le site est publié

Toute modification enregistrée sur la branche `main` déclenche la
reconstruction et la mise en ligne, en une à deux minutes. Il n'y a rien à
lancer manuellement.

L'adresse actuelle est temporaire, et le site est **volontairement invisible
sur Google** le temps de la relecture. Ce n'est pas un défaut de
référencement : c'est pour éviter que cette version concurrence le site
définitif. Si Maxime s'étonne de ne pas se trouver sur Google, c'est
l'explication.

## Le référencement

C'est la raison d'être de la refonte : l'ancien site n'était plus trouvé.
Chaque page a donc un titre et une description propres, des données
structurées et un maillage entre les pages. Quelques réflexes à conserver :

- Un titre de page fait au maximum **65 caractères**, une description entre
  **70 et 165**. `check.py` le vérifie.
- Une seule idée par page. Mieux vaut une page dédiée à « capture de chien
  errant » qu'un paragraphe noyé ailleurs.
- Emploie les mots que les gens tapent : « formation maître-chien police
  municipale », « permis chien catégorisé », plutôt que le jargon interne.
- Cite la ville et le département quand c'est naturel : une bonne partie des
  recherches sont locales.

## Suivi

`REVUE.md` liste ce qui a été traité, les photos encore attendues et les
questions en suspens. Tiens-le à jour quand un point est réglé.

`REFERENCEMENT.md` explique les deux démarches à faire chez Google (Search
Console et fiche Business) et liste les informations que le site attend
encore : horaires, coordonnées GPS, lien vers la fiche. Si Maxime te donne
l'une d'elles, inscris-la et coche la ligne correspondante.

`NOTES.md` conserve le détail du contenu d'origine, pour retrouver la source
d'une information.
