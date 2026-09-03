# -*- coding: utf-8 -*-
# Contenu des pages SEO de studionovalem.fr. Chaque page = un dictionnaire.
# Pour ajouter une page : copie un bloc, change slug/title/desc/h1/lead/body/faq, relance _src/build.py.

ZONES = [
    ("creation-site-internet-guadeloupe", "Guadeloupe"),
    ("creation-site-internet-martinique", "Martinique"),
    ("creation-site-internet-saint-martin", "Saint-Martin"),
    ("creation-site-internet-saint-barthelemy", "Saint-Barthélemy"),
]

GUIDES = [
    ("prix-site-internet-guadeloupe", "Combien coûte un site internet en Guadeloupe ?"),
    ("site-internet-ou-page-facebook", "Site internet ou page Facebook ?"),
    ("agence-web-guadeloupe-ou-freelance", "Agence web ou indépendant en Guadeloupe ?"),
    ("refonte-site-wix-wordpress-guadeloupe", "Refaire un site Wix ou WordPress"),
    ("aides-site-internet-guadeloupe", "Faire financer son site jusqu'à 80 %"),
]

METIERS = [
    ("site-internet-restaurant-guadeloupe", "Site pour restaurant"),
    ("site-internet-artisan-guadeloupe", "Site pour artisan"),
    ("site-internet-commerce-guadeloupe", "Site pour commerce"),
    ("site-internet-location-gite-guadeloupe", "Site pour gîte et location"),
    ("site-internet-coiffeur-beaute-guadeloupe", "Site pour coiffeur et beauté"),
]

PAGES = []

# ------------------------------------------------------------------ GUADELOUPE
PAGES.append(dict(
    slug="creation-site-internet-guadeloupe", crumb="Guadeloupe",
    title="Création de site internet en Guadeloupe : dès 490 €, livré en 7 jours | Studio Novalem",
    desc="Création de site internet en Guadeloupe par Louis, développeur basé sur place. Site codé sur mesure dès 490 €, livré en 7 jours, zéro abonnement, le site vous appartient. Pointe-à-Pitre, Jarry, Le Gosier, Sainte-Anne, Basse-Terre.",
    kicker="Création de sites internet", where="en Guadeloupe", geoplace="Guadeloupe", georegion="GP",
    h1="Création de site internet en Guadeloupe", pose="salut",
    lead="Je suis Louis, je vis en Guadeloupe et je code des sites internet pour les commerces d'ici. Prix ferme dès 490 €, livré en 7 jours, zéro abonnement, et je me déplace pour le cadrage comme pour la remise.",
    service="Création de site internet en Guadeloupe", area=["Guadeloupe"],
    wa="Bonjour Louis, je suis en Guadeloupe et je voudrais un site pour mon commerce.",
    related=[("aides-site-internet-guadeloupe", "Faire financer son site jusqu'à 80 % par la Région"), ("prix-site-internet-guadeloupe", "Combien coûte un site internet en Guadeloupe ?"), ("site-internet-restaurant-guadeloupe", "Un site pour votre restaurant")],
    body="""
<h2>Combien coûte un site internet en Guadeloupe ?</h2>
<p>Chez Studio Novalem, un site internet coûte 490 € pour une page, 990 € pour un site complet jusqu'à 5 pages, et 1 390 € pour un site qui prend les rendez-vous tout seul. Ce sont des prix fermes, payés une fois. Il n'y a aucun abonnement : le seul frais qui reste ensuite est l'hébergement, environ 25 € par an, à votre nom. À titre de comparaison, une agence facture le plus souvent entre 3 000 et 6 000 € pour un site vitrine, avec une maintenance mensuelle en plus.</p>
{PLANS}

<h2>Pourquoi un commerce guadeloupéen a besoin d'un site en 2026 ?</h2>
<p>Parce que vos clients vous cherchent sur leur téléphone avant de pousser votre porte. Quand quelqu'un tape « restaurant Sainte-Anne », « garage Baie-Mahault » ou « coiffeur Le Gosier » sur Google, il tombe sur les commerces qui ont un site et une fiche Google à jour. Une page Facebook n'apparaît pas dans ces résultats, et elle n'a ni horaires clairs, ni carte, ni bouton pour appeler. En Guadeloupe, la majorité des petits commerces n'ont toujours pas de site : c'est une place à prendre, et elle se prend vite.</p>

<h2>Un site codé sur mesure, pas un gabarit WordPress</h2>
<p>Je code chaque site à la main, augmenté à l'IA pour aller vite. Concrètement, ça veut dire un site 3 à 5 fois plus rapide qu'un site WordPress, sans extension à mettre à jour, sans faille héritée d'un thème, et surtout sans abonnement caché. Le design est fait pour votre commerce, pas choisi dans un catalogue. Dès le premier écran, votre client trouve un bouton Appeler, un bouton WhatsApp et l'itinéraire Google Maps.</p>

<h2>Où est-ce que j'interviens en Guadeloupe ?</h2>
<p>Partout. Je suis basé sur la Grande-Terre et je me déplace pour le rendez-vous de cadrage et la remise du site : Pointe-à-Pitre, Les Abymes, Baie-Mahault et la zone de Jarry, Le Gosier, Sainte-Anne, Saint-François, Le Moule, Petit-Bourg, Lamentin, Basse-Terre, Capesterre, Sainte-Rose, Deshaies, Bouillante, et aussi Marie-Galante et Les Saintes. Le reste se fait au téléphone et sur WhatsApp, ce qui vous évite de bloquer une demi-journée.</p>

<h2>Comment ça se passe, du premier appel à la mise en ligne ?</h2>
<ol class="seo-steps">
  <li><b>Cadrage, 30 minutes au téléphone ou sur place.</b> Vos objectifs, votre clientèle, ce que vous avez déjà. Devis ferme sous 48 h.</li>
  <li><b>Maquette.</b> Vous voyez le design avant que je code quoi que ce soit, et vous corrigez ce que vous voulez.</li>
  <li><b>Code, 7 à 14 jours.</b> Intégration de vos textes et photos, tests sur téléphone, tablette et ordinateur. Deux tours de modifications compris.</li>
  <li><b>Mise en ligne.</b> Nom de domaine, HTTPS, indexation Google, remise des fichiers et prise en main de 30 minutes.</li>
</ol>

<h2>Des sites de commerces guadeloupéens, en ligne</h2>
<p>Voici trois sites que j'ai réalisés pour des commerces d'ici. Vous pouvez les visiter, ils tournent tous les jours.</p>
{WORKS}

<h2>Ce que vous ne paierez jamais chez moi</h2>
<p>Pas d'abonnement mensuel, pas de thème à acheter, pas de maintenance imposée, et pas de frais pour récupérer votre site : les fichiers sont à vous dès la livraison. Le SAV est gratuit à vie sur tout ce qui casse à cause de mon code, quelle que soit l'ancienneté du site.</p>

<h2>Questions fréquentes sur la création de site en Guadeloupe</h2>
""",
    faq=[
        ("Combien de temps pour avoir mon site en ligne en Guadeloupe ?", "7 jours pour un site une page à partir du rendez-vous de cadrage, 10 à 14 jours pour un site complet jusqu'à 5 pages, 3 semaines pour la formule Signature. Le délai est écrit sur le devis, et un retard qui m'est imputable ouvre droit à une remise de 10 % par semaine entamée."),
        ("Je n'ai ni logo, ni photos, ni textes. Vous faites quoi ?", "On part de zéro ensemble. Je vous guide pour prendre les photos avec votre téléphone, j'écris les textes avec vous au téléphone, et si vous n'avez pas de logo je vous fais un logo typographique propre. Le site sort quand même en 7 jours."),
        ("Est-ce que vous vous déplacez en Guadeloupe ?", "Oui. Cadrage et remise du site se font sur place si vous le souhaitez, sur toute la Guadeloupe, Marie-Galante et Les Saintes compris. Le reste se fait au téléphone et sur WhatsApp."),
        ("Le site sera-t-il vraiment à moi ?", "Oui, à 100 %. Le nom de domaine et l'hébergement sont à votre nom, et je vous remets tous les fichiers du site. Vous pouvez changer de prestataire du jour au lendemain sans me demander la permission."),
        ("Est-ce que mon site sera trouvé sur Google en Guadeloupe ?", "Chaque site est livré avec les balises Google de base, une fiche Google Business si vous n'en avez pas encore (option 150 €), un sitemap et l'indexation demandée. La formule Vitrine ajoute le référencement complet, la Search Console et les données structurées. Être premier sur une recherche concurrentielle prend des semaines à des mois, et je ne vous promettrai jamais une position : je vous dis ce qui est réaliste."),
        ("Combien coûte l'hébergement d'un site en Guadeloupe ?", "Environ 25 € par an pour le nom de domaine et l'hébergement, facturés à votre nom. C'est le seul frais récurrent, et il n'y a aucune maintenance obligatoire."),
    ],
))

# ------------------------------------------------------------------ MARTINIQUE
PAGES.append(dict(
    slug="creation-site-internet-martinique", crumb="Martinique",
    title="Création de site internet en Martinique : dès 490 €, sans abonnement | Studio Novalem",
    desc="Création de site internet en Martinique pour les commerces et indépendants : site codé sur mesure dès 490 €, livré en 7 jours, zéro abonnement. Fort-de-France, Le Lamentin, Schoelcher, Le Robert, Sainte-Luce, Le Marin.",
    kicker="Création de sites internet", where="en Martinique", geoplace="Martinique", georegion="MQ",
    h1="Création de site internet en Martinique", pose="pointe",
    lead="Un site codé sur mesure pour votre commerce martiniquais, livré en 7 jours, prix ferme dès 490 €, zéro abonnement. Je suis basé en Guadeloupe et je travaille avec la Martinique par téléphone et WhatsApp, avec les mêmes prix et le même SAV à vie.",
    service="Création de site internet en Martinique", area=["Martinique"],
    wa="Bonjour Louis, je suis en Martinique et je voudrais un site pour mon commerce.",
    related=[("prix-site-internet-guadeloupe", "Combien coûte un site internet aux Antilles ?"), ("site-internet-ou-page-facebook", "Site internet ou page Facebook ?"), ("site-internet-location-gite-guadeloupe", "Un site pour votre gîte ou votre location")],
    body="""
<h2>Combien coûte un site internet en Martinique ?</h2>
<p>Les prix sont les mêmes qu'en Guadeloupe : 490 € pour un site une page, 990 € pour un site complet jusqu'à 5 pages, 1 390 € pour un site avec prise de rendez-vous en ligne. Prix fermes, payés une fois, sans abonnement. Ensuite, seulement l'hébergement à votre nom, environ 25 € par an. Une agence en Martinique facture le plus souvent 3 000 à 6 000 € un site vitrine comparable, plus une maintenance mensuelle.</p>
{PLANS}

<h2>Comment je travaille avec la Martinique depuis la Guadeloupe ?</h2>
<p>Exactement comme avec un client de Pointe-à-Pitre, à une différence près : le rendez-vous de cadrage se fait au téléphone ou en visio plutôt qu'autour d'une table. Trente minutes suffisent. Ensuite, la maquette arrive sur votre WhatsApp, vous la corrigez, je code, et le site part en ligne. Vos photos et vos textes me parviennent par WhatsApp ou par mail. Pour un projet important, je me déplace à Fort-de-France : c'est 45 minutes de vol.</p>

<h2>Pour quels commerces martiniquais ?</h2>
<p>Restaurants et lolos de Sainte-Anne, du Diamant ou de Sainte-Luce, gîtes et locations des Trois-Îlets et du Marin, artisans et services du Lamentin, de Ducos et du Robert, commerces de Fort-de-France et de Schoelcher, cabinets et salons de coiffure, garages, loueurs de voitures. Si vos clients vous cherchent sur Google avec le nom de votre commune, un site fait pour ça vous fait apparaître avant ceux qui n'ont qu'une page Facebook.</p>

<h2>Ce qui est compris dans chaque site</h2>
<ul class="seo-list">
  <li>Un design fait pour votre commerce, jamais un gabarit</li>
  <li>Boutons Appeler, WhatsApp et itinéraire Google Maps dès le premier écran</li>
  <li>Un site pensé pour le téléphone d'abord, rapide, sécurisé en HTTPS</li>
  <li>Nom de domaine et hébergement à votre nom, fichiers du site remis</li>
  <li>Deux tours de modifications, puis SAV gratuit à vie sur les bugs</li>
</ul>

<h2>Des sites en ligne, faits pour les Antilles</h2>
{WORKS}

<h2>Questions fréquentes, Martinique</h2>
""",
    faq=[
        ("Vous venez en Martinique pour le rendez-vous ?", "Par défaut, non : le cadrage se fait au téléphone ou en visio, en 30 minutes, et ça marche très bien. Pour un projet important (site à plusieurs pages, boutique, outil métier), je peux venir à Fort-de-France."),
        ("Le prix est-il le même qu'en Guadeloupe ?", "Oui, strictement le même : 490 €, 990 € ou 1 390 € selon la formule, et aucun frais de déplacement puisque tout se fait à distance."),
        ("Comment je vous envoie mes photos et mes textes ?", "Par WhatsApp ou par mail, en vrac. Je trie, je compresse, j'intègre. Si vous n'avez rien, je vous guide pour prendre les photos avec votre téléphone et j'écris les textes avec vous."),
        ("Et le SAV, à distance ?", "Le SAV gratuit à vie ne dépend pas de la distance : un bug, vous m'écrivez, je corrige. La plupart des corrections se font dans la journée."),
        ("Mon site apparaîtra-t-il sur Google en Martinique ?", "Le site est livré avec les balises Google, un sitemap et l'indexation demandée. Je vous conseille en plus une fiche Google Business, gratuite, que je peux créer ou optimiser pour vous : c'est elle qui vous fait apparaître sur la carte quand on cherche votre métier dans votre commune."),
    ],
))

