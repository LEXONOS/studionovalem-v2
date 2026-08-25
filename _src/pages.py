# -*- coding: utf-8 -*-
# Contenu des pages. Les fonctions img/gal/guichet et les icônes sont injectées par build.py.

PAGES = []

# ============================================================ ACCUEIL
INDEX = f'''
<section class="hero">
  <div class="hero-media">{img("hero-piscine.jpg", "La piscine et les gîtes Tropical Dream sous le soleil de Baie-Mahault", loading="eager")}</div>
  <div class="container hero-grid">
    <div>
      <p class="eyebrow">Baie-Mahault · au centre de la Guadeloupe</p>
      <h1 class="hero-title">Un gîte, une voiture, <em>un jacuzzi.</em></h1>
      <p class="hero-sub">Tout ce qu'il faut pour un séjour simple en Guadeloupe, chez une famille qui vit ici et qui habite juste à côté. À 7 minutes de l'aéroport.</p>
      <div class="hero-actions">
        <a class="btn btn-white" href="gites.html">Voir les gîtes</a>
        <a class="btn btn-ghost" href="vehicules.html">Louer un véhicule</a>
      </div>
      <div class="hero-facts">
        <span>4,8 / 5 sur Google</span><span>Piscine · Wi-Fi 162 Mb/s</span><span>Parking privé</span><span>Véhicule livré à l'aéroport</span>
      </div>
    </div>
    <div class="hero-guichet">{guichet()}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <div><p class="eyebrow">Trois façons de profiter</p><h2>Dormir, rouler, <em>souffler.</em></h2></div>
      <p class="lead">Chaque service se réserve seul ou avec les autres. Les clients qui combinent gîte et véhicule ne s'occupent plus de rien à l'arrivée.</p>
    </div>
    <div class="univers">
      <a class="univers-card reveal" href="gites.html">
        {img("univers-gite.jpg", "Chambre lumineuse d'un gîte Tropical Dream")}
        <div class="univers-body"><p class="eyebrow">Gîtes</p><h3>Deux gîtes, une piscine</h3><p>Un gîte familial de 3 chambres et un studio pour deux, autour d'une piscine, d'une cuisine extérieure et d'un jardin où les enfants jouent.</p><span class="link">Découvrir les gîtes</span></div>
      </a>
      <a class="univers-card reveal" data-delay="1" href="vehicules.html">
        {img("univers-vehicule.jpg", "Véhicule de location Tropical Dream sur une route de Guadeloupe")}
        <div class="univers-body"><p class="eyebrow">Véhicules</p><h3>Votre voiture vous attend à l'aéroport</h3><p>Des véhicules récents, entretenus, remis en main propre à Pôle Caraïbes ou au gîte. Sans file d'attente ni navette.</p><span class="link">Voir les véhicules</span></div>
      </a>
      <a class="univers-card reveal" data-delay="2" href="bien-etre.html">
        {img("univers-spa.jpg", "Jacuzzi-spa privatif Tropical Dream au coucher du soleil")}
        <div class="univers-body"><p class="eyebrow">Bien-être</p><h3>Jacuzzi-spa privatif &amp; massages</h3><p>Une séance rien que pour vous, en couple ou entre amis, avec ou sans massage. Ouvert aussi à ceux qui ne dorment pas ici.</p><span class="link">Réserver une séance</span></div>
      </a>
    </div>
  </div>
</section>

<section class="section-tight section-sable">
  <div class="container">
    <div class="facts">
      <div class="fact reveal"><strong>7 min</strong><span>de l'aéroport Pôle Caraïbes</span></div>
      <div class="fact reveal" data-delay="1"><strong>2 min</strong><span>du centre commercial Destreland</span></div>
      <div class="fact reveal" data-delay="2"><strong>7 min</strong><span>du centre de Pointe-à-Pitre</span></div>
      <div class="fact reveal" data-delay="3"><strong>5 min</strong><span>de la zone de Jarry</span></div>
      <div class="fact reveal" data-delay="1"><strong>162 Mb/s</strong><span>de Wi-Fi, streaming et télétravail</span></div>
      <div class="fact reveal" data-delay="2"><strong>4,8 / 5</strong><span>sur 32 avis Google</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="split-media reveal">{img("hotes.jpg", "Astrid et Christophe, vos hôtes à Tropical Dream")}<span class="tag">Vos hôtes</span></div>
    <div class="reveal" data-delay="1">
      <p class="eyebrow">Une maison de famille, pas un hôtel</p>
      <h2>Astrid &amp; Christophe habitent <em>juste à côté.</em></h2>
      <p class="lead">Une famille multiculturelle qui aime son île et qui a créé Tropical Dream en 2020 pour la faire découvrir autrement.</p>
      <p>Ici, on vous accueille quelle que soit l'heure d'arrivée, on vous envoie nos bonnes adresses avant même que vous n'atterrissiez, et on est disponible sans être envahissant. Les enfants de passage jouent avec les nôtres, et on vous garde les bagages le jour du départ si votre vol est tard.</p>
      <p class="hotes-signature">À très vite,<small>Astrid &amp; Christophe</small></p>
      <p style="margin-top:1.4rem"><a class="btn btn-ghost" href="a-propos.html">Faire connaissance</a></p>
    </div>
  </div>
</section>

<section class="section section-lagon">
  <div class="container">
    <div class="section-head reveal">
      <div><p class="eyebrow">Les gîtes</p><h2>Deux hébergements, <em>une seule adresse.</em></h2></div>
      <a class="btn btn-ghost" href="gites.html">Tout voir sur les gîtes</a>
    </div>
    <div class="offres">
      <article class="offre reveal">
        <div class="offre-media">{img("gite-familial-salon.jpg", "Salon du gîte familial 3 chambres")}<span class="offre-badge">Jusqu'à 7 personnes</span></div>
        <div class="offre-body">
          <h3>Le gîte familial</h3>
          <div class="offre-meta"><span>3 chambres</span><span>2 salles de bain</span><span>4 adultes + 3 enfants</span></div>
          <p>Un vrai appartement climatisé avec salon, cuisine équipée, deux douches à l'italienne et une terrasse sur la piscine. Le linge et les serviettes sont fournis.</p>
          <div class="offre-actions"><a class="btn btn-primary btn-sm" href="reservation.html?resa=gite&gite=Gîte+familial+3+chambres">Demander les dates</a><a class="btn btn-ghost btn-sm" href="gites.html#familial">Détails</a></div>
        </div>
      </article>
      <article class="offre reveal" data-delay="1">
        <div class="offre-media">{img("studio-chambre.jpg", "Le studio Ti Punch, idéal pour un couple")}<span class="offre-badge">Couple ou pro en déplacement</span></div>
        <div class="offre-body">
          <h3>Le studio Ti Punch</h3>
          <div class="offre-meta"><span>2 personnes</span><span>Terrasse privée</span><span>Accès piscine</span></div>
          <p>Le format juste pour deux amoureux, ou pour un professionnel en mission à Jarry qui veut un vrai lit, du calme et une bonne connexion.</p>
          <div class="offre-actions"><a class="btn btn-primary btn-sm" href="reservation.html?resa=gite&gite=Studio+Ti+Punch+(couple)">Demander les dates</a><a class="btn btn-ghost btn-sm" href="gites.html#studio">Détails</a></div>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split reverse">
    <div class="split-media landscape reveal">{img("aeroport.jpg", "Remise des clés du véhicule à l'aéroport Guadeloupe Pôle Caraïbes")}<span class="tag">Remise à l'aéroport</span></div>
    <div class="reveal" data-delay="1">
      <p class="eyebrow">Location de véhicules</p>
      <h2>Vous sortez de l'avion, <em>les clés sont là.</em></h2>
      <p class="lead">Après plusieurs heures de vol, la dernière chose qu'on veut, c'est une navette et une file d'attente. Christophe vous attend avec le véhicule.</p>
      <ul class="checklist">
        <li>Véhicules récents et révisés régulièrement</li>
        <li>Remise et restitution à Pôle Caraïbes ou au gîte</li>
        <li>Tarifs clairs, adaptés à la durée</li>
        <li>Nos bonnes adresses envoyées dès l'arrivée</li>
      </ul>
      <p style="margin-top:1.6rem"><a class="btn btn-primary" href="vehicules.html">Voir les véhicules et les conditions</a></p>
    </div>
  </div>
</section>

<section class="section on-dark">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">Jacuzzi-spa &amp; bien-être</p>
      <h2>Une heure rien que <em>pour vous.</em></h2>
      <p class="lead">Le jacuzzi-spa se privatise à la séance. On y vient à deux pour une soirée, entre amies pour un moment, ou en fin de journée après avoir couru l'île.</p>
      <p>Chaque séance est préparée avant votre arrivée. Vous pouvez y ajouter un massage détente ou composer une formule couple. Les séances sont ouvertes à tous, que vous dormiez à Tropical Dream ou non.</p>
      <div class="hero-actions"><a class="btn btn-white" href="bien-etre.html">Découvrir les formules</a><a class="btn btn-ghost" href="#" data-open-resa="bienetre">Réserver une séance</a></div>
    </div>
    <div class="split-media reveal" data-delay="1">{img("jacuzzi-2.jpg", "Le jacuzzi-spa privatif Tropical Dream de nuit")}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <div><p class="eyebrow">Ils sont passés par Baie-Mahault</p><h2>Ce que disent <em>nos voyageurs.</em></h2></div>
      <div class="avis-badges">
        <span class="badge"><strong>4,8</strong><span><span class="stars">★★★★★</span><br>32 avis Google</span></span>
        <span class="badge"><strong>8,4</strong><span>Note Booking.com<br>« Très bien »</span></span>
      </div>
    </div>
    <div class="avis-grid">
      <article class="avis reveal"><q>Les hôtes sont adorables et aux petits soins. Nous avions loué les deux gîtes pour être tranquilles, les enfants ont profité des jeux du jardin et se sont fait des copains.</q><div class="avis-auteur"><span class="stars">★★★★★</span>Séjour en famille · Booking</div></article>
      <article class="avis reveal" data-delay="1"><q>La voiture était quasiment neuve, bien équipée et à un prix très raisonnable. Christophe est ponctuel, professionnel et rassurant.</q><div class="avis-auteur"><span class="stars">★★★★★</span>Location de véhicule · Google</div></article>
      <article class="avis reveal" data-delay="2"><q>Récupérer et rendre la voiture directement à l'aéroport nous a évité bien des tracas après des heures de vol. En bonus, une liste de bonnes adresses envoyée dès l'arrivée.</q><div class="avis-auteur"><span class="stars">★★★★★</span>Location 15 jours · Google</div></article>
    </div>
  </div>
</section>

<section class="section section-sable">
  <div class="container map-wrap">
    <div class="reveal">
      <p class="eyebrow">Où sommes-nous</p>
      <h2>Au centre, pour <em>tout rayonner.</em></h2>
      <p class="muted">Baie-Mahault est la commune charnière entre Grande-Terre et Basse-Terre. Plages, rivières, cascades et parc national sont tous accessibles dans la journée, et vous rentrez sans embouteillage.</p>
      <ul class="distances">
        <li><span>Aéroport Guadeloupe Pôle Caraïbes</span><span>7 km · 7 min</span></li>
        <li><span>Centre commercial Destreland</span><span>2 min</span></li>
        <li><span>Pointe-à-Pitre, centre-ville</span><span>7 min</span></li>
        <li><span>Zone d'activités de Jarry</span><span>5 min</span></li>
        <li><span>Plages du Gosier et de Sainte-Anne</span><span>20 à 35 min</span></li>
        <li><span>Cascades et rivières de Basse-Terre</span><span>30 à 45 min</span></li>
      </ul>
    </div>
    <div class="map-frame reveal" data-delay="1">
      <iframe title="Carte : Tropical Dream, 6 impasse de la Concorde, Baie-Mahault" src="https://www.google.com/maps?q=16.2548547,-61.5855826&z=15&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta-band reveal">
      <p class="eyebrow">Réservation</p>
      <h2>Dites-nous vos dates, on s'occupe <em>du reste.</em></h2>
      <p class="lead">Un message suffit. Astrid ou Christophe vous répond avec la disponibilité et le tarif, puis vous confirmez.</p>
      <div class="btn-row">
        <a class="btn btn-primary btn-lg" href="#" data-open-resa="gite">Réserver un gîte</a>
        <a class="btn btn-white btn-lg" href="#" data-open-resa="vehicule">Louer un véhicule</a>
        <a class="btn btn-ghost btn-lg" href="https://wa.me/590690702529" target="_blank" rel="noopener">{ICON_WA} Écrire sur WhatsApp</a>
      </div>
    </div>
  </div>
</section>
'''
PAGES.append(({"file": "index.html", "title": "Tropical Dream — Gîtes, location de véhicules & jacuzzi-spa à Baie-Mahault, Guadeloupe", "desc": "Deux gîtes avec piscine à 7 min de l'aéroport, véhicules récents livrés à Pôle Caraïbes et jacuzzi-spa privatif. Une adresse familiale au centre de la Guadeloupe. Réservation simple par WhatsApp."}, INDEX))

