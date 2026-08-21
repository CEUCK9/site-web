# Suivi des retours de l'association

Version en ligne : <https://avtplay.github.io/ceuc/>
(hébergement temporaire, indexation bloquée le temps de la relecture)

## Version 2 — retours du 21/08/2026

### Traité

- [x] **En-tête** — « Centre d'Entraînement **des** Unités Cynophiles »
- [x] **« Chiens » → « Vente de chiens »** — nouvelle adresse `/vente-chiens/`
- [x] **Brigade canine sortie de l'onglet Formations** — rubrique autonome
      `/creation-brigade-canine/`, avec son propre menu
- [x] **SST** — la page n'annonce plus la délivrance du certificat. Elle
      indique que l'unité est en cours de mise en place et propose un devis.
- [x] **Photos 2025-2026** — accueil, équipe, perfectionnement (×2),
      recherche de personne, secourisme
- [x] **Galerie** — les six photos récentes passent en tête, les visuels les
      plus faibles de l'ancien site sont retirés
- [x] **Correctifs de contenu** — retrait de deux affirmations qui ne
      venaient d'aucune source : « 15+ années d'instruction » et la mention
      de l'A42 / ligne Lyon–Ambérieu sur la page Contact

### En attente de photos

Maxime souhaite **2 à 3 photos par thème**. Fournies pour le perfectionnement
seulement ; il en manque pour :

- [ ] Formation cynotechnicien de Police Municipale
- [ ] Olfaction & recherche *(1 photo sur 2-3)*
- [ ] Capture de chiens errants et dangereux
- [ ] Création de brigade canine & audit
- [ ] Permis de détention chien catégorisé
- [ ] Vente de chiens
- [ ] Cinéma & tournages
- [ ] Prestations annexes
- [ ] Le centre / structures *(1 photo sur 2-3)*

### Questions encore ouvertes

- [ ] **Nom de domaine** — `ceuc.fr` et `ceuc-k9.fr` sont **tous les deux
      libres** (vérifié auprès de l'AFNIC le 21/08/2026). `ceuc.fr` est plus
      court et plus mémorisable ; `ceuc-k9.fr` porte le « K9 » déjà présent
      sur le logo et les réseaux. Recommandation : réserver les deux et faire
      pointer l'un vers l'autre — un `.fr` coûte une dizaine d'euros par an.
- [ ] **SST** — publier ou non la date d'ouverture (« début novembre ») ?
      Elle n'est volontairement pas affichée pour ne pas engager le centre
      sur un calendrier qui peut glisser.
- [ ] **Droit à l'image** — les photos 2026 ont les visages floutés, ce qui
      est rassurant. Reste à confirmer que la diffusion est bien couverte.
- [ ] **Équipe** — Stéphan et Olivier font-ils toujours partie de la
      structure ? (l'ancien site les citait, le brief non)
- [ ] **Fiches chiens** — les trois annonces sont toutes en « VENDU » et
      datent de l'ancien site. À rafraîchir ou à retirer.
- [ ] **Réseaux sociaux** — les adresses Facebook et Instagram ont été
      déduites des noms de comptes, à vérifier.
- [ ] **Contenu rédigé par défaut** — certaines sections ont été écrites
      faute de matière (FAQ, « comment nous travaillons avec les
      productions », descriptifs des spécialités olfactives). À relire et
      corriger par l'association.

## Après validation du contenu

- [ ] **Choisir la solution d'édition** — le site est aujourd'hui statique :
      Maxime ne peut pas le modifier lui-même. Deux pistes à trancher :
      WordPress sur le VPS, ou conserver ce site et y brancher un CMS léger
      (Decap, Sveltia) qui donne une interface d'édition web.
- [ ] Créer / revendiquer la **fiche Google Business Profile** (Meximieux)
- [ ] Soumettre le sitemap à la **Google Search Console**
- [ ] Activer les **redirections 301** depuis `ceuc.free.fr` — le fichier
      `_redirects` généré contient les 37 règles (GitHub Pages les ignore,
      elles fonctionneront sur le VPS ou sur Netlify)
- [ ] Retirer `CEUC_STAGING` pour autoriser l'indexation du site définitif