# ------------------------------------------------------------------ SAINT-MARTIN
PAGES.append(dict(
    slug="creation-site-internet-saint-martin", crumb="Saint-Martin",
    title="Création de site internet à Saint-Martin : dès 490 €, en français et en anglais | Studio Novalem",
    desc="Création de site internet à Saint-Martin pour restaurants, locations, activités et commerces. Site codé sur mesure dès 490 €, version anglaise possible, zéro abonnement. Marigot, Grand-Case, Orient Bay, Cul-de-Sac.",
    kicker="Création de sites internet", where="à Saint-Martin", geoplace="Saint-Martin", georegion="MF",
    h1="Création de site internet à Saint-Martin", pose="pointe",
    lead="Un site codé sur mesure pour votre commerce de Saint-Martin, en français, en anglais ou les deux. Prix ferme dès 490 €, livré en 7 jours, zéro abonnement, tout se fait à distance.",
    service="Création de site internet à Saint-Martin", area=["Saint-Martin"],
    wa="Bonjour Louis, je suis à Saint-Martin et je voudrais un site pour mon commerce.",
    related=[("site-internet-location-gite-guadeloupe", "Un site pour votre location ou votre villa"), ("site-internet-restaurant-guadeloupe", "Un site pour votre restaurant"), ("prix-site-internet-guadeloupe", "Combien coûte un site internet aux Antilles ?")],
    body="""
<h2>Un site bilingue pour une île bilingue</h2>
<p>À Saint-Martin, vos clients viennent de partout : métropole, Amérique du Nord, Caraïbe anglophone, et la partie hollandaise de l'île. Un site en français seul rate la moitié d'entre eux. Je livre votre site en français, et j'ajoute une version anglaise complète pour 290 € : mêmes pages, même design, avec un sélecteur de langue. Vos clients de Philipsburg comme ceux de Marigot se retrouvent sur la même adresse.</p>

<h2>Combien coûte un site internet à Saint-Martin ?</h2>
<p>490 € pour un site une page, 990 € pour un site complet, 1 390 € avec prise de réservation ou de rendez-vous en ligne. Version anglaise : 290 € en plus. Prix fermes, payés une fois, zéro abonnement, hébergement environ 25 € par an à votre nom.</p>
{PLANS}

<h2>Pour quels commerces de Saint-Martin ?</h2>
<p>Restaurants et bars de Grand-Case et d'Orient Bay, villas et locations des Terres Basses, activités nautiques et excursions, loueurs de voitures et de scooters, boutiques de Marigot, artisans et services de Cul-de-Sac, Quartier d'Orléans et Concordia. Pour la location et l'activité touristique, un site qui prend les réservations en direct vous évite les commissions des plateformes.</p>

<h2>Comment ça se passe à distance ?</h2>
<p>Un appel ou une visio de 30 minutes pour cadrer, la maquette sur WhatsApp, deux tours de corrections, puis la mise en ligne. Vos photos et vos textes arrivent par WhatsApp ou par mail. Tout est fait en quelques jours, et le SAV gratuit à vie fonctionne de la même façon : un message, une correction.</p>

<h2>Des sites en ligne, faits pour les Antilles</h2>
{WORKS}

<h2>Questions fréquentes, Saint-Martin</h2>
""",
    faq=[
        ("Le site peut-il être uniquement en anglais ?", "Oui. Le site est livré dans la langue que vous voulez : français, anglais, ou les deux avec un sélecteur. La version dans une seconde langue coûte 290 €."),
        ("Vous prenez les réservations en direct ?", "Oui, avec la formule Signature ou l'option prise de réservation à 190 € : calendrier, confirmation automatique, rappels. Vous gardez la commission que vous versiez aux plateformes."),
        ("Le nom de domaine, en .fr, en .com ou en .sx ?", "Ce que vous voulez. Pour une clientèle internationale, je conseille souvent un .com. Il est acheté à votre nom, environ 25 € par an avec l'hébergement."),
        ("Vous vous déplacez à Saint-Martin ?", "Tout se fait à distance, et ça suffit dans la grande majorité des cas. Pour un gros projet, je peux venir."),
    ],
))

# ------------------------------------------------------------------ SAINT-BARTH
PAGES.append(dict(
    slug="creation-site-internet-saint-barthelemy", crumb="Saint-Barthélemy",
    title="Création de site internet à Saint-Barthélemy : sur mesure, bilingue, sans abonnement | Studio Novalem",
    desc="Création de site internet à Saint-Barthélemy pour villas, restaurants, boutiques et services. Site codé sur mesure, version anglaise, prix ferme dès 490 €, zéro abonnement. Gustavia, Saint-Jean, Lorient, Flamands.",
    kicker="Création de sites internet", where="à Saint-Barth", geoplace="Saint-Barthélemy", georegion="BL",
    h1="Création de site internet à Saint-Barthélemy", pose="pointe",
    lead="Un site codé sur mesure, soigné, bilingue si vous le souhaitez, pour votre commerce de Saint-Barth. Prix ferme dès 490 €, livré en 7 jours, zéro abonnement, tout se fait à distance.",
    service="Création de site internet à Saint-Barthélemy", area=["Saint-Barthélemy"],
    wa="Bonjour Louis, je suis à Saint-Barth et je voudrais un site pour mon commerce.",
    related=[("site-internet-location-gite-guadeloupe", "Un site pour votre villa ou votre location"), ("site-internet-commerce-guadeloupe", "Un site pour votre boutique"), ("agence-web-guadeloupe-ou-freelance", "Agence web ou indépendant ?")],
    body="""
<h2>Un site à la hauteur de Saint-Barth, sans le prix d'une agence</h2>
<p>À Saint-Barthélemy, une clientèle exigeante attend un site rapide, élégant, en français et en anglais. Une agence facture ce genre de site 4 000 à 8 000 €. Je le code sur mesure pour 990 € en formule Vitrine, plus 290 € pour la version anglaise, et vous n'avez aucun abonnement ensuite. Le design est fait pour vous, avec vos photos, et le site est à vous.</p>

<h2>Combien coûte un site internet à Saint-Barthélemy ?</h2>
<p>490 € pour une page, 990 € pour un site complet jusqu'à 5 pages, 1 390 € avec réservation ou prise de rendez-vous en ligne. Version anglaise 290 €. Hébergement environ 25 € par an, à votre nom. Prix fermes, payés une fois.</p>
{PLANS}

<h2>Pour qui, à Saint-Barth ?</h2>
<p>Villas et locations de Saint-Jean, Lorient, Flamands ou Gouverneur, restaurants et bars de Gustavia, boutiques et concept stores, conciergeries, loueurs de voitures, activités nautiques, services à la personne, artisans. Pour une villa, un site avec galerie plein écran, calendrier de disponibilités et demande de réservation directe vous évite les commissions des plateformes et vous donne une adresse à transmettre à vos clients fidèles.</p>

<h2>Comment ça se passe à distance ?</h2>
<p>Un appel ou une visio de 30 minutes, la maquette sur WhatsApp, deux tours de corrections, la mise en ligne. Vos photos arrivent par WhatsApp, mail ou lien de partage. Le SAV gratuit à vie fonctionne de la même manière.</p>

<h2>Des sites en ligne, faits pour les Antilles</h2>
{WORKS}

<h2>Questions fréquentes, Saint-Barthélemy</h2>
""",
    faq=[
        ("Pouvez-vous faire un site plus haut de gamme que la formule Vitrine ?", "Oui. La formule Signature (1 390 €) et le sur mesure permettent galeries plein écran, calendrier de disponibilités, réservation directe, espace client. On établit le cahier des charges ensemble et le prix est ferme avant de commencer."),
        ("Le site sera-t-il bilingue ?", "Si vous le souhaitez : français et anglais avec un sélecteur, pour 290 € en plus. Vous fournissez ou faites relire la traduction, ou je m'en charge avec un traducteur en supplément."),
        ("Comment se passe le paiement ?", "40 % à la commande, le solde à la mise en ligne, par virement ou carte. Devis et factures en règle."),
        ("Vous vous déplacez à Saint-Barth ?", "Tout se fait à distance. Pour un projet important, je peux venir."),
    ],
))