# ============================================================ GÎTES
GITES = f'''
<section class="hero hero-inner">
  <div class="hero-media">{img("piscine-2.jpg", "La piscine de Tropical Dream entourée de végétation", loading="eager")}</div>
  <div class="container">
    <p class="eyebrow">Les gîtes</p>
    <h1 class="hero-title">Deux gîtes autour d'une piscine, <em>au calme.</em></h1>
    <p class="hero-sub">Un gîte familial de 3 chambres, un studio pour deux. Climatisés, équipés comme à la maison, avec une cuisine extérieure que tout le monde finit par préférer.</p>
    <div class="hero-actions"><a class="btn btn-primary" href="#" data-open-resa="gite">Demander les dates</a><a class="btn btn-ghost" href="#espaces">Voir les espaces communs</a></div>
  </div>
</section>

<section class="section" id="familial">
  <div class="container split">
    <div class="split-media reveal">{img("gite-familial-chambre.jpg", "Chambre du gîte familial Tropical Dream")}<span class="tag">Gîte familial</span></div>
    <div class="reveal" data-delay="1">
      <p class="eyebrow">Jusqu'à 4 adultes et 3 enfants</p>
      <h2>Le gîte familial <em>3 chambres</em></h2>
      <p class="lead">Un appartement entier, pas une chambre. Chacun a sa pièce, la cuisine permet de cuisiner vraiment, et la terrasse donne sur la piscine.</p>
      <ul class="checklist">
        <li>3 chambres climatisées</li>
        <li>2 salles de bain, douches à l'italienne</li>
        <li>Salon avec TV écran plat</li>
        <li>Cuisine équipée : four, lave-vaisselle, café et thé</li>
        <li>Terrasse privée avec vue piscine</li>
        <li>Linge de lit et serviettes fournis</li>
        <li>Wi-Fi 162 Mb/s</li>
        <li>Parking privé gratuit, sans réservation</li>
      </ul>
      <div class="hero-actions"><a class="btn btn-primary" href="reservation.html?resa=gite&gite=Gîte+familial+3+chambres">Réserver le gîte familial</a></div>
    </div>
  </div>
</section>

<section class="section section-sable" id="studio">
  <div class="container split reverse">
    <div class="split-media reveal">{img("studio-terrasse.jpg", "Terrasse privée du studio Ti Punch")}<span class="tag">Studio Ti Punch</span></div>
    <div class="reveal" data-delay="1">
      <p class="eyebrow">Pour deux</p>
      <h2>Le studio <em>Ti Punch</em></h2>
      <p class="lead">Idéal pour un couple, ou pour un professionnel en déplacement à Jarry qui préfère une adresse calme à un hôtel de zone.</p>
      <ul class="checklist">
        <li>Lit confortable, climatisation</li>
        <li>Coin cuisine : réfrigérateur, micro-ondes, vaisselle</li>
        <li>Salle d'eau privée</li>
        <li>Terrasse privée</li>
        <li>Accès à la piscine et au jardin</li>
        <li>Bureau et Wi-Fi rapide pour travailler</li>
        <li>Linge fourni</li>
        <li>Parking privé gratuit</li>
      </ul>
      <div class="hero-actions"><a class="btn btn-primary" href="reservation.html?resa=gite&gite=Studio+Ti+Punch+(couple)">Réserver le studio</a></div>
    </div>
  </div>
</section>

<section class="section" id="espaces">
  <div class="container">
    <div class="section-head reveal">
      <div><p class="eyebrow">Les espaces communs</p><h2>Ce que vous partagez, <em>et que vous allez adorer.</em></h2></div>
      <p class="lead">La piscine, le jardin et la cuisine extérieure sont partagés avec la famille et, selon les dates, avec l'autre gîte. C'est ce qui fait l'ambiance du lieu.</p>
    </div>
    <div class="gallery reveal">
      {gal("piscine-2.jpg", "La piscine", "wide tall")}
      {gal("cuisine-exterieure.jpg", "La cuisine extérieure")}
      {gal("jeux-enfants.jpg", "Les jeux pour enfants")}
      {gal("barbecue.jpg", "Le barbecue")}
      {gal("jardin.jpg", "Le jardin")}
      {gal("piscine-enfants.jpg", "La piscine enfants", "wide")}
      {gal("gite-familial-cuisine.jpg", "Cuisine équipée du gîte familial")}
      {gal("gite-familial-sdb.jpg", "Salle de bain, douche à l'italienne")}
    </div>
  </div>
</section>

<section class="section section-lagon">
  <div class="container">
    <div class="section-head reveal"><div><p class="eyebrow">Inclus dans votre séjour</p><h2>Tout ce qu'on trouve <em>chez soi.</em></h2></div></div>
    <div class="offres">
      <article class="offre reveal"><div class="offre-body"><h3>Pour se détendre</h3><ul class="offre-list"><li>Piscine et piscine enfants</li><li>Transats, jardin tropical</li><li>Tennis de table, fléchettes</li><li>Jeux intérieurs et extérieurs pour les enfants</li><li>Jacuzzi-spa privatif sur réservation</li></ul></div></article>
      <article class="offre reveal" data-delay="1"><div class="offre-body"><h3>Pour cuisiner</h3><ul class="offre-list"><li>Cuisine extérieure et coin repas dehors</li><li>Barbecue</li><li>Cuisines équipées dans chaque gîte</li><li>Café et thé à disposition</li><li>Supermarché à 5 minutes à pied</li></ul></div></article>
      <article class="offre reveal" data-delay="2"><div class="offre-body"><h3>Pour être tranquille</h3><ul class="offre-list"><li>Accueil quelle que soit l'heure d'arrivée</li><li>Navette aéroport et location de véhicule</li><li>Bagagerie le jour du départ</li><li>Wi-Fi 162 Mb/s dans tous les espaces</li><li>Établissement sécurisé, parking privé</li></ul></div></article>
    </div>
  </div>
</section>

<section class="section">
  <div class="container narrow">
    <div class="section-head reveal"><div><p class="eyebrow">Bon à savoir</p><h2>Questions <em>fréquentes</em></h2></div></div>
    <div class="faq reveal">
      <details><summary>Peut-on arriver tard le soir ?</summary><p>Oui. Prévenez-nous simplement de votre heure d'arrivée : nous habitons à côté et nous vous accueillons quelle que soit l'heure.</p></details>
      <details><summary>La piscine est-elle privée ?</summary><p>La piscine, le jardin et la cuisine extérieure sont partagés avec la famille et avec l'autre gîte s'il est occupé. Si vous voulez le lieu pour vous, réservez les deux gîtes : c'est ce que font souvent les familles et les groupes d'amis.</p></details>
      <details><summary>Peut-on recevoir des visiteurs au gîte ?</summary><p>L'accueil de personnes extérieures à la réservation n'est pas autorisé, pour la tranquillité et la sécurité de tous. Pour un événement, parlez-nous-en : <a href="evenements.html">on organise</a>.</p></details>
      <details><summary>Faut-il une voiture ?</summary><p>Un supermarché est à 5 minutes à pied et les transports en commun passent à proximité, mais pour découvrir l'île une voiture est presque indispensable. Nous en louons, remises à l'aéroport ou au gîte : <a href="vehicules.html">voir les véhicules</a>.</p></details>
      <details><summary>Comment se passe la réservation ?</summary><p>Vous nous envoyez vos dates par WhatsApp, e-mail ou via le formulaire. Nous confirmons la disponibilité et le tarif, vous validez, et vous recevez toutes les informations pratiques avant l'arrivée. Vous pouvez aussi réserver sur Booking.com.</p></details>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="cta-band reveal">
      <h2>Vos dates, <em>votre gîte.</em></h2>
      <p class="lead">Indiquez vos dates et le nombre de voyageurs, on vous répond vite.</p>
      <div class="btn-row"><a class="btn btn-primary btn-lg" href="#" data-open-resa="gite">Demander les dates</a><a class="btn btn-ghost btn-lg" href="https://wa.me/590690702529" target="_blank" rel="noopener">{ICON_WA} WhatsApp</a></div>
    </div>
  </div>
</section>
'''
PAGES.append(({"file": "gites.html", "title": "Gîtes avec piscine à Baie-Mahault — Gîte familial 3 chambres & studio couple | Tropical Dream", "desc": "Gîte familial 3 chambres (4 adultes + 3 enfants) et studio Ti Punch pour deux, climatisés, avec piscine, cuisine extérieure, jeux enfants et Wi-Fi 162 Mb/s. À 7 min de l'aéroport de Guadeloupe."}, GITES))

