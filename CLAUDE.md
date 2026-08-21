# CEUC — Refonte du site web

## Contexte du projet

Refonte du site de l'association **CEUC (Centre d'Entraînement Unités Cynophiles)**,
centre de formation en cynotechnie professionnelle (Police Municipale, sécurité,
particuliers) basé à Meximieux (01).

- Ancien site (très daté) : http://ceuc.free.fr/
- Contact association : Maxime (responsable)
- Raison de la refonte : le site actuel n'est plus du tout référencé, et un devis
  pro avait été obtenu mais jugé trop cher — Maxime n'a pas donné suite.
- Contrainte budget : à moindre frais. Hébergement cible : **VPS OVH + nom de
  domaine** (déjà prévus/possédés par l'association).
- Édition du contenu : doit pouvoir être faite par **un membre non-technique**
  de l'association (Maxime) une fois le site en place → privilégier un CMS
  simple plutôt qu'un site 100% statique.
- Référencement (SEO) : exigence explicite de Maxime, le vieux site n'a
  aucune base SEO exploitable.

Voir aussi `NOTES.md` pour le détail du contenu collecté (ancien site + brief
questionnaire fourni par Maxime pour l'ancien devis).

## Méthodologie de travail (agile très light)

On travaille en boucle courte avec l'association, sans validation lourde en
amont :

1. **Maxime fournit les infos** (contenu, photos, retours, corrections).
2. **On produit une version** du site à partir de ces infos.
3. **On l'héberge sur un hébergement gratuit temporaire** (pas le VPS OVH
   définitif) pour qu'il puisse la voir en ligne facilement pendant les
   itérations.
4. **Maxime relit** la version en ligne.
5. **Il renvoie ses retours et modifications.**
6. On boucle sur les étapes 2 à 5 jusqu'à validation.

Le passage sur le VPS OVH définitif + nom de domaine ne se fait qu'une fois
le contenu/la structure stabilisés avec Maxime — pas dès la première version.

Implications pratiques :
- Pas de gros documents de specs ou de maquettes figées à valider avant de
  coder : on avance par itérations visibles et rapides.
- Prioriser la rapidité de mise en ligne d'une version testable plutôt que la
  perfection dès le premier jet.
- Documenter les décisions prises à chaque retour de Maxime plutôt que de
  tout garder en mémoire de conversation (voir NOTES.md).