# ------------------------------------------------------------------ METIERS
PAGES.append(dict(
    slug="site-internet-restaurant-guadeloupe", crumb="Restaurant", crumbs=[("Guadeloupe", "creation-site-internet-guadeloupe")],
    title="Site internet pour restaurant en Guadeloupe : carte en ligne, réservation WhatsApp, dès 490 €",
    desc="Site internet pour restaurant, lolo ou food truck en Guadeloupe : carte lisible sur téléphone, horaires, itinéraire, réservation par WhatsApp. Codé sur mesure dès 490 €, livré en 7 jours, zéro abonnement.",
    kicker="Site internet", where="pour restaurant", h1="Site internet pour restaurant en Guadeloupe", pose="coco",
    lead="Votre carte lisible sur téléphone, vos horaires, l'itinéraire et un bouton pour réserver sur WhatsApp. Un site codé sur mesure pour votre restaurant, lolo ou food truck, dès 490 €, livré en 7 jours.",
    service="Site internet pour restaurant en Guadeloupe", area=["Guadeloupe", "Martinique", "Saint-Martin", "Saint-Barthélemy"],
    wa="Bonjour Louis, j'ai un restaurant et je voudrais un site.",
    related=[("creation-site-internet-guadeloupe", "Création de site internet en Guadeloupe"), ("site-internet-ou-page-facebook", "Site internet ou page Facebook ?"), ("prix-site-internet-guadeloupe", "Combien coûte un site internet ?")],
    body="""
<h2>Ce qu'un client cherche sur le site d'un restaurant</h2>
<p>Trois choses, dans cet ordre : la carte et les prix, les horaires du jour, et comment venir ou réserver. Si votre site répond à ces trois questions en moins de dix secondes sur un téléphone, il fait son travail. Tout le reste, la galerie, l'histoire du lieu, les avis, vient en soutien. C'est exactement comme ça que je construis un site de restaurant : la carte d'abord, le bouton Réserver ou Appeler toujours visible, l'itinéraire en un clic.</p>

<h2>Combien coûte un site pour un restaurant ?</h2>
<p>Pour la plupart des restaurants, lolos et food trucks, je conseille la formule Vitrine à 990 € : une page d'accueil, la carte complète par catégorie, une galerie, les infos pratiques et une page contact avec la carte Google. Pour un lolo ou un food truck avec une carte courte, la formule Essentiel à 490 € suffit : tout tient sur une page. Dans les deux cas, prix ferme, payé une fois, zéro abonnement.</p>
{PLANS}

<h2>La carte en ligne : lisible, à jour, et sans refaire le site</h2>
<p>J'intègre votre carte directement à partir de vos menus imprimés ou de vos photos, par catégorie, avec les prix. Quand un plat change, une modification coûte quelques dizaines d'euros et se fait dans la journée. Si votre carte change tous les jours, j'ajoute un petit espace où vous la modifiez vous-même depuis votre téléphone, sur devis.</p>

<h2>Les options qui font vraiment la différence pour un restaurant</h2>
<ul class="seo-list">
  <li><b>Réservation par WhatsApp</b> avec message pré-rempli (60 €) : le client écrit « table pour 4 ce soir » en un clic</li>
  <li><b>Avis Google en direct</b> sur le site (90 €) : vos meilleurs avis rassurent avant même l'appel</li>
  <li><b>Menu ou carte imprimée</b> dans le style du site, avec QR code vers la carte en ligne (dès 120 €)</li>
  <li><b>Fiche Google Business</b> créée ou reprise (150 €) : c'est elle qui vous fait apparaître sur la carte quand on cherche « restaurant » plus votre commune</li>
  <li><b>Agent IA au téléphone</b> qui prend les réservations quand vous êtes en service (sur devis)</li>
</ul>

<h2>Un exemple : IFC à Sainte-Anne et Le Manaïa</h2>
<p>Pour IFC, roulotte de sorbets artisanaux sur la plage de Sainte-Anne, j'ai livré en 7 jours un site avec le concept, la carte, une galerie et une demande de devis pour les événements. Pour Le Manaïa, restaurant de plage, la carte complète est en ligne par catégorie, à partir de leurs menus imprimés, avec galerie, itinéraire et réservation par WhatsApp.</p>
{WORKS}

<h2>Questions fréquentes des restaurateurs</h2>
""",
    faq=[
        ("Je n'ai pas de belles photos de mes plats.", "Je vous guide pour les prendre avec votre téléphone, en lumière naturelle, et je les retouche. Trois ou quatre bonnes photos suffisent pour un site qui donne faim."),
        ("Ma carte change souvent, comment je fais ?", "Une modification ponctuelle coûte quelques dizaines d'euros et se fait dans la journée. Si ça change tous les jours, j'ajoute un espace où vous modifiez la carte vous-même depuis votre téléphone."),
        ("Est-ce que mes clients pourront réserver en ligne ?", "Oui, de deux façons : un bouton WhatsApp avec message pré-rempli (60 €), ou une vraie réservation en ligne avec calendrier et confirmation automatique (190 € en option, comprise dans la formule Signature)."),
        ("Combien de temps pour le site de mon restaurant ?", "7 jours pour une page, 10 à 14 jours pour un site complet avec la carte par catégorie, à partir du rendez-vous de cadrage."),
    ],
))

PAGES.append(dict(
    slug="site-internet-artisan-guadeloupe", crumb="Artisan", crumbs=[("Guadeloupe", "creation-site-internet-guadeloupe")],
    title="Site internet pour artisan en Guadeloupe : plombier, électricien, clim, paysagiste, dès 490 €",
    desc="Site internet pour artisan et services à domicile en Guadeloupe : électricien, plombier, climatisation, paysagiste, peintre, éducateur canin. Une page qui fait appeler, demande de devis, dès 490 €, livré en 7 jours.",
    kicker="Site internet", where="pour artisan", h1="Site internet pour artisan en Guadeloupe", pose="marteau",
    lead="Une page qui dit ce que vous faites, votre zone d'intervention, et qui fait appeler. Pour électriciens, plombiers, climaticiens, paysagistes, peintres et tous les services à domicile. Dès 490 €, livré en 7 jours.",
    service="Site internet pour artisan en Guadeloupe",
    wa="Bonjour Louis, je suis artisan et je voudrais un site.",
    related=[("creation-site-internet-guadeloupe", "Création de site internet en Guadeloupe"), ("prix-site-internet-guadeloupe", "Combien coûte un site internet ?"), ("agence-web-guadeloupe-ou-freelance", "Agence web ou indépendant ?")],
    body="""
<h2>Un artisan a besoin d'une page qui fait appeler, pas d'un site de dix pages</h2>
<p>Quand une clim tombe en panne à Baie-Mahault ou qu'une fuite se déclare au Gosier, la personne cherche « climatisation Baie-Mahault » ou « plombier Le Gosier » sur son téléphone et appelle le premier qui inspire confiance. Votre site doit donc faire trois choses : dire clairement ce que vous faites et où, montrer que vous êtes sérieux (photos de chantiers, avis, assurance), et mettre un bouton Appeler sous le pouce. C'est la formule Essentiel, 490 €, une page, livrée en 7 jours.</p>

<h2>Combien coûte un site pour un artisan ?</h2>
{PLANS}
<p>Si vous avez plusieurs métiers (électricité et clim, plomberie et chauffe-eau solaire), la formule Vitrine à 990 € donne une page par service : chaque page peut ressortir sur Google pour sa propre recherche.</p>

<h2>Les options utiles pour un artisan</h2>
<ul class="seo-list">
  <li><b>Formulaire de devis</b> en plusieurs étapes (150 €) : le client décrit son besoin, vous recevez tout par mail</li>
  <li><b>Fiche Google Business</b> (150 €) : indispensable pour apparaître sur la carte avec vos avis</li>
  <li><b>Bouton WhatsApp</b> (60 €) : beaucoup de clients préfèrent envoyer une photo de la panne</li>
  <li><b>Carte de visite et flyer</b> avec QR code vers le site (dès 60 €), pour laisser quelque chose après chaque intervention</li>
</ul>

<h2>Ce que je mets sur la page d'un artisan</h2>
<p>Vos services, en langage simple. Votre zone : les communes où vous intervenez, nommées, parce que c'est ce que vos clients tapent sur Google. Trois à six photos de chantiers réels. Vos garanties : assurance décennale, devis gratuit, délai d'intervention. Vos avis Google. Et partout, le bouton Appeler.</p>

<h2>Un exemple : Love Dog's, services canins à domicile</h2>
<p>Pour Love Dog's, éducateur canin et dog sitter sur toute la Guadeloupe, la page présente les trois services dès le premier écran, et un simulateur de tarifs permet au client de savoir en trois clics ce que ça lui coûterait. Résultat : des demandes plus précises, et moins d'appels pour rien.</p>
{WORKS}

<h2>Questions fréquentes des artisans</h2>
""",
    faq=[
        ("Une seule page, ça suffit vraiment ?", "Pour un artisan avec un ou deux services, oui : Google positionne très bien une page claire qui nomme le métier et les communes. Si vous avez plusieurs métiers distincts, une page par service (formule Vitrine) fait ressortir chacun sur sa propre recherche."),
        ("Je travaille sur toute la Guadeloupe, comment le dire ?", "On nomme les communes où vous intervenez le plus, et on indique la zone globale. Ce sont ces noms de communes que vos clients tapent."),
        ("Je n'ai pas le temps de m'en occuper.", "C'est prévu : 30 minutes au téléphone, vous m'envoyez quelques photos par WhatsApp, et je fais le reste. Vous validez la maquette, c'est tout."),
        ("Et pour recevoir les demandes de devis ?", "Le formulaire arrive directement dans votre boîte mail, avec le téléphone du client. Avec l'option formulaire de devis, il décrit son besoin en plusieurs étapes et peut joindre une photo."),
    ],
))

PAGES.append(dict(
    slug="site-internet-commerce-guadeloupe", crumb="Commerce", crumbs=[("Guadeloupe", "creation-site-internet-guadeloupe")],
    title="Site internet pour commerce et boutique en Guadeloupe : horaires, produits, itinéraire, dès 490 €",
    desc="Site internet pour commerce, boutique, garage ou concession en Guadeloupe : produits, horaires, itinéraire, avis Google, boutique en ligne en option. Codé sur mesure dès 490 €, zéro abonnement.",
    kicker="Site internet", where="pour commerce", h1="Site internet pour commerce et boutique en Guadeloupe", pose="plaque",
    lead="Vos produits ou vos services, vos horaires, l'itinéraire et vos avis Google, sur un site codé pour votre boutique. Dès 490 €, livré en 7 jours, zéro abonnement. Boutique en ligne possible en option.",
    service="Site internet pour commerce en Guadeloupe",
    wa="Bonjour Louis, j'ai un commerce et je voudrais un site.",
    related=[("creation-site-internet-guadeloupe", "Création de site internet en Guadeloupe"), ("refonte-site-wix-wordpress-guadeloupe", "Refaire un site Wix ou WordPress"), ("site-internet-ou-page-facebook", "Site internet ou page Facebook ?")],
    body="""
<h2>Un commerce a besoin d'être trouvé, puis d'être choisi</h2>
<p>Trouvé : quand quelqu'un cherche « boutique de décoration Jarry », « garage Le Moule » ou « concession moto Guadeloupe », votre site et votre fiche Google doivent apparaître. Choisi : une fois sur le site, la personne doit voir en quelques secondes ce que vous vendez, à quels horaires, et comment venir. Un site bien fait fait les deux ; une page Facebook ne fait ni l'un ni l'autre.</p>

<h2>Combien coûte un site pour un commerce ?</h2>
{PLANS}
<p>Pour un commerce, je conseille le plus souvent la formule Vitrine à 990 € : une page par rayon ou par service, une galerie, et le référencement complet. Pour vendre en ligne, on ajoute une boutique (catalogue, panier, paiement sécurisé) à partir de 900 €, sur devis.</p>

<h2>Les options utiles pour un commerce</h2>
<ul class="seo-list">
  <li><b>Fiche Google Business</b> créée ou optimisée (150 €) : horaires, photos, avis, sur la carte</li>
  <li><b>Avis Google en direct</b> sur le site (90 €)</li>
  <li><b>Flyer ou affiche</b> pour la devanture avec QR code vers le site (dès 90 €)</li>
  <li><b>Boutique en ligne</b> avec paiement (dès 900 €) : click and collect ou livraison</li>
  <li><b>Réponses WhatsApp et Instagram automatiques</b> pour répondre aux questions courantes jour et nuit (sur devis)</li>
</ul>

<h2>Un exemple : Unik'eau et Focus Moto</h2>
<p>Pour Unik'eau, fontaines à eau sur réseau pour les entreprises, une page claire présente les deux forfaits avec un contact WhatsApp direct. Pour Focus Moto, concession moto, scooter et quad, le site présente les gammes et les services pour amener le client en magasin.</p>
{WORKS}

<h2>Questions fréquentes des commerçants</h2>
""",
    faq=[
        ("Je veux vendre en ligne, c'est possible ?", "Oui. On part d'un site Vitrine à 990 € et on ajoute une boutique avec catalogue, panier, paiement sécurisé et suivi des commandes, à partir de 900 €. Le prix exact dépend du nombre de produits et des options (livraison, retrait en magasin)."),
        ("J'ai déjà un site fait sur Wix, je peux le refaire ?", "Oui, et vous arrêtez l'abonnement. Je reprends vos contenus, je garde vos adresses de pages pour ne pas perdre votre référencement, et le site devient à vous."),
        ("Mes horaires changent selon la saison.", "Une modification d'horaires coûte quelques dizaines d'euros et se fait dans la journée. Je les mets aussi à jour sur votre fiche Google si vous prenez l'option."),
        ("Combien de temps pour le site de ma boutique ?", "10 à 14 jours pour un site Vitrine complet, à partir du rendez-vous de cadrage. 7 jours pour une page."),
    ],
))

