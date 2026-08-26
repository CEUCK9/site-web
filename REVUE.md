# Suivi des retours de l'association

Version en ligne : <https://avtplay.github.io/ceuc/>
(hébergement temporaire, indexation bloquée le temps de la relecture)

## Comment on travaille avec l'association

Boucle courte, sans validation lourde en amont :

1. Maxime fournit les infos (contenu, photos, retours).
2. On produit une version.
3. Elle est publiée automatiquement sur l'adresse de relecture.
4. Maxime relit en ligne.
5. Il renvoie ses corrections.
6. On reboucle sur 2-5 jusqu'à validation.

Le passage sur le nom de domaine définitif n'intervient qu'une fois le
contenu stabilisé.

## Hébergement

Décision arrêtée : **GitHub Pages**, gratuit. Le site est entièrement
statique, aucun serveur PHP n'est nécessaire, et l'adresse e-mail
professionnelle viendra avec le nom de domaine. Budget total : environ
10 € la première année pour les deux noms de domaine, puis ~16 €/an.

Le dépôt doit être transféré dans une organisation GitHub appartenant à
l'association, pour qu'elle ne dépende pas d'un compte personnel.

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

- [x] **Solution d'édition arrêtée** — pas de CMS. Maxime modifiera le site
      lui-même via l'application Claude connectée au dépôt GitHub. Le mode
      d'emploi destiné à ces sessions est dans `CLAUDE.md`.
- [ ] **Transférer le dépôt** dans l'organisation GitHub de l'association
      (Maxime crée le compte et l'organisation, ajoute Alexandre en Owner)
- [ ] **Activer la publication automatique** — déplacer
      `.github/workflows-disponibles/deploy.yml.exemple` vers
      `.github/workflows/deploy.yml` et régler Settings → Pages sur
      « GitHub Actions ». Sans cela Maxime modifiera des fichiers sans que
      le site ne change, ce qui le découragera vite.
- [ ] Créer / revendiquer la **fiche Google Business Profile** (Meximieux)
- [ ] Soumettre le sitemap à la **Google Search Console**
- [ ] Activer les **redirections 301** depuis `ceuc.free.fr` — le fichier
      `_redirects` généré contient les 37 règles (GitHub Pages les ignore,
      elles fonctionneront sur le VPS ou sur Netlify)
- [ ] Retirer `CEUC_STAGING` pour autoriser l'indexation du site définitif