# ============================================================ VÉHICULES
VEHICULES = f'''
<section class="hero hero-inner">
  <div class="hero-media">{img("univers-vehicule.jpg", "Véhicule de location Tropical Dream", loading="eager")}</div>
  <div class="container">
    <p class="eyebrow">Location de véhicules</p>
    <h1 class="hero-title">Votre véhicule, remis en main propre <em>à l'aéroport.</em></h1>
    <p class="hero-sub">Des voitures récentes et révisées, un interlocuteur unique, et zéro navette à la sortie de l'avion. C'est ce que nos clients retiennent en premier.</p>
    <div class="hero-actions"><a class="btn btn-primary" href="#" data-open-resa="vehicule">Demander un tarif</a><a class="btn btn-ghost" href="#conditions">Voir les conditions</a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><div><p class="eyebrow">Comment ça se passe</p><h2>Quatre étapes, <em>aucune surprise.</em></h2></div></div>
    <div class="steps">
      <div class="step reveal"><h3>Vous demandez</h3><p>Dates, catégorie souhaitée, lieu de remise. Par WhatsApp, e-mail ou formulaire. Christophe vous confirme la disponibilité et le tarif.</p></div>
      <div class="step reveal" data-delay="1"><h3>On vous attend</h3><p>À l'aéroport Pôle Caraïbes avec votre numéro de vol, ou au gîte à Baie-Mahault. Tour du véhicule ensemble, état des lieux, et les clés sont à vous.</p></div>
      <div class="step reveal" data-delay="2"><h3>Vous roulez</h3><p>Vous recevez nos bonnes adresses : plages, restaurants, balades. En cas de question pendant le séjour, un message suffit.</p></div>
      <div class="step reveal" data-delay="3"><h3>Vous rendez</h3><p>Restitution au même endroit, à l'heure convenue, y compris tôt le matin ou tard le soir pour un vol. État des lieux de retour et c'est fini.</p></div>
    </div>
  </div>
</section>

<section class="section section-sable">
  <div class="container">
    <div class="section-head reveal">
      <div><p class="eyebrow">La flotte</p><h2>Le bon format <em>pour votre séjour.</em></h2></div>
      <p class="lead">Dites-nous combien vous êtes et où vous comptez aller, on vous conseille la catégorie la plus adaptée.</p>
    </div>
    <div class="offres">
      <article class="offre reveal">
        <div class="offre-media">{img("vehicule-citadine.jpg", "Citadine de location Tropical Dream")}<span class="offre-badge">Économique</span></div>
        <div class="offre-body"><h3>Citadine</h3><div class="offre-meta"><span>2 à 4 personnes</span><span>Climatisée</span></div><p>Maniable en ville, sobre sur la route. Parfaite pour un couple ou un déplacement pro entre Jarry, Pointe-à-Pitre et les plages.</p><div class="offre-actions"><a class="btn btn-primary btn-sm" href="reservation.html?resa=vehicule">Demander un tarif</a></div></div>
      </article>
      <article class="offre reveal" data-delay="1">
        <div class="offre-media">{img("vehicule-compacte.jpg", "Compacte de location Tropical Dream")}<span class="offre-badge">Polyvalente</span></div>
        <div class="offre-body"><h3>Compacte / berline</h3><div class="offre-meta"><span>4 à 5 personnes</span><span>Grand coffre</span></div><p>Le compromis confort et budget pour deux semaines de découverte, valises comprises, de Deshaies à la Pointe des Châteaux.</p><div class="offre-actions"><a class="btn btn-primary btn-sm" href="reservation.html?resa=vehicule">Demander un tarif</a></div></div>
      </article>
      <article class="offre reveal" data-delay="2">
        <div class="offre-media">{img("vehicule-suv.jpg", "SUV de location Tropical Dream")}<span class="offre-badge">Familial</span></div>
        <div class="offre-body"><h3>SUV / familial</h3><div class="offre-meta"><span>5 à 7 personnes</span><span>Position haute</span></div><p>Pour les familles, les groupes et les routes de Basse-Terre. De l'espace pour tout le monde et pour les glacières.</p><div class="offre-actions"><a class="btn btn-primary btn-sm" href="reservation.html?resa=vehicule">Demander un tarif</a></div></div>
      </article>
    </div>
  </div>
</section>

<section class="section" id="conditions">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">Conditions</p>
      <h2>Simple et <em>transparent.</em></h2>
      <p class="lead">Les tarifs dépendent de la catégorie et de la durée : plus le séjour est long, plus la journée est douce. Le prix annoncé est celui que vous payez.</p>
      <ul class="checklist">
        <li>Permis de conduire en cours de validité</li>
        <li>Pièce d'identité</li>
        <li>Caution restituée au retour du véhicule</li>
        <li>Véhicule remis propre, avec le carburant convenu</li>
        <li>Assurance incluse, détails précisés sur le contrat</li>
        <li>Siège enfant sur demande</li>
        <li>Remise à l'aéroport, au gîte ou à une autre adresse</li>
        <li>Conducteur additionnel possible</li>
      </ul>
      <p class="muted" style="margin-top:1.2rem;font-size:.92rem">Les conditions détaillées (âge minimum, franchise, kilométrage) figurent sur le contrat de location remis à la prise du véhicule.</p>
    </div>
    <div class="split-media reveal" data-delay="1">{img("aeroport.jpg", "Remise du véhicule à l'aéroport")}<span class="tag">Pôle Caraïbes</span></div>
  </div>
</section>

<section class="section on-dark">
  <div class="container">
    <div class="section-head reveal">
      <div><p class="eyebrow">Ils ont loué chez nous</p><h2>Sans navette, <em>sans stress.</em></h2></div>
      <span class="badge"><strong>4,8</strong><span><span class="stars">★★★★★</span><br>32 avis Google</span></span>
    </div>
    <div class="avis-grid">
      <article class="avis reveal"><q>Ne cherchez plus, Tropical Dream est LA solution pour louer une voiture. Plusieurs week-ends de location, des véhicules en excellent état et Christophe d'une gentillesse incroyable.</q><div class="avis-auteur"><span class="stars">★★★★★</span>Maud C., Clermont-Ferrand</div></article>
      <article class="avis reveal" data-delay="1"><q>Deux voitures louées pendant deux semaines. Christophe est une personne de confiance, aucun souci avec les véhicules. Je referais appel à lui sans hésiter.</q><div class="avis-auteur"><span class="stars">★★★★★</span>Didier</div></article>
      <article class="avis reveal" data-delay="2"><q>Location de 15 jours : tout s'est parfaitement passé. La remise à l'aéroport a été un vrai plus, et ils ont été très arrangeants.</q><div class="avis-auteur"><span class="stars">★★★★★</span>Avis Google</div></article>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split reverse">
    <div class="split-media landscape reveal">{img("hero-piscine.jpg", "Les gîtes et la piscine Tropical Dream")}<span class="tag">Gîte + véhicule</span></div>
    <div class="reveal" data-delay="1">
      <p class="eyebrow">L'astuce</p>
      <h2>Combinez le gîte <em>et la voiture.</em></h2>
      <p class="lead">Vous atterrissez, vous récupérez les clés, vous roulez 7 minutes, vous êtes chez vous. Le véhicule dort sur le parking privé du gîte et vous le rendez à l'aéroport le jour du départ.</p>
      <div class="hero-actions"><a class="btn btn-primary" href="reservation.html?resa=gite">Réserver gîte + véhicule</a><a class="btn btn-ghost" href="gites.html">Voir les gîtes</a></div>
    </div>
  </div>
</section>
'''
PAGES.append(({"file": "vehicules.html", "title": "Location de voiture en Guadeloupe avec remise à l'aéroport — Tropical Dream, Baie-Mahault", "desc": "Location de véhicules récents en Guadeloupe : citadine, compacte, SUV. Remise et restitution à l'aéroport Pôle Caraïbes ou au gîte. Interlocuteur unique, tarifs clairs, 4,8/5 sur Google."}, VEHICULES))