PAGES.append(dict(
    slug="site-internet-location-gite-guadeloupe", crumb="Gîte et location", crumbs=[("Guadeloupe", "creation-site-internet-guadeloupe")],
    title="Site internet pour gîte, villa et location en Guadeloupe : réservation en direct, sans commission",
    desc="Site internet pour gîte, villa, location saisonnière ou location de voitures en Guadeloupe : galerie, disponibilités, demande de réservation directe sans commission. Codé sur mesure dès 490 €, version anglaise possible.",
    kicker="Site internet", where="pour location", h1="Site internet pour gîte, villa et location en Guadeloupe", pose="coco",
    lead="Une galerie qui donne envie, vos tarifs, et une demande de réservation directe pour arrêter de verser 15 à 20 % de commission aux plateformes. Site codé sur mesure dès 490 €, version anglaise possible.",
    service="Site internet pour gîte et location en Guadeloupe",
    wa="Bonjour Louis, j'ai une location et je voudrais un site.",
    related=[("creation-site-internet-saint-martin", "Création de site à Saint-Martin"), ("creation-site-internet-saint-barthelemy", "Création de site à Saint-Barth"), ("prix-site-internet-guadeloupe", "Combien coûte un site internet ?")],
    body="""
<h2>Pourquoi un gîte ou une villa a besoin de son propre site</h2>
<p>Parce que chaque réservation passée par une plateforme vous coûte 15 à 20 % de commission, et que vos clients fidèles n'ont aucune adresse à laquelle revenir. Un site à vous, avec vos photos, vos tarifs et un formulaire de réservation directe, récupère une partie de ces réservations. Sur une saison, la différence paie le site plusieurs fois. Et sur Google, « gîte Sainte-Anne » ou « villa piscine Saint-François » vous amène des clients qui ne sont pas passés par les plateformes.</p>

<h2>Combien coûte un site pour une location ?</h2>
{PLANS}
<p>Pour un gîte unique, une page Essentiel à 490 € suffit : galerie, équipements, tarifs, disponibilités, demande de réservation. Pour plusieurs logements ou une location de véhicules, la formule Vitrine à 990 € donne une page par logement ou par véhicule. Version anglaise : 290 €.</p>

<h2>Ce que contient un site de location bien fait</h2>
<ul class="seo-list">
  <li>Une galerie plein écran, avec vos vraies photos (je vous guide pour les prendre)</li>
  <li>Les équipements, la capacité, la distance des plages et de l'aéroport</li>
  <li>Les tarifs par saison, clairement affichés</li>
  <li>Un formulaire de demande de réservation qui arrive sur votre WhatsApp ou votre mail</li>
  <li>La carte pour situer le logement, et vos avis Google ou Booking reformulés</li>
  <li>En option, un calendrier de disponibilités synchronisé et la réservation en ligne (190 €)</li>
</ul>

<h2>Location de voitures, scooters, bateaux : même logique</h2>
<p>Pour un loueur, une page par catégorie de véhicule, les tarifs, les conditions, la remise à l'aéroport, et une demande de réservation directe. Pour les excursions et activités nautiques, une page par activité avec les horaires, les tarifs et la réservation.</p>
{WORKS}

<h2>Questions fréquentes des loueurs</h2>
""",
    faq=[
        ("Puis-je garder Airbnb et Booking en plus du site ?", "Bien sûr. Le site sert à récupérer les clients directs et les clients fidèles, et à vous rendre visible sur Google. Les plateformes restent un canal parmi d'autres, sans être le seul."),
        ("Le calendrier de disponibilités peut-il être synchronisé ?", "Oui, avec l'option prise de réservation (190 €) : le calendrier se synchronise avec vos plateformes et évite les doubles réservations."),
        ("Mes clients sont souvent étrangers.", "La version anglaise complète coûte 290 €, avec un sélecteur de langue. Pour Saint-Martin et Saint-Barth, c'est presque toujours conseillé."),
        ("Combien de temps pour le site de mon gîte ?", "7 jours pour une page, 10 à 14 jours pour plusieurs logements."),
    ],
))

PAGES.append(dict(
    slug="site-internet-coiffeur-beaute-guadeloupe", crumb="Coiffeur et beauté", crumbs=[("Guadeloupe", "creation-site-internet-guadeloupe")],
    title="Site internet pour coiffeur, institut de beauté et bien-être en Guadeloupe : prise de rendez-vous en ligne",
    desc="Site internet pour salon de coiffure, barbier, institut de beauté, onglerie, massage ou cabinet en Guadeloupe : prestations, tarifs, prise de rendez-vous en ligne sans décrocher. Dès 490 €, livré en 7 jours.",
    kicker="Site internet", where="pour la beauté", h1="Site internet pour coiffeur, beauté et bien-être en Guadeloupe", pose="tel",
    lead="Vos prestations, vos tarifs, vos photos, et une prise de rendez-vous en ligne pour ne plus décrocher entre deux clientes. Site codé sur mesure dès 490 €, livré en 7 jours.",
    service="Site internet pour coiffeur et institut de beauté en Guadeloupe",
    wa="Bonjour Louis, j'ai un salon et je voudrais un site avec prise de rendez-vous.",
    related=[("creation-site-internet-guadeloupe", "Création de site internet en Guadeloupe"), ("site-internet-ou-page-facebook", "Site internet ou page Facebook ?"), ("prix-site-internet-guadeloupe", "Combien coûte un site internet ?")],
    body="""
<h2>Le problème d'un salon : le téléphone sonne quand vous avez les mains prises</h2>
<p>Une cliente qui n'a pas de réponse rappelle rarement. Un site avec prise de rendez-vous en ligne règle ça : elle choisit sa prestation, son créneau, elle reçoit une confirmation et un rappel, et vous voyez tout dans votre agenda. Sur Google, « coiffeur Le Gosier », « barbier Pointe-à-Pitre » ou « onglerie Baie-Mahault » vous amènent de nouvelles clientes qui n'auraient jamais trouvé une page Instagram.</p>

<h2>Combien coûte un site pour un salon ?</h2>
{PLANS}
<p>Pour la plupart des salons, je conseille la formule Essentiel à 490 € avec l'option prise de rendez-vous à 190 € : une page avec vos prestations, vos tarifs, vos photos, et le module de réservation. Pour un institut avec beaucoup de prestations, ou un cabinet avec plusieurs praticiens, la formule Signature à 1 390 € comprend la prise de rendez-vous et une page par soin.</p>

<h2>Ce que je mets sur le site d'un salon ou d'un institut</h2>
<ul class="seo-list">
  <li>Vos prestations avec les tarifs, par catégorie</li>
  <li>Une galerie de vos réalisations (coupes, colorations, ongles, avant-après)</li>
  <li>Les horaires, l'itinéraire, le bouton Appeler et WhatsApp</li>
  <li>Le module de rendez-vous en ligne, avec confirmation et rappel automatiques</li>
  <li>Vos avis Google, affichés en direct (option 90 €)</li>
  <li>Le lien vers votre Instagram, et en option des réponses automatiques aux messages</li>
</ul>

<h2>Et pour un cabinet de santé ou de bien-être ?</h2>
<p>Kinésithérapeute, ostéopathe, sophrologue, masseur, coach : même logique. Une page par soin ou par praticien, la prise de rendez-vous en ligne, les tarifs et les remboursements éventuels. La formule Signature est faite pour ça.</p>
{WORKS}

<h2>Questions fréquentes des salons et cabinets</h2>
""",
    faq=[
        ("La prise de rendez-vous en ligne, ça marche comment ?", "La cliente choisit une prestation et un créneau dans les disponibilités que vous avez définies, elle reçoit une confirmation par SMS ou mail, puis un rappel avant le rendez-vous. Vous voyez tout dans un agenda, et vous pouvez toujours bloquer ou déplacer un créneau."),
        ("Je travaille déjà avec Instagram, à quoi sert le site ?", "Instagram montre votre travail à ceux qui vous suivent déjà. Le site vous fait trouver par ceux qui cherchent un salon sur Google dans votre commune, et il prend les rendez-vous. Les deux se complètent : le site renvoie vers Instagram, et votre bio Instagram renvoie vers le site."),
        ("Je n'ai pas de photos professionnelles.", "Vos photos de réalisations prises au téléphone, en lumière naturelle, suffisent. Je vous donne quelques règles simples et je les retouche."),
        ("Combien de temps pour le site de mon salon ?", "7 jours pour une page avec prise de rendez-vous, 3 semaines pour la formule Signature."),
    ],
))

