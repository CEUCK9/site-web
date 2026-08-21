# Points à valider avec Maxime — version 1

Version en ligne : <https://avtplay.github.io/ceuc/>
(hébergement temporaire, indexation bloquée le temps de la relecture)

## À vérifier en priorité

### Contenu factuel
- [ ] **Équipe** — le brief ne cite plus que Anthony, David et Maxime. L'ancien
      site mentionnait aussi **Stéphan et Olivier** (hommes d'attaque). Sont-ils
      toujours dans la structure ?
- [ ] **Chiens vendus** — les trois fiches reprises sont celles de l'ancien site
      et sont toutes marquées « VENDU ». À remplacer par des placements récents,
      ou à retirer si l'association préfère.
- [ ] **Chiffres de la page d'accueil** — « 15+ années d'instruction » est une
      estimation à partir des références citées (court-métrage 2009, SIRET).
      À confirmer ou corriger.
- [ ] **Formation SST** — présente dans le brief mais sans détail (durée,
      tarif, public). La page est volontairement courte en attendant.
- [ ] **Conduite opérationnelle** — annoncée « très prochainement » depuis
      des années sur l'ancien site et absente du brief : page supprimée.
      Confirmer l'abandon.
- [ ] **Liens réseaux sociaux** — les URL Facebook et Instagram ont été
      déduites des noms de comptes (« ceuc cyno », « ceuc_k9 »). À vérifier.

### Droit à l'image
- [ ] Sur les photos de l'ancien site, les visages sont **floutés sur les
      séances Police mais pas sur les stages de capture**. Seules les photos
      floutées ont été retenues, et une photo de démonstration a été recadrée
      pour écarter le public. À confirmer que la diffusion est couverte par des
      autorisations.

### Éléments manquants
- [ ] **Photos en haute définition** — celles de l'ancien site plafonnent à
      800 px de large. Le site est prêt à recevoir mieux : il suffit de fournir
      les originaux.
- [ ] **Nom de domaine** — quel domaine l'association réserve-t-elle ? Le code
      pointe provisoirement vers `ceuc-k9.fr`.
- [ ] **Tarifs** — aucun tarif n'est affiché. Souhaité ou non ?
- [ ] **Formulaire de contact** — la page n'affiche que téléphone et e-mail.
      Un formulaire est possible, mais demande un service d'envoi côté serveur
      (à prévoir sur le VPS).

## Ce qui a changé par rapport à l'ancien site

| Avant | Maintenant |
|---|---|
| ~32 pages, dont une majorité vides | 16 pages, toutes remplies |
| Menu à 3 niveaux | Menu à 2 niveaux, 7 entrées |
| Illisible sur téléphone | Conçu mobile d'abord |
| Accents cassés (ISO-8859-1) | UTF-8 |
| Aucune base de référencement | Titres et descriptions uniques, données structurées, sitemap |
| Galeries cassées ou vides | Galerie unique avec visionneuse |
| Partenaire K9 Métier Passion | Kraken Tactical (selon le brief) |
| Facebook seul | Facebook + Instagram |

## Référencement — reste à faire une fois le domaine choisi

- [ ] Créer / revendiquer la **fiche Google Business Profile** (Meximieux) —
      c'est le levier le plus rentable pour les recherches locales.
- [ ] Soumettre le sitemap à la **Google Search Console**.
- [ ] Mettre en place les **redirections 301** depuis les anciennes URL
      `ceuc.free.fr` (le fichier `_redirects` généré liste les 35 règles).
- [ ] Retirer `CEUC_STAGING` pour autoriser l'indexation du site définitif.