# ============================================================ BIEN-ÊTRE
BIENETRE = f'''
<section class="hero hero-inner">
  <div class="hero-media">{img("jacuzzi-1.jpg", "Jacuzzi-spa privatif Tropical Dream", loading="eager")}</div>
  <div class="container">
    <p class="eyebrow">Jacuzzi-spa &amp; bien-être</p>
    <h1 class="hero-title">Un jacuzzi-spa privatisé, <em>rien que pour vous.</em></h1>
    <p class="hero-sub">À la séance, en couple ou entre amis, avec ou sans massage. Ouvert à tous, que vous logiez chez nous ou non.</p>
    <div class="hero-actions"><a class="btn btn-primary" href="#" data-open-resa="bienetre">Réserver une séance</a><a class="btn btn-ghost" href="#formules">Voir les formules</a></div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="split-media reveal">{img("jacuzzi-2.jpg", "Le jacuzzi-spa de nuit, ambiance tamisée")}<span class="tag">Séance privative</span></div>
    <div class="reveal" data-delay="1">
      <p class="eyebrow">Le principe</p>
      <h2>Le spa est à vous <em>le temps de la séance.</em></h2>
      <p class="lead">Pas de créneau partagé, pas de voisins de bassin. Le jacuzzi haut de gamme est préparé avant votre arrivée et vous en avez l'usage exclusif.</p>
      <ul class="checklist">
        <li>Jacuzzi-spa haut de gamme, usage exclusif</li>
        <li>Espace préparé et nettoyé avant chaque séance</li>
        <li>Serviettes fournies</li>
        <li>Ambiance tamisée en soirée</li>
        <li>Boissons et petite attention sur demande</li>
        <li>Massage détente en option</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-sable" id="formules">
  <div class="container">
    <div class="section-head reveal">
      <div><p class="eyebrow">Les formules</p><h2>Choisissez votre <em>moment.</em></h2></div>
      <p class="lead">Les tarifs sont communiqués à la demande selon la formule, le nombre de personnes et le créneau. On vous répond dans la journée.</p>
    </div>
    <div class="offres">
      <article class="offre reveal">
        <div class="offre-media">{img("jacuzzi-1.jpg", "Séance jacuzzi-spa privatif")}<span class="offre-badge">Le classique</span></div>
        <div class="offre-body"><h3>Séance jacuzzi-spa</h3><div class="offre-meta"><span>1 à 4 personnes</span><span>Privatif</span></div><p>Le jacuzzi pour vous, le temps d'une séance. Idéal après une journée de randonnée ou de plage.</p><div class="offre-actions"><a class="btn btn-primary btn-sm" href="reservation.html?resa=bienetre">Réserver</a></div></div>
      </article>
      <article class="offre reveal" data-delay="1">
        <div class="offre-media">{img("massage.jpg", "Massage détente")}<span class="offre-badge">Le complet</span></div>
        <div class="offre-body"><h3>Jacuzzi-spa + massage</h3><div class="offre-meta"><span>1 à 2 personnes</span><span>Détente</span></div><p>La séance de spa suivie d'un massage détente. Le combo pour relâcher vraiment.</p><div class="offre-actions"><a class="btn btn-primary btn-sm" href="reservation.html?resa=bienetre">Réserver</a></div></div>
      </article>
      <article class="offre reveal" data-delay="2">
        <div class="offre-media">{img("jacuzzi-2.jpg", "Formule couple en soirée")}<span class="offre-badge">À deux</span></div>
        <div class="offre-body"><h3>Formule couple</h3><div class="offre-meta"><span>2 personnes</span><span>Soirée</span></div><p>Une soirée en tête-à-tête : spa privatisé, ambiance tamisée, petite attention. Anniversaire, Saint-Valentin, ou sans raison.</p><div class="offre-actions"><a class="btn btn-primary btn-sm" href="reservation.html?resa=bienetre">Réserver</a></div></div>
      </article>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><div><p class="eyebrow">Comment ça se passe</p><h2>Réserver une séance, <em>en trois messages.</em></h2></div></div>
    <div class="steps">
      <div class="step reveal"><h3>Vous choisissez</h3><p>La formule, la date et le créneau qui vous vont. Matin, après-midi ou soirée.</p></div>
      <div class="step reveal" data-delay="1"><h3>On confirme</h3><p>Disponibilité et tarif par retour de message. La séance est bloquée pour vous.</p></div>
      <div class="step reveal" data-delay="2"><h3>Vous profitez</h3><p>Vous arrivez, tout est prêt. Il ne reste qu'à se laisser porter.</p></div>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="cta-band reveal">
      <p class="eyebrow">Idée cadeau</p>
      <h2>Offrez une séance à quelqu'un <em>qui le mérite.</em></h2>
      <p class="lead">Fête des mères, anniversaire, remerciement : une séance de jacuzzi-spa s'offre facilement. Écrivez-nous, on prépare le bon cadeau avec vous.</p>
      <div class="btn-row"><a class="btn btn-primary btn-lg" href="#" data-open-resa="bienetre">Réserver une séance</a><a class="btn btn-ghost btn-lg" href="https://wa.me/590690702529?text=Bonjour%2C%20je%20voudrais%20offrir%20une%20s%C3%A9ance%20jacuzzi-spa." target="_blank" rel="noopener">{ICON_WA} Offrir une séance</a></div>
    </div>
  </div>
</section>
'''
PAGES.append(({"file": "bien-etre.html", "title": "Jacuzzi-spa privatif & massages à Baie-Mahault, Guadeloupe — Tropical Dream", "desc": "Séance de jacuzzi-spa privatisé, massage détente et formule couple en soirée, à Baie-Mahault. Ouvert à tous, sur réservation. Idée cadeau."}, BIENETRE))