# ------------------------------------------------------------------ GUIDES
PAGES.append(dict(
    slug="prix-site-internet-guadeloupe", crumb="Prix d'un site internet", article=True,
    about="Prix d'un site internet en Guadeloupe et aux Antilles",
    title="Combien coûte un site internet en Guadeloupe en 2026 ? Prix réels, agence, freelance, Wix",
    desc="Prix d'un site internet en Guadeloupe en 2026 : 490 à 1 390 € chez un indépendant, 3 000 à 6 000 € en agence, 35 € par mois à vie sur un constructeur. Ce qui est compris, les frais cachés, et ce que ça coûte sur 5 ans.",
    kicker="Guide", where="prix 2026", h1="Combien coûte un site internet en Guadeloupe ?", pose="plaque",
    lead="Entre 490 € et 6 000 € selon qui le fait et comment. Voici les vrais prix en 2026, ce qui est compris, les frais qui reviennent tous les mois, et ce que ça coûte sur 5 ans.",
    wa="Bonjour Louis, j'ai lu votre guide sur les prix et je voudrais un devis.",
    related=[("aides-site-internet-guadeloupe", "Faire financer son site jusqu'à 80 % par la Région"), ("agence-web-guadeloupe-ou-freelance", "Agence web ou indépendant ?"), ("creation-site-internet-guadeloupe", "Création de site internet en Guadeloupe")],
    body="""
<h2>Les trois façons d'avoir un site, et leur prix</h2>
<table class="seo-table">
  <thead><tr><th>Solution</th><th>Prix de départ</th><th>Frais récurrents</th><th>Le site est à vous ?</th></tr></thead>
  <tbody>
    <tr><td>Constructeur en ligne (Wix, Jimdo, Squarespace)</td><td>0 €</td><td>25 à 40 € par mois, pour toujours</td><td>Non</td></tr>
    <tr><td>Indépendant qui code sur mesure (Studio Novalem)</td><td>490 à 1 390 €</td><td>Environ 25 € par an d'hébergement</td><td>Oui, fichiers remis</td></tr>
    <tr><td>Agence web en Guadeloupe</td><td>3 000 à 6 000 €</td><td>Maintenance 40 à 80 € par mois, souvent obligatoire</td><td>Parfois, selon le contrat</td></tr>
  </tbody>
</table>
<p>Le prix de départ trompe. Un constructeur en ligne semble gratuit, mais 35 € par mois pendant 5 ans font 2 100 €, et à la fin vous ne possédez rien : le jour où vous arrêtez de payer, le site disparaît. Une agence facture 3 500 € en moyenne un site vitrine, puis une maintenance mensuelle. Un site codé sur mesure par un indépendant se paie une fois, et le seul frais qui reste est l'hébergement.</p>

<h2>Ce que ça coûte vraiment sur 5 ans</h2>
<ul class="seo-list">
  <li><b>Constructeur en ligne :</b> environ 2 100 € (35 € × 60 mois), site jamais à vous</li>
  <li><b>Studio Novalem, formule Vitrine :</b> environ 1 115 € (990 € + 5 × 25 € d'hébergement), site à vous</li>
  <li><b>Agence :</b> environ 6 500 € (3 500 € + 50 € × 60 mois)</li>
</ul>
<p>Ce sont des moyennes du marché pour un site vitrine comparable de 5 pages. Les prix exacts varient selon les prestataires, mais l'ordre de grandeur est stable depuis plusieurs années.</p>

<h2>Qu'est-ce qui fait varier le prix d'un site ?</h2>
<p>Quatre choses. Le nombre de pages : une page coûte moins cher que dix. Les fonctions : un formulaire de contact est compris partout, une prise de rendez-vous en ligne ou une boutique se chiffrent en plus. Le contenu : si vous fournissez photos et textes, c'est plus rapide ; si tout est à créer, ça prend plus de temps. Et le prestataire : une agence a des locaux, des commerciaux et des chefs de projet à payer, un indépendant non.</p>

<h2>Mes prix, en clair</h2>
{PLANS}
<p>Les options les plus demandées : bouton WhatsApp 60 €, avis Google en direct 90 €, fiche Google Business 150 €, formulaire de devis 150 €, prise de rendez-vous 190 €, version anglaise 290 €, boutique en ligne dès 900 €. Tout est chiffré avant de commencer, et le prix annoncé est le prix payé.</p>

<h2>Les frais cachés à vérifier avant de signer</h2>
<ul class="seo-list">
  <li>La maintenance obligatoire : chez moi, il n'y en a pas, le site tourne seul</li>
  <li>Le nom de domaine au nom du prestataire : chez moi, il est à votre nom</li>
  <li>Les frais pour récupérer les fichiers du site : chez moi, 0 €, ils sont remis à la livraison</li>
  <li>Le thème ou le gabarit à acheter : chez moi, le design est fait sur mesure</li>
  <li>Le prix des modifications : chez moi, une modification simple coûte dès 20 €, et les bugs sont corrigés gratuitement à vie</li>
</ul>

<h2>Questions fréquentes sur le prix d'un site</h2>
""",
    faq=[
        ("Pourquoi un site codé coûte-t-il moins cher qu'en agence ?", "Pas de locaux, pas de commercial, pas de chef de projet, pas de sous-traitance. Je code moi-même, augmenté à l'IA, ce qui me fait gagner beaucoup de temps. Le résultat est le même, souvent plus rapide, pour 3 à 5 fois moins cher."),
        ("Un site à 490 €, c'est sérieux ?", "Oui, à condition de savoir ce que c'est : une page, codée sur mesure, rapide, avec les boutons Appeler et WhatsApp, un formulaire et la mise en ligne. C'est exactement ce qu'il faut à un artisan ou à un petit commerce. Ce n'est pas un site de dix pages avec boutique."),
        ("Y a-t-il un abonnement ?", "Non. Le site est payé une fois. Le seul frais récurrent est l'hébergement et le nom de domaine, environ 25 € par an, facturés à votre nom."),
        ("Comment se passe le paiement ?", "40 % à la commande, le solde à la mise en ligne, par virement ou carte. Devis et factures en règle, TVA non applicable."),
    ],
))

PAGES.append(dict(
    slug="site-internet-ou-page-facebook", crumb="Site ou page Facebook", article=True,
    about="Différence entre un site internet et une page Facebook pour un commerce",
    title="Site internet ou page Facebook pour un commerce en Guadeloupe ? Ce que Google voit, ce que vos clients trouvent",
    desc="Faut-il un site internet quand on a déjà une page Facebook ou Instagram ? Ce qu'une page ne fait pas (Google, horaires, bouton Appeler), ce qu'un site fait, et comment les deux se complètent pour un commerce en Guadeloupe.",
    kicker="Guide", where="Facebook ou site", h1="Site internet ou page Facebook pour mon commerce ?", pose="loupe",
    lead="Les deux, mais pas pour la même chose. La page parle à ceux qui vous suivent déjà. Le site vous fait trouver par ceux qui cherchent votre métier sur Google, et il fait appeler.",
    wa="Bonjour Louis, j'ai une page Facebook et je me demande si j'ai besoin d'un site.",
    related=[("creation-site-internet-guadeloupe", "Création de site internet en Guadeloupe"), ("prix-site-internet-guadeloupe", "Combien coûte un site internet ?"), ("site-internet-restaurant-guadeloupe", "Un site pour votre restaurant")],
    body="""
<h2>Ce qu'une page Facebook ne fait pas</h2>
<p>Elle n'apparaît presque jamais quand quelqu'un cherche « restaurant Sainte-Anne » ou « électricien Baie-Mahault » sur Google. Elle n'a pas d'horaires lisibles en un coup d'œil, pas de carte des prestations, pas de bouton Appeler sous le pouce. Elle vous appartient encore moins qu'un site sur Wix : Facebook peut changer ses règles, réduire votre portée ou fermer votre page. Et elle donne une image « pas encore installé » à un client qui compare deux commerces.</p>

<h2>Ce qu'un site fait, et que la page ne fera jamais</h2>
<ul class="seo-list">
  <li>Apparaître sur Google quand on cherche votre métier plus votre commune</li>
  <li>Répondre en dix secondes : c'est quoi, c'est où, c'est ouvert quand, comment j'appelle</li>
  <li>Afficher votre carte, vos tarifs, vos prestations de façon claire et à jour</li>
  <li>Prendre les réservations ou les rendez-vous, même quand vous ne pouvez pas décrocher</li>
  <li>Vous appartenir : le nom de domaine et les fichiers sont à vous</li>
</ul>

<h2>Ce que la page fait mieux que le site</h2>
<p>Montrer votre quotidien, vos nouveautés, votre ambiance, à ceux qui vous suivent déjà. Faire circuler une promo en un clic. Recevoir des messages. Une page Facebook ou un compte Instagram bien tenu reste utile : le site ne le remplace pas, il le complète.</p>

<h2>Comment les deux se complètent</h2>
<p>Le site est votre adresse fixe : celle que Google montre, celle qui figure sur votre carte de visite, votre devanture et votre fiche Google Business. La page est votre canal d'animation : elle renvoie vers le site pour la carte, les tarifs, la réservation. Votre bio Instagram pointe vers le site. Le site affiche vos derniers posts ou le lien vers votre page. Et vos photos Facebook servent de matière première pour le site : je les récupère et je les intègre.</p>

<h2>Combien ça coûte de passer de la page au site ?</h2>
{PLANS}
<p>Pour la plupart des commerces qui n'ont qu'une page, la formule Essentiel à 490 € est le bon point de départ : une page claire, livrée en 7 jours, qui reprend vos photos et vos infos. Vous gardez votre page Facebook, elle renverra vers le site.</p>

<h2>Questions fréquentes</h2>
""",
    faq=[
        ("J'ai 2 000 abonnés sur Facebook, ça ne suffit pas ?", "Ça prouve que votre commerce plaît. Mais ces 2 000 personnes vous connaissent déjà. Le site sert à toucher ceux qui cherchent votre métier sur Google et ne vous connaissent pas encore."),
        ("Est-ce que Google montre les pages Facebook ?", "Rarement, et jamais aussi bien qu'un site : pas d'horaires, pas d'adresse cliquable, pas de description claire. Pour une recherche locale, Google privilégie les fiches Google Business et les sites."),
        ("Je peux mettre mes posts Facebook ou Instagram sur le site ?", "Oui, en option : vos derniers posts s'affichent sur le site. Et je récupère vos photos existantes pour construire le site."),
        ("Combien de temps pour passer de la page au site ?", "7 jours pour une page à partir de notre rendez-vous, avec vos photos Facebook comme base."),
    ],
))

