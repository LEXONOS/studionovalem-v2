# Tropical Dream — site internet

Site vitrine multipage pour **Tropical Dream** (Baie-Mahault, Guadeloupe) : gîtes, location de véhicules, jacuzzi-spa & bien-être, événements.
Code natif (HTML / CSS / JS), zéro dépendance, zéro build, prêt pour GitHub → Vercel (aperçu) puis OVH via FileZilla (prod).

## Pages

| Fichier | Rôle |
|---|---|
| `index.html` | Accueil : hero + guichet de réservation, 3 univers, chiffres clés, hôtes, gîtes, véhicules, bien-être, avis, carte, CTA |
| `gites.html` | Gîte familial 3 chambres, studio Ti Punch, espaces communs (galerie + lightbox), inclus, FAQ |
| `vehicules.html` | Étapes, 3 catégories, conditions, avis, combo gîte + voiture |
| `bien-etre.html` | Jacuzzi-spa privatif, 3 formules, déroulé, idée cadeau |
| `evenements.html` | Anniversaires, EVJF, réunions de famille, séminaires |
| `a-propos.html` | Astrid & Christophe, façon de faire, distances depuis Baie-Mahault |
| `contact.html` | Coordonnées, formulaire (WhatsApp / e-mail), carte, itinéraire |
| `reservation.html` | Réservation complète à 4 onglets avec aperçu du message en direct |
| `mentions-legales.html` | Mentions légales (SAS Tropical Dream, SIREN 890 410 137) |
| `404.html` | Page introuvable |

Sur **toutes** les pages : bouton flottant « Réserver » qui ouvre un tiroir de réservation rapide (3 onglets), et barre mobile Appeler / WhatsApp / Réserver.

## Comment marche la réservation

Le client n'a pas de moteur de réservation ni de paiement en ligne. Le site **compose un message** (gîte / véhicule / bien-être / événement, dates, personnes, options) et l'ouvre dans **WhatsApp** (`wa.me/590690702529`) ou dans la **messagerie e-mail** (`tropicaldream971@gmail.com`) du visiteur. Astrid ou Christophe répondent avec la dispo et le tarif. Aucun serveur, aucune donnée stockée, rien à maintenir.

Liens directs utiles : `reservation.html?resa=vehicule`, `?resa=bienetre`, `?resa=evenement`, `?resa=gite&gite=Studio+Ti+Punch+(couple)`.

## Photos : comment ça marche (important)

Je n'ai pas pu aspirer les photos Instagram / Facebook / Booking (accès bloqué). Le site tourne donc avec des **photos d'attente** chargées en ligne (Unsplash), déjà cadrées pour chaque emplacement.

Pour mettre les vraies photos, **aucune ligne de code à toucher** :
1. Ouvre `PHOTOS-A-AJOUTER.md` : il liste les 29 fichiers attendus et ce qu'il faut dessus.
2. Récupère les photos du client (fiche Google Business, Booking, Instagram, ou demande-lui les originaux).
3. Renomme chaque photo avec le nom exact (ex. `hero-piscine.jpg`) et dépose-la dans `assets/img/`.
4. Recharge : la vraie photo remplace automatiquement la photo d'attente (`data-fallback`).

Compresse les JPG avant (squoosh.app, 1600 px de large, < 400 ko).

## Mise en ligne, clic par clic

### Aperçu (GitHub + Vercel)
1. github.com → **New repository** → nom `tropical-dream` → Create.
2. Sur la page du repo vide : **uploading an existing file** → glisse TOUT le contenu du dossier (pas le dossier lui-même) → **Commit changes**.
3. vercel.com → **Add New… → Project** → importe `tropical-dream` → **Deploy** (rien à régler, `vercel.json` est déjà là). Lien d'aperçu `.vercel.app` en 30 s.

### Production (OVH + FileZilla)
1. FileZilla → connexion au serveur OVH du client → dossier `www/`.
2. Glisse tout le contenu du dossier (les `.html`, `assets/`, `favicon.svg`, `robots.txt`, `sitemap.xml`, `.htaccess`).
3. Dans `_src/build.py` ligne 8, remplace `SITE_URL` par le vrai domaine puis relance `python3 _src/build.py` (ou fais un rechercher/remplacer de `https://www.tropicaldream-guadeloupe.fr` dans tous les `.html` + `robots.txt`). Ça met à jour les balises canonical / Open Graph / sitemap.

## Modifier le contenu

- Textes : soit directement dans les `.html`, soit dans `_src/pages.py` puis `python3 _src/build.py` (regénère tout, header/footer compris).
- Coordonnées : `assets/js/main.js` (4 lignes en haut) + footer dans `_src/build.py`.
- Couleurs / polices : variables en haut de `assets/css/styles.css`.
- Le dossier `_src/` n'est pas nécessaire au site en ligne : tu peux ne pas l'envoyer chez OVH.

## Contenu à valider avec le client

Voir `CONTENU-A-VALIDER.md` : tout ce que j'ai déduit ou proposé faute d'info (flotte, tarifs, formules spa, conditions de location).