# ============================================================ ÉVÉNEMENTS
EVENEMENTS = f'''
<section class="hero hero-inner">
  <div class="hero-media">{img("evenement-1.jpg", "Table dressée pour un événement à Tropical Dream", loading="eager")}</div>
  <div class="container">
    <p class="eyebrow">Événementiel</p>
    <h1 class="hero-title">Un anniversaire, une fête, <em>un lieu à vous.</em></h1>
    <p class="hero-sub">Le jardin, la piscine, la cuisine extérieure et le jacuzzi peuvent accueillir votre événement en petit comité, avec hébergement sur place.</p>
    <div class="hero-actions"><a class="btn btn-primary" href="reservation.html?resa=evenement">Décrire mon événement</a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <div><p class="eyebrow">Ce qu'on organise</p><h2>Des moments <em>à taille humaine.</em></h2></div>
      <p class="lead">Pas de salle des fêtes impersonnelle : une maison, un jardin, et une famille qui vous aide à tout préparer.</p>
    </div>
    <div class="offres">
      <article class="offre reveal"><div class="offre-media">{img("evenement-2.jpg", "Anniversaire au gîte")}</div><div class="offre-body"><h3>Anniversaires</h3><p>Enfants ou adultes, autour de la piscine et du barbecue. Décoration, gâteau et musique : dites-nous ce que vous voulez, on coordonne.</p></div></article>
      <article class="offre reveal" data-delay="1"><div class="offre-media">{img("jacuzzi-2.jpg", "Soirée entre amies au spa")}</div><div class="offre-body"><h3>EVJF, soirées entre amis</h3><p>Le jacuzzi-spa privatisé, le jardin en soirée et le studio ou le gîte pour dormir sur place. Personne ne reprend la route.</p></div></article>
      <article class="offre reveal" data-delay="2"><div class="offre-media">{img("cuisine-exterieure.jpg", "Repas de famille dehors")}</div><div class="offre-body"><h3>Réunions de famille</h3><p>Louez les deux gîtes pour être entre vous. La cuisine extérieure et le coin repas dehors deviennent le cœur du week-end.</p></div></article>
      <article class="offre reveal" data-delay="3"><div class="offre-media">{img("gite-familial-salon.jpg", "Séminaire en petit comité")}</div><div class="offre-body"><h3>Séminaires en petit comité</h3><p>À 5 minutes de Jarry : une journée de travail au calme, Wi-Fi 162 Mb/s, pause piscine, et hébergement pour l'équipe.</p></div></article>
    </div>
  </div>
</section>

<section class="section section-sable">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">Ce que vous avez sur place</p>
      <h2>Tout est déjà <em>là.</em></h2>
      <ul class="checklist">
        <li>Jardin tropical et coin repas extérieur</li>
        <li>Cuisine extérieure et barbecue</li>
        <li>Piscine et piscine enfants</li>
        <li>Jacuzzi-spa privatisable</li>
        <li>Jeux pour enfants</li>
        <li>Hébergement sur place (jusqu'à 9 personnes avec les deux gîtes)</li>
        <li>Parking privé</li>
        <li>Musique et éclairage d'ambiance en soirée</li>
      </ul>
      <p class="muted" style="margin-top:1rem;font-size:.92rem">Chaque événement est étudié au cas par cas : nombre d'invités, horaires, besoins. On vous fait une proposition claire avant tout engagement.</p>
    </div>
    <div class="split-media reveal" data-delay="1">{img("barbecue.jpg", "Barbecue en soirée au gîte")}</div>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="cta-band reveal">
      <h2>Racontez-nous <em>votre projet.</em></h2>
      <p class="lead">Type d'événement, date, nombre d'invités : on revient vers vous avec une proposition.</p>
      <div class="btn-row"><a class="btn btn-primary btn-lg" href="reservation.html?resa=evenement">Décrire mon événement</a><a class="btn btn-ghost btn-lg" href="https://wa.me/590690702529" target="_blank" rel="noopener">{ICON_WA} WhatsApp</a></div>
    </div>
  </div>
</section>
'''
PAGES.append(({"file": "evenements.html", "title": "Anniversaires, EVJF et événements en petit comité à Baie-Mahault — Tropical Dream", "desc": "Organisez un anniversaire, un EVJF, une réunion de famille ou un séminaire en petit comité dans un lieu privé avec piscine, jacuzzi-spa, cuisine extérieure et hébergement sur place."}, EVENEMENTS))