PAGES.append(dict(
    slug="agence-web-guadeloupe-ou-freelance", crumb="Agence ou indépendant", article=True,
    about="Choisir entre une agence web et un développeur indépendant en Guadeloupe",
    title="Agence web en Guadeloupe ou développeur indépendant : comparatif honnête pour un commerce",
    desc="Agence web ou freelance pour créer son site en Guadeloupe ? Prix (3 000 à 6 000 € contre 490 à 1 390 €), délais, interlocuteur, propriété du site, SAV. Un comparatif honnête, avec les cas où l'agence est le bon choix.",
    kicker="Guide", where="agence ou indépendant", h1="Agence web en Guadeloupe ou développeur indépendant ?", pose="pointe",
    lead="Pour un commerce, un artisan ou une location, un indépendant qui code sur mesure coûte 3 à 5 fois moins cher, va plus vite, et vous parlez à celui qui fait le site. Pour un grand groupe, l'agence garde ses avantages. Voici le comparatif.",
    wa="Bonjour Louis, je compare agence et indépendant pour mon site.",
    related=[("prix-site-internet-guadeloupe", "Combien coûte un site internet ?"), ("creation-site-internet-guadeloupe", "Création de site internet en Guadeloupe"), ("refonte-site-wix-wordpress-guadeloupe", "Refaire un site Wix ou WordPress")],
    body="""
<h2>Le comparatif en un tableau</h2>
<table class="seo-table">
  <thead><tr><th></th><th>Agence web</th><th>Studio Novalem (indépendant)</th></tr></thead>
  <tbody>
    <tr><td>Prix d'un site vitrine</td><td>3 000 à 6 000 €</td><td>490 à 1 390 €</td></tr>
    <tr><td>Délai</td><td>4 à 12 semaines</td><td>7 à 21 jours</td></tr>
    <tr><td>Interlocuteur</td><td>Commercial, puis chef de projet, puis développeur</td><td>Une seule personne : celui qui code</td></tr>
    <tr><td>Maintenance</td><td>Souvent obligatoire, 40 à 80 € par mois</td><td>Aucune, le site tourne seul</td></tr>
    <tr><td>Propriété du site</td><td>Selon le contrat</td><td>Fichiers remis, domaine à votre nom</td></tr>
    <tr><td>SAV</td><td>Inclus dans la maintenance payante</td><td>Gratuit à vie sur les bugs</td></tr>
    <tr><td>Technologie</td><td>Souvent WordPress avec extensions</td><td>Code natif, sans extension</td></tr>
  </tbody>
</table>

<h2>Quand une agence est le bon choix</h2>
<p>Quand vous avez besoin d'une équipe entière : stratégie de marque, campagnes publicitaires sur plusieurs mois, production vidéo, site de plusieurs dizaines de pages avec plusieurs langues et plusieurs intervenants, ou intégration lourde avec un système d'information existant. Un groupe hôtelier, une collectivité, une enseigne avec plusieurs points de vente ont des raisons de choisir une agence. Un restaurant, un artisan ou une boutique, presque jamais.</p>

<h2>Quand un indépendant est le bon choix</h2>
<p>Quand vous voulez un site propre, rapide, qui fait appeler, livré vite et à un prix ferme. Quand vous voulez parler directement à celui qui code, sans commercial entre les deux. Quand vous ne voulez pas d'abonnement ni de maintenance imposée. Quand vous voulez que le site soit à vous.</p>

<h2>Les questions à poser avant de signer, avec n'importe qui</h2>
<ul class="seo-list">
  <li>Le nom de domaine sera-t-il à mon nom ?</li>
  <li>Aurai-je les fichiers du site à la livraison ?</li>
  <li>Y a-t-il une maintenance obligatoire, et combien ?</li>
  <li>Qui corrige un bug dans un an, et à quel prix ?</li>
  <li>Combien coûte une modification simple ?</li>
  <li>Le délai est-il écrit, et que se passe-t-il s'il n'est pas tenu ?</li>
</ul>
<p>Mes réponses : à votre nom, oui, aucune, moi et gratuitement, dès 20 €, écrit sur le devis avec 10 % de remise par semaine de retard.</p>

<h2>Mes prix</h2>
{PLANS}

<h2>Questions fréquentes</h2>
""",
    faq=[
        ("Un indépendant seul, c'est risqué si vous n'êtes plus disponible ?", "C'est justement pour ça que le site est à vous : fichiers remis, domaine à votre nom, code natif lisible par n'importe quel développeur. Vous n'êtes jamais bloqué."),
        ("Une agence fait-elle un meilleur site ?", "Pas forcément. La qualité dépend de la personne qui conçoit et code, pas de la taille de la structure. Visitez les sites que j'ai livrés et comparez."),
        ("Vous faites aussi la publicité et les réseaux sociaux ?", "Oui, en option : fiche Google Business, Google Ads, réseaux sociaux pilotés par IA, agents de réponse WhatsApp et Instagram. Mais le cœur du métier reste le site, et je vous dis franchement si une option ne sert à rien."),
    ],
))

PAGES.append(dict(
    slug="refonte-site-wix-wordpress-guadeloupe", crumb="Refonte Wix ou WordPress", article=True,
    about="Refaire un site Wix, Jimdo ou WordPress en site codé sur mesure",
    title="Refaire un site Wix, Jimdo ou WordPress en Guadeloupe : arrêter l'abonnement sans perdre son référencement",
    desc="Votre site Wix, Jimdo ou WordPress est lent, cher ou vieux ? Refonte en site codé sur mesure dès 990 €, en gardant vos adresses de pages pour ne pas perdre votre référencement Google. Zéro abonnement ensuite.",
    kicker="Guide", where="refonte", h1="Refaire un site Wix, Jimdo ou WordPress en Guadeloupe", pose="marteau",
    lead="Vous payez 30 à 40 € par mois pour un site lent que vous ne possédez pas ? Je le refais en site codé sur mesure, je garde vos adresses de pages pour ne pas perdre votre référencement, et vous arrêtez l'abonnement.",
    wa="Bonjour Louis, j'ai un site Wix ou WordPress à refaire.",
    related=[("prix-site-internet-guadeloupe", "Combien coûte un site internet ?"), ("creation-site-internet-guadeloupe", "Création de site internet en Guadeloupe"), ("agence-web-guadeloupe-ou-freelance", "Agence web ou indépendant ?")],
    body="""
<h2>Les signes qu'il est temps de refaire votre site</h2>
<ul class="seo-list">
  <li>Il met plus de 3 secondes à s'afficher sur un téléphone en 4G</li>
  <li>Vous payez un abonnement tous les mois depuis des années</li>
  <li>Il n'est pas lisible sur téléphone, ou le bouton Appeler est introuvable</li>
  <li>Vous ne pouvez pas récupérer les fichiers : le site n'est pas à vous</li>
  <li>WordPress demande des mises à jour d'extensions et affiche des alertes de sécurité</li>
  <li>Il a été fait il y a plus de 5 ans et ne vous ressemble plus</li>
</ul>

<h2>Comment je refais un site sans perdre le référencement</h2>
<p>Un site qui existe depuis des années a acquis une place sur Google. Une refonte mal faite la détruit. Voici ce que je fais pour la garder : je liste toutes vos pages actuelles et leurs adresses, je garde les mêmes adresses quand c'est possible et je mets en place des redirections pour les autres, je reprends vos textes en les améliorant, je conserve vos titres qui fonctionnent, et je déclare le nouveau site à Google Search Console dès la mise en ligne. Dans la plupart des cas, le nouveau site, plus rapide et mieux structuré, fait mieux que l'ancien en quelques semaines.</p>

<h2>Combien coûte une refonte ?</h2>
{PLANS}
<p>Une refonte se chiffre comme un site neuf, le plus souvent en formule Vitrine à 990 €, parce que le travail est le même : design, intégration, mise en ligne. La différence, c'est que vous avez déjà les contenus et les photos, ce qui accélère les choses. Et vous arrêtez l'abonnement : sur un site à 35 € par mois, la refonte est remboursée en moins de 3 ans.</p>

<h2>Wix, Jimdo, WordPress : ce qui change avec un site codé</h2>
<p>Un site codé sur mesure n'a pas d'extensions à mettre à jour, pas de thème à payer, pas de faille héritée d'un module tiers, et il est 3 à 5 fois plus rapide, ce que Google mesure et récompense. Il est à vous : les fichiers sont remis, le domaine est à votre nom, et n'importe quel développeur peut le reprendre. En contrepartie, vous ne le modifiez pas dans un éditeur en ligne : une modification simple coûte dès 20 € et se fait dans la journée, ou j'ajoute un petit espace d'édition pour ce qui change souvent.</p>

<h2>Questions fréquentes sur la refonte</h2>
""",
    faq=[
        ("Je vais perdre mon nom de domaine ?", "Non. S'il est chez Wix ou chez un autre registrar, on le transfère à votre nom chez OVH. S'il est déjà à vous, on le pointe simplement vers le nouveau site. Les adresses mail continuent de fonctionner."),
        ("Et mes textes et mes photos ?", "Je les récupère tous depuis votre site actuel avant de couper quoi que ce soit, je les trie et je les améliore."),
        ("Combien de temps sans site pendant la refonte ?", "Zéro. L'ancien site reste en ligne pendant que je construis le nouveau, et la bascule se fait en quelques minutes."),
        ("Je peux garder WordPress mais l'améliorer ?", "Je ne travaille pas sur WordPress : je code sur mesure. Si vous tenez à WordPress, je vous le dis franchement et je vous oriente ailleurs."),
    ],
))


# ------------------------------------------------------------------ FORMULES (detail)
def _formule(slug, nom, prix, delai, pour, inclus, pas_inclus, options, faq, pose):
    return dict(
        slug=slug, crumb="Formule " + nom,
        title="Formule %s à %s : ce qui est compris, délai, options | Studio Novalem" % (nom, prix),
        desc="La formule %s de Studio Novalem à %s : tout ce qui est compris, ce qui ne l'est pas, le délai (%s), les options utiles et comment ça se passe. Prix ferme, payé une fois, zéro abonnement." % (nom, prix, delai.lower()),
        kicker="Formule", where=nom, h1="Formule %s, %s" % (nom, prix), pose=pose,
        lead=pour + " Prix ferme, payé une fois à la mise en ligne, zéro abonnement.",
        service="Site internet formule " + nom,
        wa="Bonjour Louis, la formule %s à %s m'intéresse. Mon commerce : " % (nom, prix),
        related=[(x, y) for x, y in [("formule-essentiel", "Formule Essentiel, 490 €"), ("formule-vitrine", "Formule Vitrine, 990 €"), ("formule-signature", "Formule Signature, 1 390 €")] if x != slug] + [("options-et-abonnements", "Toutes les options")],
        body="""
<h2>Ce qui est compris dans la formule %s</h2>
<ul class="seo-list">%s</ul>
<h2>Ce qui n'est pas compris</h2>
<ul class="seo-list">%s</ul>
<h2>Le délai : %s</h2>
<p>Le compte démarre au rendez-vous de cadrage (30 minutes au téléphone ou sur place). Le délai est écrit sur le devis. Un retard qui m'est imputable ouvre droit à une remise de 10 %% par semaine entamée.</p>
<h2>Comment ça se passe</h2>
<ol class="seo-steps">
  <li><b>Vous m'écrivez</b> le nom de votre commerce, sur WhatsApp ou par téléphone.</li>
  <li><b>Vous recevez un aperçu</b> de votre site sous 48 h, gratuitement, avec vos infos et vos photos.</li>
  <li><b>On ajuste</b> ensemble ce que vous voulez : deux tours de modifications sont compris.</li>
  <li><b>Mise en ligne</b> : domaine, HTTPS, Google. Vous payez à ce moment-là, quand le site vous plaît.</li>
</ol>
<h2>Les options souvent ajoutées à cette formule</h2>
<ul class="seo-list">%s</ul>
<h2>Et après</h2>
<p>Le site est à vous : nom de domaine et hébergement à votre nom (environ 25 €€ par an, seul frais récurrent), fichiers remis. SAV gratuit à vie sur tout ce qui casse à cause de mon code. Une modification de contenu coûte dès 20 €€ et se fait dans la journée. Aucun abonnement obligatoire.</p>
<h2>Les autres formules</h2>
{PLANS}
""".replace("€€", "€") % (nom, "".join("<li>%s</li>" % x for x in inclus), "".join("<li>%s</li>" % x for x in pas_inclus), delai, "".join("<li>%s</li>" % x for x in options)),
        faq=faq,
    )

PAGES.append(_formule("formule-essentiel", "Essentiel", "490 €", "Livré en 7 jours",
    "Une page qui dit ce que vous faites, où, quand, et qui fait appeler. Pour un artisan, un indépendant, un lolo, un salon, une activité locale.",
    ["Un site une page, jusqu'à 6 sections (présentation, services ou carte, photos, avis, infos pratiques, contact)", "Design sur mesure, à vos couleurs, jamais un gabarit", "Boutons Appeler, WhatsApp et itinéraire Google Maps dès le premier écran", "Formulaire de contact qui arrive dans votre boîte mail", "Pensé pour le téléphone d'abord, rapide, sécurisé en HTTPS", "Nom de domaine et hébergement à votre nom, mise en ligne comprise", "Balises Google de base, sitemap, indexation demandée", "Deux tours de modifications avant la mise en ligne", "Fichiers du site remis, SAV gratuit à vie sur les bugs"],
    ["Plusieurs pages (voir Vitrine)", "Prise de rendez-vous en ligne (option 190 € ou formule Signature)", "Boutique en ligne (option dès 900 €)", "Rédaction complète de vos textes (je les écris avec vous au téléphone, c'est compris ; une rédaction longue est chiffrée)", "Photos professionnelles (je vous guide pour les prendre au téléphone)"],
    ["Fiche Google Business créée ou reprise, 150 €", "Avis Google affichés en direct, 90 €", "Formulaire de devis détaillé, 150 €", "Carte de visite avec QR code, 60 €"],
    [("Une seule page, ça suffit pour être trouvé sur Google ?", "Pour un commerce avec un métier et une commune, oui : Google positionne très bien une page claire qui nomme le métier et la zone. Si vous avez plusieurs services distincts, la formule Vitrine donne une page par service."),
     ("Je peux passer à Vitrine plus tard ?", "Oui, à tout moment. On ajoute des pages au site existant, vous ne repayez pas la base."),
     ("Je paie quand ?", "À la mise en ligne, quand le site vous plaît. Avant, l'aperçu et les ajustements sont gratuits.")],
    "salut"))

