# Être trouvé sur Google

Le site est en ligne et techniquement prêt à être référencé. Restent deux
démarches à faire depuis un navigateur, qui ne demandent aucune compétence
technique. Elles sont indépendantes : on peut faire l'une sans l'autre.

**Important** : utiliser un compte Google **de l'association**, pas un compte
personnel. Sinon l'association perd l'accès le jour où la personne s'en va.

---

## Les informations du centre

À recopier **à l'identique** dans les deux démarches. Google recoupe ce qui
est déclaré avec ce qui figure sur le site : la moindre variation affaiblit
le lien entre les deux.

```
Nom          Centre d'Entraînement des Unités Cynophiles
Sigle        CEUC
Adresse      Chemin du Mortaray, 01800 Meximieux
Téléphone    06 62 20 60 13
Second tél.  06 37 48 39 47
E-mail       ceuck9@yahoo.fr
Site web     https://ceuc.fr
Facebook     ceuc cyno
Instagram    ceuc_k9
SIRET        52506111500024
```

Ces valeurs sont enregistrées dans le site à un seul endroit :
`src/template.py`, bloc `ORG`. Les modifier là les met à jour partout —
pages, pied de page, données lues par Google.

---

## 1. Search Console — environ 15 minutes

Elle indique à Google que le site existe, accélère son exploration, et
signale ensuite les problèmes éventuels.

### Déclarer le site

1. Aller sur <https://search.google.com/search-console>
2. **Ajouter une propriété**, puis choisir **Domaine** dans la colonne de
   gauche — et non « Préfixe d'URL ». La version Domaine couvre d'un seul
   coup `ceuc.fr`, `www.ceuc.fr`, le http et le https ; l'autre obligerait à
   déclarer chaque variante séparément.
3. Saisir `ceuc.fr`
4. Google affiche un code de vérification de la forme
   `google-site-verification=…`

### Ajouter le code chez OVH

Dans l'espace client OVH, section **Noms de domaine → ceuc.fr → Zone DNS**,
ajouter une entrée :

| Type | Sous-domaine | Valeur |
| --- | --- | --- |
| TXT | *(laisser vide)* | le code fourni par Google |

Revenir sur Search Console et cliquer **Valider**. En cas d'échec, attendre
une dizaine de minutes — la modification DNS met un peu de temps à se
propager — puis réessayer.

### Envoyer le plan du site

Une fois la propriété validée : menu de gauche → **Sitemaps** → saisir
`sitemap.xml` → **Envoyer**.

Ce fichier est régénéré automatiquement à chaque modification du site : il
n'y a jamais à le renvoyer.

### À quoi s'attendre

Les premiers jours, Google annonce « 0 page indexée ». C'est normal.
Comptez une à deux semaines pour les premières pages, davantage pour un
référencement stable.

---

## 2. Fiche Google Business — 30 minutes, puis attente

C'est l'encadré qui apparaît à droite de l'écran quand on cherche un
professionnel, avec l'adresse, le téléphone et les photos. **Pour un centre
de formation local, c'est le levier le plus rentable** — davantage que bien
des optimisations techniques.

1. Aller sur <https://business.google.com>
2. Créer la fiche avec les informations ci-dessus

### Le choix décisif : la catégorie

Google demande une **catégorie principale**. C'est ce réglage, bien plus que
le texte de description, qui détermine sur quelles recherches la fiche
apparaît.

Chercher du côté de « Centre de formation » ou « École de dressage pour
chiens », puis ajouter les autres en catégories secondaires. Prendre le
temps de parcourir les propositions : ce choix pèse lourd et se modifie
ensuite difficilement sans perdre de l'ancienneté acquise.

### Adresse visible ou zone d'intervention ?

Google demande si les clients se déplacent sur place.

* **Oui** — l'adresse du terrain apparaît publiquement sur Google Maps.
* **Non** — l'adresse reste masquée et on déclare une *zone d'intervention*
  (le département de l'Ain, la région, ou la France entière). La fiche reste
  visible, l'adresse non.

Les deux fonctionnent pour le référencement. C'est une décision de
l'association, pas une contrainte technique.

### La validation

Google envoie le plus souvent un **courrier postal contenant un code**, à
l'adresse déclarée. Comptez une à deux semaines. Il propose parfois une
validation par téléphone ou par vidéo, plus rapide.

**Tant que la fiche n'est pas validée, elle n'apparaît pas publiquement.**

### Une fois validée

* Renseigner les horaires, ou indiquer « sur rendez-vous »
* **Ajouter des photos** — les fiches qui en comportent sont nettement plus
  consultées. Celles du site conviennent parfaitement, les visages y sont
  déjà floutés.
* Rédiger une description courte reprenant les mots que les gens tapent :
  formation maître-chien, Police Municipale, permis chien catégorisé.

---

## Ce qui reste à ajouter au site

Trois éléments renforceraient le référencement local. Ils manquent parce
qu'ils demandent une information que seule l'association possède. Il suffit
de la donner à Claude, qui saura où l'inscrire.

- [ ] **Horaires d'ouverture** — Google les recoupe avec la fiche Business.
      Même « sur rendez-vous uniquement » est une réponse valable.
- [ ] **Coordonnées GPS du terrain** — elles aident Google à rattacher le
      site à un point précis sur la carte. Se relèvent sur Google Maps :
      clic droit sur le lieu, les deux nombres s'affichent en haut.
- [ ] **Lien vers la fiche Business** depuis le site, une fois qu'elle
      existe — cela consolide l'association entre les deux.

---

## Ce qui est déjà en place

Inutile de s'en préoccuper, c'est automatique et vérifié à chaque
publication :

* Un titre et une description propres à chaque page, aux bonnes longueurs
* Des données structurées décrivant l'organisme, ses formations et ses
  questions fréquentes, dans le format que Google attend
* Un plan du site régénéré à chaque modification
* Une description sur chaque image
* Les redirections depuis les anciennes adresses du site `ceuc.free.fr`
* Compression et cache, que Google mesure dans son évaluation

Le contrôle automatique refuse de publier si l'un de ces points est cassé.