# ============================================================ À PROPOS
APROPOS = f'''
<section class="hero hero-inner">
  <div class="hero-media">{img("guadeloupe-plage.jpg", "Plage de Guadeloupe", loading="eager")}</div>
  <div class="container">
    <p class="eyebrow">À propos</p>
    <h1 class="hero-title">Une famille qui aime son île <em>et qui la partage.</em></h1>
    <p class="hero-sub">Tropical Dream, c'est Astrid, Christophe, leurs enfants, et une maison à Baie-Mahault ouverte aux voyageurs depuis 2020.</p>
  </div>
</section>

<section class="section">
  <div class="container hotes">
    <div class="split-media reveal">{img("hotes.jpg", "Astrid et Christophe")}</div>
    <div class="reveal" data-delay="1">
      <p class="eyebrow">L'histoire</p>
      <h2>Tout est parti <em>d'un gîte.</em></h2>
      <p class="lead">Nous sommes une famille multiculturelle installée à Baie-Mahault. En 2020, nous avons ouvert un premier gîte à côté de chez nous pour accueillir des voyageurs comme on aimerait l'être.</p>
      <p>Très vite, les mêmes demandes sont revenues : « vous connaissez quelqu'un pour une voiture ? », « on peut fêter un anniversaire ici ? », « il y a un spa dans le coin ? ». On a répondu à chacune. Aujourd'hui, Tropical Dream, c'est deux gîtes, une flotte de véhicules qu'on remet nous-mêmes à l'aéroport, un jacuzzi-spa qu'on privatise, et des événements qu'on organise dans le jardin.</p>
      <p>Ce qui n'a pas changé : on habite juste à côté, on répond vite, et on vous envoie nos bonnes adresses avant même votre arrivée.</p>
      <p class="hotes-signature">Astrid &amp; Christophe<small>Tropical Dream, Baie-Mahault</small></p>
    </div>
  </div>
</section>

<section class="section section-sable">
  <div class="container">
    <div class="section-head reveal"><div><p class="eyebrow">Notre façon de faire</p><h2>Trois choses <em>qu'on tient.</em></h2></div></div>
    <div class="offres">
      <article class="offre reveal"><div class="offre-body"><h3>Disponibles, pas envahissants</h3><p>On vous accueille à toute heure, on est là si besoin, et on vous laisse vivre votre séjour. Les avis parlent d'hôtes « aux petits soins » et « juste comme il faut ».</p></div></article>
      <article class="offre reveal" data-delay="1"><div class="offre-body"><h3>Des prix clairs</h3><p>Le tarif annoncé est celui que vous payez. Pour les véhicules, il s'adapte à la durée ; pour les gîtes et le spa, il est confirmé avant toute réservation.</p></div></article>
      <article class="offre reveal" data-delay="2"><div class="offre-body"><h3>La Guadeloupe de l'intérieur</h3><p>Plages sans sargasses, restaurants où on va vraiment, cascades accessibles avec des enfants : on partage ce qu'on connaît, pas une brochure.</p></div></article>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split reverse">
    <div class="split-media reveal">{img("guadeloupe-nature.jpg", "Rivière et forêt de Basse-Terre")}<span class="tag">Basse-Terre à 30 min</span></div>
    <div class="reveal" data-delay="1">
      <p class="eyebrow">Depuis Baie-Mahault</p>
      <h2>Tout est <em>à portée.</em></h2>
      <p class="lead">Baie-Mahault est au centre : la Grande-Terre et ses plages d'un côté, la Basse-Terre et sa forêt de l'autre. On rayonne partout et on rentre sans embouteillage.</p>
      <ul class="distances">
        <li><span>Plages du Gosier, Sainte-Anne, Saint-François</span><span>20 à 45 min</span></li>
        <li><span>Cascade aux Écrevisses, parc national</span><span>35 min</span></li>
        <li><span>Deshaies, plage de Grande-Anse</span><span>45 min</span></li>
        <li><span>Réserve Cousteau, Malendure</span><span>50 min</span></li>
        <li><span>Embarcadère pour Les Saintes, Marie-Galante</span><span>30 min à 1 h</span></li>
        <li><span>Aéroport Pôle Caraïbes</span><span>7 min</span></li>
      </ul>
    </div>
  </div>
</section>

<section class="section on-dark">
  <div class="container">
    <div class="section-head reveal">
      <div><p class="eyebrow">Ce qu'on retient</p><h2>Les mots <em>qui reviennent.</em></h2></div>
      <div class="avis-badges"><span class="badge"><strong>4,8</strong><span><span class="stars">★★★★★</span><br>32 avis Google</span></span><span class="badge"><strong>8,4</strong><span>Booking.com</span></span></div>
    </div>
    <div class="avis-grid">
      <article class="avis reveal"><q>Un accueil chaleureux, une grande piscine, de l'espace, des jeux pour les enfants. Un hébergement sécurisé et bien situé.</q><div class="avis-auteur"><span class="stars">★★★★★</span>Booking</div></article>
      <article class="avis reveal" data-delay="1"><q>Très bon accueil quelle que soit l'heure d'arrivée. Il y a tout ce qu'on trouve chez soi pour cuisiner. Très calme, très propre, idéalement placé.</q><div class="avis-auteur"><span class="stars">★★★★★</span>Booking</div></article>
      <article class="avis reveal" data-delay="2"><q>Christophe s'est mis en quatre pour nous aider, et a même gardé nos bagages le jour du départ. Les garçons étaient ravis de jouer avec ses enfants.</q><div class="avis-auteur"><span class="stars">★★★★★</span>Google</div></article>
    </div>
  </div>
</section>
'''
PAGES.append(({"file": "a-propos.html", "title": "Astrid & Christophe, vos hôtes à Baie-Mahault — Tropical Dream Guadeloupe", "desc": "Une famille de Baie-Mahault qui accueille des voyageurs depuis 2020 : deux gîtes, location de véhicules, jacuzzi-spa et événements. Disponibles, pas envahissants, et de vraies bonnes adresses."}, APROPOS))