PAGES.append(_formule("formule-vitrine", "Vitrine", "990 €", "Livré en 10 à 14 jours",
    "Un site complet, une page par service ou par rayon, avec galerie, trouvé sur Google. C'est la formule la plus prise : restaurants, commerces, locations, artisans à plusieurs métiers.",
    ["Jusqu'à 5 pages (accueil + une page par service, rayon, logement ou catégorie)", "Arborescence pensée avec vous au cadrage", "Design sur mesure, à vos couleurs", "Galerie photo ou réalisations", "Formulaire de contact avancé (choix du service, pièces jointes)", "Boutons Appeler, WhatsApp et itinéraire sur chaque page", "Référencement Google complet : titres, descriptions, balisage, données structurées, Search Console et sitemap", "Pensé pour le téléphone d'abord, rapide, HTTPS", "Nom de domaine et hébergement à votre nom, mise en ligne comprise", "Prise en main de 30 minutes à la remise", "Deux tours de modifications, fichiers remis, SAV gratuit à vie sur les bugs"],
    ["Plus de 5 pages (90 € par page supplémentaire)", "Prise de rendez-vous en ligne (option 190 € ou formule Signature)", "Blog avec interface de publication (option 350 € ou formule Signature)", "Boutique en ligne (option dès 900 €)", "Version anglaise (option 290 €)"],
    ["Fiche Google Business, 150 €", "Avis Google en direct, 90 €", "Prise de rendez-vous ou de réservation, 190 €", "Version anglaise, 290 € (Saint-Martin, Saint-Barth, locations)", "Menu ou carte imprimée dans le style du site, dès 120 €"],
    [("Pourquoi c'est la formule la plus prise ?", "Parce qu'une page par service, c'est une page par recherche Google : « coiffeur + commune », « gîte + commune », « plombier + commune ». Chaque page peut ressortir seule. Et le référencement complet est compris."),
     ("Combien de temps exactement ?", "10 à 14 jours après le rendez-vous de cadrage, selon la quantité de contenu. L'aperçu arrive sous 48 h."),
     ("Je peux vendre en ligne avec Vitrine ?", "Oui en ajoutant l'option boutique (catalogue, panier, paiement sécurisé) à partir de 900 €, chiffrée selon le nombre de produits.")],
    "pointe"))

PAGES.append(_formule("formule-signature", "Signature", "1 390 €", "Livré en 3 semaines",
    "Un site qui prend les rendez-vous tout seul et génère des contacts : salons, cabinets, instituts, entreprises qui veulent être trouvées sur chaque recherche.",
    ["Jusqu'à 10 pages : tout le contenu de Vitrine, plus des pages ciblées par service, par soin ou par commune", "Prise de rendez-vous ou de réservation en ligne : calendrier, confirmations et rappels automatiques", "Blog avec interface de publication autonome", "Référencement avancé, y compris pour être cité par les IA (ChatGPT, Perplexity, Google AI)", "Suivi statistiques configuré (visites, appels, demandes)", "Galerie, formulaire avancé, boutons Appeler, WhatsApp et itinéraire partout", "Nom de domaine et hébergement à votre nom, mise en ligne, HTTPS", "Prise en main de 30 minutes, deux tours de modifications, fichiers remis, SAV gratuit à vie sur les bugs"],
    ["Boutique en ligne (option dès 900 €)", "Espace client sécurisé (option 450 €)", "Agents IA téléphone, WhatsApp ou réseaux (sur devis)", "Rédaction d'articles de blog (70 € par article, ou abonnement contenu)"],
    ["Fiche Google Business, 150 €", "Avis Google en direct, 90 €", "Réponses WhatsApp et Instagram automatiques, sur devis", "Abonnement Visibilité, 149 € par mois sans engagement : un article par mois, avis, rapport"],
    [("Signature ou Vitrine + option rendez-vous ?", "Vitrine + rendez-vous (990 + 190 = 1 180 €) suffit à un salon avec une seule adresse. Signature apporte en plus les pages par soin ou par commune, le blog, le référencement avancé et les statistiques : c'est pour ceux qui veulent générer des contacts, pas seulement exister."),
     ("La prise de rendez-vous marche avec mon agenda ?", "Oui : le calendrier se synchronise avec Google Agenda ou un agenda métier, les clients reçoivent confirmation et rappel, et vous gardez la main sur les créneaux."),
     ("Trois semaines, pourquoi plus long ?", "Jusqu'à 10 pages, un module de rendez-vous à configurer avec vos créneaux, un blog et le référencement avancé. L'aperçu arrive quand même sous 48 h.")],
    "drapeau"))

# ------------------------------------------------------------------ OPTIONS ET ABONNEMENTS
PAGES.append(dict(
    slug="options-et-abonnements", crumb="Options et abonnements",
    title="Options, agents IA et abonnements : tous les prix de Studio Novalem",
    desc="Toutes les options à ajouter à un site Studio Novalem : bouton WhatsApp 60 €, avis Google 90 €, prise de rendez-vous 190 €, boutique dès 900 €, fiche Google Business 150 €, agents IA, flyers, et les abonnements sans engagement 39, 149 et 290 € par mois.",
    kicker="Studio Novalem", where="à la carte", h1="Options, agents IA et abonnements", pose="marteau",
    lead="Chaque option s'ajoute à une formule ou à un site déjà en ligne. Rien n'est obligatoire, et je vous dis franchement si une option ne sert à rien dans votre cas.",
    wa="Bonjour Louis, j'ai une question sur une option.",
    related=[("prix-site-internet-guadeloupe", "Combien coûte un site internet ?"), ("creation-site-internet-guadeloupe", "Création de site internet en Guadeloupe")],
    body="""
<h2>Les formules de base</h2>
{PLANS}
<h2>Fonctions du site</h2>
<table class="seo-table"><tbody>
<tr><td>Page supplémentaire</td><td>Design et intégration, contenu fourni par vos soins</td><td>90 €</td></tr>
<tr><td>Bouton WhatsApp</td><td>Contact direct, message pré-rempli</td><td>60 €</td></tr>
<tr><td>Avis Google en direct</td><td>Vos avis affichés automatiquement sur le site</td><td>90 €</td></tr>
<tr><td>Formulaire de devis</td><td>Multi-étapes, envoi automatique</td><td>150 €</td></tr>
<tr><td>Prise de rendez-vous</td><td>Agenda synchronisé, confirmations et rappels automatiques</td><td>190 €</td></tr>
<tr><td>Version multilingue</td><td>Par langue, traduction professionnelle en supplément</td><td>290 €</td></tr>
<tr><td>Espace client sécurisé</td><td>Connexion, documents privés, gestion des comptes</td><td>450 €</td></tr>
<tr><td>Boutique en ligne</td><td>Catalogue, panier, paiement Stripe, commandes</td><td>dès 900 €</td></tr>
</tbody></table>
<h2 id="agents">Agents IA et automatisations</h2>
<table class="seo-table"><tbody>
<tr><td>Agent IA au téléphone</td><td>Il décroche quand vous ne pouvez pas : horaires, tarifs, réservation, message envoyé sur votre WhatsApp</td><td>Sur devis</td></tr>
<tr><td>Réponses WhatsApp et Instagram</td><td>Réponse en quelques secondes jour et nuit, les demandes sérieuses vous remontent</td><td>Sur devis</td></tr>
<tr><td>Réseaux sociaux pilotés par IA</td><td>Posts et stories préparés à partir de vos photos, validés par vous en un clic</td><td>Sur devis, 1 mois d'essai</td></tr>
<tr><td>CRM et automatisations</td><td>Contacts, devis, relances, demandes d'avis, sans double saisie</td><td>Sur devis</td></tr>
</tbody></table>
<h2>Visibilité Google</h2>
<table class="seo-table"><tbody>
<tr><td>Fiche Google Business</td><td>Création ou reprise, photos, horaires, avis</td><td>150 €</td></tr>
<tr><td>Référencement technique</td><td>Audit, balisage, vitesse, jusqu'à 10 pages</td><td>290 €</td></tr>
<tr><td>Blog</td><td>Structure, catégories, interface de publication autonome</td><td>350 €</td></tr>
<tr><td>Rédaction d'articles</td><td>1 000 mots, mots-clés recherchés</td><td>70 € / article</td></tr>
<tr><td>Être cité par les IA</td><td>ChatGPT, Perplexity et Google AI Overviews</td><td>350 €</td></tr>
<tr><td>Google Ads, lancement</td><td>Compte, mots-clés, annonces, suivi</td><td>350 €</td></tr>
<tr><td>Google Ads, pilotage</td><td>Optimisation continue, hors budget publicitaire</td><td>190 € / mois</td></tr>
</tbody></table>
<h2>Imprimés</h2>
<table class="seo-table"><tbody>
<tr><td>Carte de visite</td><td>Recto-verso, QR code vers le site, prêt à imprimer</td><td>60 €</td></tr>
<tr><td>Flyer ou affiche</td><td>Dans le style du site, QR code, prêt à imprimer</td><td>dès 90 €</td></tr>
<tr><td>Menu ou carte</td><td>Versions papier et écran</td><td>dès 120 €</td></tr>
</tbody></table>
<h2>Abonnements, sans engagement</h2>
<p>Mes sites fonctionnent très bien sans abonnement. Ces formules existent pour ceux qui préfèrent me confier la vie du site, le contenu ou la publicité. Résiliables par e-mail, premier mois remboursé si vous n'êtes pas convaincu, et le site reste à vous dans tous les cas.</p>
<table class="seo-table"><tbody>
<tr><td>Tranquillité</td><td>2 modifications par mois, surveillance, sauvegardes, domaine et hébergement gérés</td><td>39 € / mois</td></tr>
<tr><td>Visibilité</td><td>Tranquillité + 1 article par mois, réponses à vos avis Google, ajustements et rapport mensuel</td><td>149 € / mois</td></tr>
<tr><td>Croissance</td><td>Visibilité + pilotage Google Ads, pages de conversion, point téléphonique mensuel</td><td>290 € / mois</td></tr>
</tbody></table>
<h2>Après la livraison</h2>
<table class="seo-table"><tbody>
<tr><td>SAV technique et bugs</td><td>Tout dysfonctionnement corrigé, sans limite de durée</td><td>Gratuit</td></tr>
<tr><td>Maintenance</td><td>Aucune obligation, le site tourne seul</td><td>0 €</td></tr>
<tr><td>Hébergement et domaine</td><td>À votre nom, facturé une fois par an</td><td>~25 € / an</td></tr>
<tr><td>Modification de contenu</td><td>Une photo, un horaire, un tarif</td><td>dès 20 €</td></tr>
<tr><td>Évolution ou refonte</td><td>Nouvelle page, nouvelle fonction, refonte partielle</td><td>Sur devis</td></tr>
</tbody></table>
""",
    faq=[
        ("Puis-je ajouter une option après la mise en ligne ?", "Oui, à tout moment. Une option s'ajoute à un site déjà en ligne au même prix, et le site reste à vous."),
        ("Les abonnements sont-ils obligatoires ?", "Non. Le site tourne seul, sans maintenance imposée. Les abonnements servent uniquement à ceux qui veulent déléguer la vie du site, le contenu ou la publicité."),
    ],
))