# ============================================================ CONTACT
CONTACT = f'''
<section class="section" style="padding-top:8rem">
  <div class="container contact-grid">
    <div class="reveal">
      <p class="eyebrow">Contact</p>
      <h1>On vous répond <em>vite.</em></h1>
      <p class="lead">WhatsApp est le plus rapide. Pour une question détaillée, l'e-mail va très bien aussi.</p>
      <ul class="contact-list" style="margin-top:2rem">
        <li><span class="ico">{ICON_WA}</span><div><strong>WhatsApp</strong><a href="https://wa.me/590690702529" target="_blank" rel="noopener">+590 690 70 25 29</a></div></li>
        <li><span class="ico">{ICON_TEL}</span><div><strong>Téléphone</strong><a href="tel:+590690702529">+590 690 70 25 29</a></div></li>
        <li><span class="ico">{ICON_MAIL}</span><div><strong>E-mail</strong><a href="mailto:tropicaldream971@gmail.com">tropicaldream971@gmail.com</a></div></li>
        <li><span class="ico">{ICON_PIN}</span><div><strong>Adresse</strong><a href="https://www.google.com/maps/search/?api=1&query=16.2548547,-61.5855826" target="_blank" rel="noopener">6 impasse de la Concorde, Destrellan Boisneuf<br>97122 Baie-Mahault, Guadeloupe</a></div></li>
      </ul>
      <div class="social" style="margin-top:2rem">
        <a href="https://www.instagram.com/tropical_dream_locations_971/" target="_blank" rel="noopener" aria-label="Instagram" style="border-color:var(--ligne);color:var(--encre)">{ICON_IG}</a>
        <a href="https://www.facebook.com/p/Tropical-Dream-Location-Guadeloupe-100045113028874/" target="_blank" rel="noopener" aria-label="Facebook" style="border-color:var(--ligne);color:var(--encre)">{ICON_FB}</a>
      </div>
    </div>
    <form class="form reveal" data-delay="1" id="form-contact" novalidate>
      <div class="fields-2">
        <div class="field"><label for="c-nom">Votre nom</label><input id="c-nom" name="nom" required autocomplete="name"></div>
        <div class="field"><label for="c-tel">Téléphone</label><input id="c-tel" name="tel" type="tel" autocomplete="tel"></div>
      </div>
      <div class="field"><label for="c-email">E-mail</label><input id="c-email" name="email" type="email" required autocomplete="email"></div>
      <div class="field"><label for="c-sujet">Sujet</label><select id="c-sujet" name="sujet"><option>Gîtes</option><option>Location de véhicule</option><option>Jacuzzi-spa / bien-être</option><option>Événement</option><option>Autre</option></select></div>
      <div class="field"><label for="c-msg">Votre message</label><textarea id="c-msg" name="message" required placeholder="Dates, nombre de personnes, ce que vous cherchez..."></textarea></div>
      <div class="hero-actions" style="margin-top:.2rem">
        <button class="btn btn-wa" type="submit" data-via="whatsapp">{ICON_WA} Envoyer par WhatsApp</button>
        <button class="btn btn-ghost" type="submit" data-via="email">{ICON_MAIL} Envoyer par e-mail</button>
      </div>
      <p class="form-note">Le message s'ouvre dans votre application, prêt à être envoyé. Aucune donnée n'est stockée sur ce site.</p>
    </form>
  </div>
</section>

<section class="section-tight section-sable">
  <div class="container map-wrap">
    <div class="reveal">
      <p class="eyebrow">Venir</p>
      <h2>Depuis <em>l'aéroport</em></h2>
      <p class="muted">Sortez de Pôle Caraïbes en direction de Baie-Mahault / Destreland. Comptez 7 minutes. Nous vous envoyons l'itinéraire précis et le code d'accès avant votre arrivée. Si vous louez un véhicule chez nous, on vous attend directement à l'aéroport.</p>
      <p><a class="btn btn-ghost btn-sm" href="https://www.google.com/maps/dir/?api=1&destination=16.2548547,-61.5855826" target="_blank" rel="noopener">Itinéraire Google Maps</a></p>
    </div>
    <div class="map-frame reveal" data-delay="1"><iframe title="Carte Tropical Dream" src="https://www.google.com/maps?q=16.2548547,-61.5855826&z=15&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
  </div>
</section>
'''
PAGES.append(({"file": "contact.html", "title": "Contact — Tropical Dream, Baie-Mahault (WhatsApp, téléphone, e-mail)", "desc": "Contactez Astrid et Christophe : WhatsApp +590 690 70 25 29, tropicaldream971@gmail.com. 6 impasse de la Concorde, 97122 Baie-Mahault, à 7 min de l'aéroport.", "light": True}, CONTACT))

# ============================================================ RÉSERVATION (page complète)
RESA = f'''
<section class="section" style="padding-top:8rem">
  <div class="container">
    <div class="section-head reveal">
      <div><p class="eyebrow">Réservation</p><h1>Composez votre demande, <em>on confirme.</em></h1></div>
      <p class="lead">Aucun paiement en ligne : vous nous envoyez la demande, on vous répond avec la disponibilité et le tarif, vous validez.</p>
    </div>
    <div class="resa-layout" id="resa" data-resa-root data-default-tab="gite">
      <div class="resa-card reveal">
        <div class="resa-tabs" role="tablist" aria-label="Type de réservation" style="grid-template-columns:repeat(4,1fr)">
          <button role="tab" data-tab="gite" aria-selected="true">{ICON_BED}Gîte</button>
          <button role="tab" data-tab="vehicule" aria-selected="false">{ICON_CAR}Véhicule</button>
          <button role="tab" data-tab="bienetre" aria-selected="false">{ICON_SPA}Bien-être</button>
          <button role="tab" data-tab="evenement" aria-selected="false"><span style="font-size:1.3rem;line-height:1">🎉</span>Événement</button>
        </div>

        <div class="resa-panel is-active" data-tab="gite">
          <div class="field"><label for="r-gite">Hébergement</label><select id="r-gite" name="gite"><option value="">Conseillez-moi</option><option>Gîte familial 3 chambres</option><option>Studio Ti Punch (couple)</option><option>Les deux gîtes (groupe)</option></select></div>
          <div class="fields-2">
            <div class="field"><label for="r-arr">Arrivée</label><input id="r-arr" type="date" name="arrivee" required></div>
            <div class="field"><label for="r-dep">Départ</label><input id="r-dep" type="date" name="depart" required></div>
          </div>
          <div class="fields-2">
            <div class="field"><label for="r-ad">Adultes</label><select id="r-ad" name="adultes"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option></select></div>
            <div class="field"><label for="r-en">Enfants</label><select id="r-en" name="enfants"><option value="">0</option><option>1</option><option>2</option><option>3</option></select></div>
          </div>
          <div class="field"><span class="field label" style="font-family:var(--f-mono);font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;color:var(--encre-2)">Souhaits (facultatif)</span>
            <div class="chips">
              <button type="button" class="chip" data-group="options" aria-pressed="false">Véhicule en plus</button>
              <button type="button" class="chip" data-group="options" aria-pressed="false">Navette aéroport</button>
              <button type="button" class="chip" data-group="options" aria-pressed="false">Séance jacuzzi-spa</button>
              <button type="button" class="chip" data-group="options" aria-pressed="false">Lit bébé</button>
              <button type="button" class="chip" data-group="options" aria-pressed="false">Arrivée tardive</button>
            </div>
          </div>
        </div>

        <div class="resa-panel" data-tab="vehicule">
          <div class="field"><label for="r-cat">Catégorie</label><select id="r-cat" name="categorie"><option value="">Conseillez-moi</option><option>Citadine</option><option>Compacte / berline</option><option>SUV / familial</option></select></div>
          <div class="fields-2">
            <div class="field"><label for="r-deb">Début</label><input id="r-deb" type="date" name="debut" required></div>
            <div class="field"><label for="r-hd">Heure</label><input id="r-hd" type="time" name="heure_debut"></div>
          </div>
          <div class="fields-2">
            <div class="field"><label for="r-fin">Fin</label><input id="r-fin" type="date" name="fin" required></div>
            <div class="field"><label for="r-hf">Heure</label><input id="r-hf" type="time" name="heure_fin"></div>
          </div>
          <div class="fields-2">
            <div class="field"><label for="r-liv">Remise du véhicule</label><select id="r-liv" name="livraison"><option>À l'aéroport Pôle Caraïbes</option><option>Au gîte (Baie-Mahault)</option><option>Autre adresse</option></select></div>
            <div class="field"><label for="r-vol">N° de vol (si aéroport)</label><input id="r-vol" name="vol" placeholder="ex. AF 640"></div>
          </div>
          <div class="field"><span style="font-family:var(--f-mono);font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;color:var(--encre-2)">Options</span>
            <div class="chips">
              <button type="button" class="chip" data-group="options" aria-pressed="false">Siège enfant</button>
              <button type="button" class="chip" data-group="options" aria-pressed="false">Conducteur additionnel</button>
              <button type="button" class="chip" data-group="options" aria-pressed="false">Gîte en plus</button>
            </div>
          </div>
        </div>

        <div class="resa-panel" data-tab="bienetre">
          <div class="field"><label for="r-form">Prestation</label><select id="r-form" name="formule"><option>Séance jacuzzi-spa privatif</option><option>Jacuzzi-spa + massage</option><option>Massage détente</option><option>Formule couple</option><option>Bon cadeau</option></select></div>
          <div class="fields-2">
            <div class="field"><label for="r-bd">Date</label><input id="r-bd" type="date" name="date" required></div>
            <div class="field"><label for="r-cr">Créneau</label><select id="r-cr" name="creneau"><option>Matin</option><option>Après-midi</option><option selected>Soirée</option></select></div>
          </div>
          <div class="field"><label for="r-pers">Personnes</label><select id="r-pers" name="personnes"><option>1</option><option selected>2</option><option>3</option><option>4</option></select></div>
          <div class="field"><span style="font-family:var(--f-mono);font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;color:var(--encre-2)">Envies</span>
            <div class="chips">
              <button type="button" class="chip" data-group="options" aria-pressed="false">Occasion spéciale</button>
              <button type="button" class="chip" data-group="options" aria-pressed="false">Boissons</button>
              <button type="button" class="chip" data-group="options" aria-pressed="false">Décoration</button>
            </div>
          </div>
        </div>

        <div class="resa-panel" data-tab="evenement">
          <div class="field"><label for="r-type">Type d'événement</label><select id="r-type" name="type"><option>Anniversaire</option><option>EVJF / EVG</option><option>Réunion de famille</option><option>Séminaire / journée d'équipe</option><option>Autre</option></select></div>
          <div class="fields-2">
            <div class="field"><label for="r-ed">Date</label><input id="r-ed" type="date" name="date" required></div>
            <div class="field"><label for="r-inv">Nombre d'invités</label><input id="r-inv" type="number" name="invites" min="1" placeholder="ex. 12"></div>
          </div>
        </div>

        <hr style="border:0;border-top:1px solid var(--ligne);margin:.4rem 0">
        <div class="fields-2">
          <div class="field"><label for="r-nom">Votre nom</label><input id="r-nom" name="nom" required autocomplete="name"></div>
          <div class="field"><label for="r-tel">Téléphone</label><input id="r-tel" name="tel" type="tel" autocomplete="tel"></div>
        </div>
        <div class="field"><label for="r-msg">Un mot pour nous (facultatif)</label><textarea id="r-msg" name="message" placeholder="Heure d'arrivée, question, occasion..."></textarea></div>
      </div>

      <aside class="resa-summary reveal" data-delay="1">
        <div class="recap">
          <p class="eyebrow">Votre demande</p>
          <h3>Aperçu du message</h3>
          <pre data-recap></pre>
          <button class="btn btn-primary btn-lg" data-send="whatsapp">{ICON_WA} Envoyer sur WhatsApp</button>
          <button class="btn btn-white" data-send="email">{ICON_MAIL} Envoyer par e-mail</button>
          <p class="muted" style="font-size:.85rem;margin:.8rem 0 0;color:rgba(255,255,255,.7)">Réponse rapide, en général dans la journée. Aucune donnée n'est stockée sur ce site.</p>
        </div>
      </aside>
    </div>
  </div>
</section>
'''
PAGES.append(({"file": "reservation.html", "title": "Réserver — gîte, véhicule, jacuzzi-spa ou événement | Tropical Dream Guadeloupe", "desc": "Composez votre demande de réservation (gîte, location de véhicule, séance bien-être, événement) et envoyez-la en un clic sur WhatsApp ou par e-mail. Confirmation rapide.", "light": True, "bodyclass": "no-fab"}, RESA))