# ------------------------------------------------------------------ AIDES
PAGES.append(dict(
    slug="aides-site-internet-guadeloupe", crumb="Aides et financement", article=True,
    about="Aides publiques au financement d'un site internet en Guadeloupe : Chèque TIC de la Région",
    title="Faire financer son site internet en Guadeloupe : le Chèque TIC, jusqu'à 80 % remboursés",
    desc="La Région Guadeloupe rembourse jusqu'à 80 % de la création d'un site internet grâce au Chèque TIC, jusqu'à 10 000 €. Qui y a droit, les pièges à éviter, le dossier pièce par pièce, et comment Studio Novalem le monte avec vous.",
    kicker="Guide", where="aides 2026", h1="Faire financer son site internet par la Région Guadeloupe", pose="plaque",
    lead="Oui, la Région Guadeloupe peut rembourser jusqu'à 80 % de votre site internet grâce au Chèque TIC, cofinancé par l'Europe. Beaucoup de commerçants ne le savent pas, et beaucoup de dossiers échouent pour des erreurs évitables. Voici comment ça marche, et comment je monte le dossier avec vous.",
    wa="Bonjour Louis, je voudrais savoir si mon commerce peut avoir le Chèque TIC pour son site.",
    related=[("prix-site-internet-guadeloupe", "Combien coûte un site internet en Guadeloupe ?"), ("creation-site-internet-guadeloupe", "Création de site internet en Guadeloupe"), ("site-internet-ou-page-facebook", "Site internet ou page Facebook ?")],
    body="""
<h2>Le Chèque TIC de la Région Guadeloupe, c'est quoi ?</h2>
<p>C'est une aide de la Région Guadeloupe, cofinancée par le FEDER (fonds européens), pour aider les petites entreprises de l'archipel à se numériser. Elle peut atteindre <b>10 000 €</b> et couvrir <b>jusqu'à 80 % de votre projet</b>. Et la création ou la refonte d'un site internet vitrine ou boutique fait partie des dépenses prévues, tout comme l'achat de logiciels, la création de contenu et l'animation du site.</p>
<p>Concrètement : une formule Vitrine à 990 € chez moi peut, si votre dossier est retenu, vous revenir à environ 200 € une fois l'aide versée. C'est le même site, le même travail, mais la Région en paie la plus grande partie.</p>

<h2>Qui peut en bénéficier ?</h2>
<ul class="seo-list">
  <li>Les TPE, PME, artisans, auto-entrepreneurs et associations de Guadeloupe, tous secteurs d'activité</li>
  <li>Enregistrés auprès de leur organisme de rattachement <b>depuis au moins un an</b></li>
  <li>Exerçant une activité économique régulière</li>
  <li>À jour de leurs obligations fiscales et sociales</li>
</ul>
<p>Si vous cochez ces cases, vous êtes éligible. Attention, éligible ne veut pas dire garanti : c'est une subvention, la Région instruit chaque dossier et décide. Un dossier bien monté passe beaucoup mieux qu'un formulaire rempli à la va-vite, et c'est exactement là que je vous aide.</p>

<h2>Les trois pièges qui font échouer les dossiers</h2>
<ol class="seo-steps">
  <li><b>Signer le devis avant de déposer la demande.</b> C'est le piège numéro un : la demande doit être déposée avant tout engagement de dépense. Un devis signé trop tôt, et c'est le refus automatique. Avec moi, le calendrier est verrouillé : je vous remets le devis, vous déposez le dossier, et on ne signe qu'après.</li>
  <li><b>Oublier que c'est un remboursement.</b> L'aide n'est pas une avance : vous payez le site, vous présentez les factures acquittées, la Région vous rembourse. Il faut donc prévoir la trésorerie. Mes formules démarrent à 490 €, et on peut étaler le paiement pour lisser l'effort.</li>
  <li><b>Bâcler la note de présentation.</b> Le dossier demande une note de 3 pages qui explique votre projet et son impact sur le numérique de votre entreprise. C'est elle qui fait la différence en commission. Je la rédige avec vous, à partir de ce que je connais déjà de votre projet.</li>
</ol>

<h2>Le dossier, pièce par pièce</h2>
<ul class="seo-list">
  <li>Une lettre de demande d'aide adressée au Président du Conseil régional (modèle fourni par la Région)</li>
  <li>Une note de présentation du projet, 3 pages maximum</li>
  <li>Une attestation de régularité fiscale et sociale</li>
  <li>Trois devis concurrentiels pour chaque prestation</li>
  <li>Un justificatif de capacité d'autofinancement (par exemple vos deux derniers relevés bancaires)</li>
  <li>Un extrait K-bis de moins de 3 mois, ou l'extrait d'inscription à votre répertoire</li>
</ul>
<p>Le dépôt se fait en ligne, sur le portail des aides de la Région Guadeloupe. Un mot sur les trois devis : la Région exige que vous fassiez chiffrer votre projet par trois prestataires différents. C'est normal, c'est de l'argent public. Je vous prépare un mail type à envoyer à d'autres prestataires pour obtenir ces chiffrages sans y passer vos soirées.</p>

<h2>Comment je monte le dossier avec vous</h2>
<p>C'est l'option Accompagnement Chèque TIC, à 290 €. Elle comprend : la vérification de votre éligibilité, la rédaction de la lettre et de la note de présentation à partir de votre projet, la liste exacte des pièces à réunir de votre côté, le mail type pour les devis concurrents, le calage du calendrier pour ne rien signer trop tôt, et le dépôt en ligne fait ensemble, au téléphone ou sur place. Vous ne remplissez rien seul.</p>
<p>Soyons clairs sur un point : je ne peux pas vous garantir l'aide, personne ne le peut, la décision appartient à la Région. Ce que je garantis, c'est un dossier complet, propre et déposé au bon moment, c'est-à-dire un dossier qui a toutes ses chances.</p>

<h2>Les autres aides qui existent</h2>
<ul class="seo-list">
  <li><b>Le Chèque Innovation</b> de la Région Guadeloupe, pour les projets de conseil et d'appui à l'innovation des TPE et PME, utile si votre projet va au-delà du site (outil métier, automatisation)</li>
  <li><b>France Num</b>, le portail national : autodiagnostics et formations gratuites, et un annuaire de prestataires référencés, les Activateurs France Num</li>
  <li><b>Le Prêt Boost Transformation numérique</b>, de 5 000 à 75 000 €, pour les projets plus lourds</li>
  <li><b>Le Diag Numérique de Bpifrance</b>, un audit gratuit avec plan d'action</li>
</ul>
<p>Le cumul des aides publiques est encadré par les règles européennes et plafonné, le plus souvent à 80 % des dépenses. On regarde ensemble ce qui s'applique à votre situation.</p>

<h2>Questions fréquentes sur les aides</h2>
""",
    faq=[
        ("Si je suis éligible, est-ce que l'aide est garantie ?", "Non. C'est une subvention : la Région instruit le dossier et les élus décident en commission, en fonction du dossier et de l'enveloppe budgétaire disponible. Personne ne peut vous garantir l'aide, et méfiez-vous de qui vous la promet. En revanche, un dossier complet, déposé au bon moment, avec une note de présentation solide, a de très bonnes chances : c'est ce que je vous prépare."),
        ("Mon site peut-il vraiment me coûter 5 fois moins cher ?", "Si l'aide est accordée au taux maximum de 80 %, oui : une formule Vitrine à 990 € revient à environ 200 €, et une formule Signature à 1 390 € à environ 280 €. Vous avancez le montant total, la Région vous rembourse sur présentation des factures acquittées."),
        ("Je suis auto-entrepreneur, est-ce que j'y ai droit ?", "Oui, les auto-entrepreneurs et micro-entreprises font partie des bénéficiaires prévus, à condition d'être immatriculé depuis au moins un an, d'exercer une activité régulière et d'être à jour fiscalement et socialement."),
        ("Mon entreprise a moins d'un an, je fais quoi ?", "Le Chèque TIC demande au moins un an d'ancienneté. Deux options : lancer votre site maintenant sans aide, parce qu'attendre un an sans site coûte souvent plus cher que l'aide elle-même, ou commencer par une formule Essentiel à 490 € et déposer un dossier pour une refonte plus ambitieuse quand vous aurez l'ancienneté."),
        ("Combien de temps entre le dépôt du dossier et le site en ligne ?", "Le dossier se prépare en une à deux semaines, le temps de réunir les pièces et les trois devis. Ensuite, l'instruction par la Région prend son propre délai, variable selon les périodes. Le site, lui, est livré en 7 à 21 jours selon la formule une fois le feu vert donné. Je vous aide à caler l'ordre des étapes pour ne pas griller le dossier en signant trop tôt."),
        ("Que se passe-t-il si mon dossier est refusé ?", "Vous restez libre : le devis n'est signé qu'après le dépôt, et si le refus tombe avant la signature, vous décidez de faire le site au prix normal ou d'attendre. L'option Accompagnement à 290 € couvre le travail de montage du dossier, qui est fait dans tous les cas."),
    ],
))

# ------------------------------------------------------------------ MENTIONS LEGALES
PAGES.append(dict(
    slug="mentions-legales", crumb="Mentions légales",
    title="Mentions légales | Studio Novalem",
    desc="Mentions légales du site studionovalem.fr, édité par Studio Novalem, micro-entreprise de création de sites internet en Guadeloupe.",
    kicker="Studio Novalem", where="mentions légales", h1="Mentions légales", pose="plan",
    lead="Les informations légales du site studionovalem.fr.",
    body="""
<h2>Éditeur du site</h2>
<p>Studio Novalem, micro-entreprise, SIRET 103 405 247 00018, dirigée par Louis (nom complet à compléter). Siège en Guadeloupe (adresse à compléter). Contact : contact@studionovalem.fr, +590 691 25 34 49. TVA non applicable, article 293 B du CGI.</p>
<h2>Hébergement</h2>
<p>Le site est hébergé par Vercel Inc., 440 N Barranca Ave #4133, Covina, CA 91723, États-Unis. Le nom de domaine est enregistré chez OVH SAS, 2 rue Kellermann, 59100 Roubaix, France.</p>
<h2>Données personnelles</h2>
<p>Le formulaire de contact collecte un prénom, un nom de commerce, un numéro de téléphone, une île ou une ville et un message, uniquement pour vous rappeler. Ces données sont transmises par le service FormSubmit et conservées dans la messagerie de Studio Novalem le temps de traiter votre demande. Elles ne sont ni revendues ni utilisées pour de la prospection. Vous pouvez demander leur suppression à contact@studionovalem.fr. Ce site n'utilise pas de cookies de suivi ni de mesure d'audience tierce.</p>
<h2>Propriété intellectuelle</h2>
<p>Le contenu de ce site (textes, illustrations, mascotte, code) est la propriété de Studio Novalem. Les sites présentés dans la rubrique réalisations appartiennent à leurs propriétaires respectifs.</p>
<h2>Crédits</h2>
<p>Site conçu et codé par Studio Novalem, en Guadeloupe, sans WordPress ni constructeur en ligne, comme les sites livrés à ses clients.</p>
""",
))