# ============================================================ MENTIONS LÉGALES
MENTIONS = '''
<section class="section" style="padding-top:8rem">
  <div class="container narrow prose">
    <p class="eyebrow">Informations légales</p>
    <h1>Mentions <em>légales</em></h1>

    <h2>Éditeur du site</h2>
    <p>TROPICAL DREAM, société par actions simplifiée (SAS) au capital de 1 000 €<br>
    Siège social : 6 impasse de la Concorde, quartier Destrellan Boisneuf, 97122 Baie-Mahault, Guadeloupe<br>
    RCS Pointe-à-Pitre — SIREN 890 410 137<br>
    Président : Christophe Rougeot<br>
    Téléphone : +590 690 70 25 29 · E-mail : tropicaldream971@gmail.com</p>

    <h2>Activités</h2>
    <p>Hébergement touristique et de courte durée (gîtes), location de véhicules, organisation d'événements, prestations de bien-être et de détente.</p>

    <h2>Hébergement du site</h2>
    <p>OVH SAS — 2 rue Kellermann, 59100 Roubaix, France — www.ovhcloud.com</p>

    <h2>Réalisation</h2>
    <p>Conception et développement : NOVALEM — <a href="https://studionovalem.fr" target="_blank" rel="noopener">studionovalem.fr</a></p>

    <h2>Propriété intellectuelle</h2>
    <p>L'ensemble du site (textes, photographies, logo, structure) est la propriété de TROPICAL DREAM ou de ses partenaires et est protégé par le droit d'auteur. Toute reproduction, même partielle, sans autorisation écrite est interdite.</p>

    <h2>Données personnelles</h2>
    <p>Ce site ne collecte et ne stocke aucune donnée personnelle. Les formulaires composent un message qui est envoyé depuis votre propre application (WhatsApp ou messagerie e-mail). Les informations transmises servent uniquement à traiter votre demande de réservation ou de renseignement. Conformément au RGPD, vous pouvez demander l'accès, la rectification ou la suppression de vos données en écrivant à tropicaldream971@gmail.com.</p>

    <h2>Cookies</h2>
    <p>Ce site n'utilise pas de cookies de suivi. La carte intégrée (Google Maps) et les polices de caractères (Google Fonts) peuvent déposer des cookies techniques soumis aux politiques de Google.</p>

    <h2>Réservations et conditions</h2>
    <p>Toute réservation est confirmée par écrit (WhatsApp ou e-mail) après vérification des disponibilités et communication du tarif. Les conditions particulières de location de véhicule (caution, franchise, assurances, kilométrage) sont précisées sur le contrat remis à la prise du véhicule. L'accueil de personnes extérieures à la réservation dans les gîtes n'est pas autorisé.</p>

    <h2>Crédits</h2>
    <p>Photographies : TROPICAL DREAM. Certaines images d'illustration sont susceptibles de provenir de banques d'images libres de droits.</p>
  </div>
</section>
'''
PAGES.append(({"file": "mentions-legales.html", "title": "Mentions légales — Tropical Dream SAS, Baie-Mahault", "desc": "Mentions légales du site Tropical Dream : éditeur, hébergeur, propriété intellectuelle, données personnelles.", "light": True}, MENTIONS))

# ============================================================ 404
P404 = '''
<section class="section" style="padding-top:9rem;min-height:70vh;display:grid;align-items:center">
  <div class="container narrow" style="text-align:center">
    <p class="eyebrow" style="justify-content:center">Erreur 404</p>
    <h1>Cette page est partie <em>à la plage.</em></h1>
    <p class="lead" style="margin-inline:auto">L'adresse n'existe pas ou a changé. Le reste du site, lui, est bien là.</p>
    <div class="hero-actions" style="justify-content:center"><a class="btn btn-primary" href="index.html">Retour à l'accueil</a><a class="btn btn-ghost" href="reservation.html">Réserver</a></div>
  </div>
</section>
'''
PAGES.append(({"file": "404.html", "title": "Page introuvable — Tropical Dream", "desc": "Page introuvable.", "light": True}, P404))
