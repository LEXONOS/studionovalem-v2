#!/usr/bin/env python3
"""Assemble les pages finales à partir de _src/pages/*.html + gabarits communs.
Usage : python3 _src/build.py   (depuis la racine du projet)
Le site livré n'a PAS besoin de ce script : les .html générés sont autonomes."""
import os, re, json, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_URL = "https://www.tropicaldream-guadeloupe.fr"  # à remplacer par le vrai domaine
IMG = "https://images.unsplash.com/"
U = lambda pid, w=1600: f"{IMG}{pid}?auto=format&fit=crop&w={w}&q=80"

# Nom local -> photo d'attente (Unsplash). Dès que la vraie photo est dans assets/img/, elle prend le dessus.
PHOTOS = {
    "hero-piscine.jpg":        ("Vue générale : piscine, terrasse et gîtes au soleil (photo large, horizontale)", U("photo-1540541338287-41700207dee6", 2000)),
    "univers-gite.jpg":        ("Chambre ou salon d'un gîte, lumineux (verticale)", U("photo-1522771739844-6a9f6d5f14af")),
    "univers-vehicule.jpg":    ("Un véhicule de la flotte devant le gîte ou sur une route de Guadeloupe (verticale)", U("photo-1494976388531-d1058494cdd8")),
    "univers-spa.jpg":         ("Le jacuzzi-spa, idéalement de nuit ou au coucher du soleil (verticale)", U("photo-1544161515-4ab6ce6db874")),
    "hotes.jpg":               ("Astrid et Christophe (portrait, sourire, devant la maison ou la piscine)", U("photo-1519046904884-53103b34b206")),
    "gite-familial-salon.jpg": ("Gîte familial : salon avec TV", U("photo-1560448204-e02f11c3d0e2")),
    "gite-familial-chambre.jpg": ("Gîte familial : chambre principale, lit fait", U("photo-1616594039964-ae9021a400a0")),
    "gite-familial-cuisine.jpg": ("Gîte familial : cuisine équipée (lave-vaisselle, four)", U("photo-1556909114-f6e7ad7d3136")),
    "gite-familial-sdb.jpg":   ("Gîte familial : salle de bain douche à l'italienne", U("photo-1552321554-5fefe8c9ef14")),
    "studio-chambre.jpg":      ("Studio Ti Punch : lit et coin nuit", U("photo-1505693416388-ac5ce068fe85")),
    "studio-terrasse.jpg":     ("Studio Ti Punch : terrasse privée", U("photo-1522708323590-d24dbb6b0267")),
    "piscine-2.jpg":           ("Piscine, autre angle (transats, végétation)", U("photo-1571003123894-1f0594d2b5d9")),
    "piscine-enfants.jpg":     ("Piscine enfants / pataugeoire", U("photo-1576013551627-0cc20b96c2a7")),
    "jeux-enfants.jpg":        ("Aire de jeux extérieure ou jeux intérieurs", U("photo-1596464716127-f2a82984de30")),
    "cuisine-exterieure.jpg":  ("Cuisine extérieure / coin repas dehors (les clients l'adorent)", U("photo-1600585154340-be6161a56a0c")),
    "barbecue.jpg":            ("Barbecue en fonctionnement, soirée", U("photo-1555939594-58d7cb561ad1")),
    "jardin.jpg":              ("Jardin tropical, fleurs, ombre", U("photo-1509233725247-49e657c54213")),
    "jacuzzi-1.jpg":           ("Jacuzzi-spa, eau qui bouillonne, cadre intime", U("photo-1571902943202-507ec2618e8f")),
    "jacuzzi-2.jpg":           ("Jacuzzi-spa de nuit, bougies/lumières (ambiance couple)", U("photo-1560750588-73207b1ef5b8")),
    "massage.jpg":             ("Espace massage / détente", U("photo-1600334129128-685c5582fd35")),
    "vehicule-citadine.jpg":   ("Véhicule catégorie citadine (photo 3/4 avant, propre)", U("photo-1549317661-bd32c8ce0db2")),
    "vehicule-compacte.jpg":   ("Véhicule catégorie compacte / berline", U("photo-1552519507-da3b142c6e3d")),
    "vehicule-suv.jpg":        ("Véhicule catégorie SUV / familial", U("photo-1519641471654-76ce0107ad1b")),
    "aeroport.jpg":            ("Remise des clés à l'aéroport Pôle Caraïbes", U("photo-1436491865332-7a61a109cc05")),
    "evenement-1.jpg":         ("Table dressée pour un anniversaire / événement au gîte", U("photo-1530103862676-de8c9debad1d")),
    "evenement-2.jpg":         ("Ambiance fête : ballons, gâteau, décoration", U("photo-1464366400600-7168b8af9bc3")),
    "guadeloupe-plage.jpg":    ("Une plage de Guadeloupe (Grande-Anse, Caravelle...)", U("photo-1507525428034-b723cf961d3e")),
    "guadeloupe-nature.jpg":   ("Cascade / rivière / forêt de Basse-Terre", U("photo-1501785888041-af3ef285b470")),
    "og-image.jpg":            ("Image de partage réseaux (1200×630) : la piscine et les gîtes", U("photo-1540541338287-41700207dee6", 1200)),
}

def img(name, alt, cls="", extra="", loading="lazy"):
    fb = PHOTOS[name][1]
    c = f' class="{cls}"' if cls else ""
    return f'<img src="assets/img/{name}" data-fallback="{fb}" alt="{alt}"{c} loading="{loading}" decoding="async"{extra}>'

def gal(name, alt, cls=""):
    fb = PHOTOS[name][1]
    c = f' class="{cls}"' if cls else ""
    return f'<a href="assets/img/{name}" data-lightbox data-src="assets/img/{name}" data-caption="{alt}"{c}>{img(name, alt)}</a>'

ICON_WA = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.6.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3a.5.5 0 0 0 0-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 2.9 2.9 0 0 0-.9 2.2 5.1 5.1 0 0 0 1.1 2.7 11.6 11.6 0 0 0 4.4 3.9c1.6.7 2.3.8 3.1.6a2.6 2.6 0 0 0 1.7-1.2 2.1 2.1 0 0 0 .2-1.2c-.1-.1-.3-.2-.5-.3z"/></svg>'
ICON_TEL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8.1 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.8 2z"/></svg>'
ICON_MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 7L2 7"/></svg>'
ICON_PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>'
ICON_IG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>'
ICON_FB = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 22v-8h2.7l.4-3.3h-3.1V8.6c0-1 .3-1.6 1.6-1.6h1.7V4.1c-.3 0-1.3-.1-2.5-.1-2.5 0-4.1 1.5-4.1 4.2v2.5H7.4V14h2.8v8z"/></svg>'
ICON_BED = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 18v-6a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v6M3 18h18M5 10V6a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v4"/></svg>'
ICON_CAR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 17h14M5 17a2 2 0 1 1-4 0 2 2 0 0 1 4 0zm18 0a2 2 0 1 1-4 0 2 2 0 0 1 4 0zM3 13l2-6a2 2 0 0 1 2-1.4h10a2 2 0 0 1 2 1.4l2 6M3 13v4m18-4v4"/></svg>'
ICON_SPA = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 14c2-3 6-3 9 0s7 3 9 0M3 18c2-3 6-3 9 0s7 3 9 0M12 3v2M8 5l1 2M16 5l-1 2"/></svg>'

NAV = [
    ("index.html", "Accueil"),
    ("gites.html", "Gîtes"),
    ("vehicules.html", "Véhicules"),
    ("bien-etre.html", "Bien-être"),
    ("evenements.html", "Événements"),
    ("a-propos.html", "À propos"),
    ("contact.html", "Contact"),
]

def header(light):
    links = "".join(f'<a href="{h}">{l}</a>' for h, l in NAV)
    return f'''<header class="site-header" data-light="{'true' if light else 'false'}">
  <div class="container header-inner">
    <a class="brand" href="index.html" aria-label="Tropical Dream, accueil">
      <svg viewBox="0 0 64 64" aria-hidden="true"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1fa598"/><stop offset="1" stop-color="#10302e"/></linearGradient></defs><rect width="64" height="64" rx="18" fill="url(#lg)"/><circle cx="40" cy="24" r="8" fill="#ffd166"/><path d="M10 40c6-6 12-6 18 0s12 6 18 0 12-6 18 0" fill="none" stroke="#f5f6f2" stroke-width="3.2" stroke-linecap="round"/><path d="M10 50c6-6 12-6 18 0s12 6 18 0 12-6 18 0" fill="none" stroke="#f5f6f2" stroke-width="3.2" stroke-linecap="round" opacity=".55"/><path d="M18 34c-1-9 3-16 10-20-2 6-2 12 0 17M18 34c-6-6-6-14-2-20 1 6 4 11 8 15M18 34c-8-2-13-8-13-15 5 3 9 7 11 12" fill="none" stroke="#9fe0d6" stroke-width="2.4" stroke-linecap="round"/></svg>
      <span class="brand-name">Tropical Dream<small>Baie-Mahault · Guadeloupe</small></span>
    </a>
    <nav class="nav" aria-label="Navigation principale">
      {links}
      <div class="nav-mobile-cta">
        <a class="btn btn-wa btn-sm" href="https://wa.me/590690702529" target="_blank" rel="noopener">{ICON_WA} WhatsApp</a>
        <a class="btn btn-primary btn-sm" href="reservation.html">Réserver</a>
      </div>
    </nav>
    <div class="header-cta">
      <a class="btn btn-primary btn-sm" href="#" data-open-resa="gite">Réserver</a>
      <button class="nav-toggle" aria-label="Ouvrir le menu" aria-expanded="false"><span></span></button>
    </div>
  </div>
</header>'''

FOOTER = f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <span class="brand-name" style="color:#fff">Tropical Dream<small>Gîtes · Véhicules · Bien-être</small></span>
        <p>Une adresse familiale au centre de la Guadeloupe pour dormir, rouler et souffler. Astrid et Christophe habitent juste à côté et répondent vite.</p>
        <div class="social">
          <a href="https://www.instagram.com/tropical_dream_locations_971/" target="_blank" rel="noopener" aria-label="Instagram">{ICON_IG}</a>
          <a href="https://www.facebook.com/p/Tropical-Dream-Location-Guadeloupe-100045113028874/" target="_blank" rel="noopener" aria-label="Facebook">{ICON_FB}</a>
          <a href="https://wa.me/590690702529" target="_blank" rel="noopener" aria-label="WhatsApp">{ICON_WA}</a>
        </div>
      </div>
      <div>
        <h4>Explorer</h4>
        <ul>
          <li><a href="gites.html">Les gîtes</a></li>
          <li><a href="vehicules.html">Location de véhicules</a></li>
          <li><a href="bien-etre.html">Jacuzzi-spa &amp; bien-être</a></li>
          <li><a href="evenements.html">Événements</a></li>
          <li><a href="a-propos.html">Astrid &amp; Christophe</a></li>
        </ul>
      </div>
      <div>
        <h4>Réserver</h4>
        <ul>
          <li><a href="reservation.html?resa=gite">Un gîte</a></li>
          <li><a href="reservation.html?resa=vehicule">Un véhicule</a></li>
          <li><a href="reservation.html?resa=bienetre">Une séance bien-être</a></li>
          <li><a href="contact.html">Poser une question</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="tel:+590690702529">+590 690 70 25 29</a></li>
          <li><a href="mailto:tropicaldream971@gmail.com">tropicaldream971@gmail.com</a></li>
          <li>6 impasse de la Concorde<br>Destrellan Boisneuf<br>97122 Baie-Mahault</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> Tropical Dream SAS · Tous droits réservés</span>
      <span><a href="mentions-legales.html">Mentions légales</a> · Site réalisé par <a href="https://studionovalem.fr" target="_blank" rel="noopener">NOVALEM</a></span>
    </div>
  </div>
</footer>'''

def guichet(compact=True):
    """Mini formulaire à 3 onglets : dans le hero et dans le tiroir."""
    return f'''<div class="guichet" data-resa-root data-default-tab="gite">
  <div class="guichet-tabs" role="tablist" aria-label="Type de réservation">
    <button role="tab" data-tab="gite" aria-selected="true">Gîte</button>
    <button role="tab" data-tab="vehicule" aria-selected="false">Véhicule</button>
    <button role="tab" data-tab="bienetre" aria-selected="false">Bien-être</button>
  </div>
  <div class="guichet-panel is-active" data-tab="gite">
    <div class="fields-2">
      <div class="field"><label for="g-arr">Arrivée</label><input id="g-arr" type="date" name="arrivee" required></div>
      <div class="field"><label for="g-dep">Départ</label><input id="g-dep" type="date" name="depart" required></div>
    </div>
    <div class="fields-2">
      <div class="field"><label for="g-ad">Adultes</label><select id="g-ad" name="adultes"><option>1</option><option selected>2</option><option>3</option><option>4</option></select></div>
      <div class="field"><label for="g-en">Enfants</label><select id="g-en" name="enfants"><option value="">0</option><option>1</option><option>2</option><option>3</option></select></div>
    </div>
    <div class="field"><label for="g-gite">Hébergement</label>
      <select id="g-gite" name="gite"><option value="">Conseillez-moi</option><option>Gîte familial 3 chambres</option><option>Studio Ti Punch (couple)</option><option>Les deux gîtes (groupe)</option></select></div>
  </div>
  <div class="guichet-panel" data-tab="vehicule">
    <div class="fields-2">
      <div class="field"><label for="v-deb">Début</label><input id="v-deb" type="date" name="debut" required></div>
      <div class="field"><label for="v-fin">Fin</label><input id="v-fin" type="date" name="fin" required></div>
    </div>
    <div class="field"><label for="v-cat">Catégorie</label>
      <select id="v-cat" name="categorie"><option value="">Conseillez-moi</option><option>Citadine</option><option>Compacte / berline</option><option>SUV / familial</option></select></div>
    <div class="field"><label for="v-liv">Remise du véhicule</label>
      <select id="v-liv" name="livraison"><option>À l'aéroport Pôle Caraïbes</option><option>Au gîte (Baie-Mahault)</option><option>Autre adresse</option></select></div>
  </div>
  <div class="guichet-panel" data-tab="bienetre">
    <div class="fields-2">
      <div class="field"><label for="b-date">Date</label><input id="b-date" type="date" name="date" required></div>
      <div class="field"><label for="b-cr">Créneau</label><select id="b-cr" name="creneau"><option>Matin</option><option>Après-midi</option><option selected>Soirée</option></select></div>
    </div>
    <div class="field"><label for="b-form">Prestation</label>
      <select id="b-form" name="formule"><option>Séance jacuzzi-spa privatif</option><option>Jacuzzi-spa + massage</option><option>Massage détente</option><option>Formule couple</option></select></div>
    <div class="field"><label for="b-pers">Personnes</label><select id="b-pers" name="personnes"><option>1</option><option selected>2</option><option>3</option><option>4</option></select></div>
  </div>
  <button class="btn btn-primary" data-send="whatsapp">{ICON_WA} Demander sur WhatsApp</button>
  <p class="guichet-note">Réponse rapide d'Astrid ou Christophe · ou <a href="#" data-send="email">envoyer par e-mail</a></p>
</div>'''

def drawer():
    return f'''<a class="btn btn-primary btn-lg fab-resa" href="#" data-open-resa="gite">Réserver</a>
<div class="drawer-backdrop"></div>
<aside class="drawer" aria-label="Réservation rapide">
  <div class="drawer-head"><h2>Réservation rapide</h2><button class="drawer-close" aria-label="Fermer">×</button></div>
  <p class="muted" style="margin:0">Choisissez, indiquez vos dates, envoyez : on vous confirme la disponibilité et le tarif.</p>
  {guichet()}
  <p class="muted" style="font-size:.88rem">Besoin de plus d'options ? <a href="reservation.html">Ouvrir la page de réservation complète</a>.</p>
</aside>
<div class="mobile-bar">
  <a class="btn btn-ghost" href="tel:+590690702529">{ICON_TEL} Appeler</a>
  <a class="btn btn-wa" href="https://wa.me/590690702529" target="_blank" rel="noopener">{ICON_WA} WhatsApp</a>
  <a class="btn btn-primary" href="#" data-open-resa="gite">Réserver</a>
</div>'''

def jsonld_base():
    return {
        "@context": "https://schema.org",
        "@type": ["LodgingBusiness", "AutoRental", "DaySpa"],
        "name": "Tropical Dream — Location de véhicules, gîtes & bien-être",
        "url": SITE_URL + "/",
        "telephone": "+590690702529",
        "email": "tropicaldream971@gmail.com",
        "image": SITE_URL + "/assets/img/og-image.jpg",
        "address": {"@type": "PostalAddress", "streetAddress": "6 impasse de la Concorde, Destrellan Boisneuf", "postalCode": "97122", "addressLocality": "Baie-Mahault", "addressRegion": "Guadeloupe", "addressCountry": "GP"},
        "geo": {"@type": "GeoCoordinates", "latitude": 16.2548547, "longitude": -61.5855826},
        "priceRange": "€€",
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.8", "reviewCount": "32", "bestRating": "5"},
        "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": n, "value": True} for n in ["Piscine", "Piscine enfants", "Wi-Fi", "Parking privé gratuit", "Climatisation", "Jacuzzi-spa", "Barbecue", "Cuisine extérieure", "Navette aéroport", "Location de voitures"]],
        "sameAs": ["https://www.instagram.com/tropical_dream_locations_971/", "https://www.facebook.com/p/Tropical-Dream-Location-Guadeloupe-100045113028874/"],
    }

def page(meta, body):
    light = meta.get("light", False)
    ld = meta.get("jsonld") or jsonld_base()
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{meta["title"]}</title>
  <meta name="description" content="{meta["desc"]}">
  <link rel="canonical" href="{SITE_URL}/{meta["file"]}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="fr_FR">
  <meta property="og:title" content="{meta["title"]}">
  <meta property="og:description" content="{meta["desc"]}">
  <meta property="og:url" content="{SITE_URL}/{meta["file"]}">
  <meta property="og:image" content="{SITE_URL}/assets/img/og-image.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="theme-color" content="#10302e">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="assets/img/logo.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT@0,9..144,300..700,0..100;1,9..144,300..700,0..100&family=Instrument+Sans:ital,wght@0,400..700;1,400..700&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/styles.css">
  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body class="{meta.get('bodyclass','')}">
<a class="sr-only" href="#main">Aller au contenu</a>
{header(light)}
<main id="main">
{body}
</main>
{FOOTER}
{drawer()}
<script src="assets/js/main.js" defer></script>
<script src="assets/js/reservation.js" defer></script>
</body>
</html>
'''

def build():
    import importlib.util
    spec = importlib.util.spec_from_file_location("pages", os.path.join(ROOT, "_src", "pages.py"))
    pages = importlib.util.module_from_spec(spec)
    pages.img, pages.gal, pages.guichet = img, gal, guichet
    for k in ["ICON_WA","ICON_TEL","ICON_MAIL","ICON_PIN","ICON_BED","ICON_CAR","ICON_SPA","ICON_IG","ICON_FB","PHOTOS","SITE_URL","jsonld_base"]:
        setattr(pages, k, globals()[k])
    spec.loader.exec_module(pages)
    files = []
    for meta, body in pages.PAGES:
        out = os.path.join(ROOT, meta["file"])
        with open(out, "w", encoding="utf-8") as f:
            f.write(page(meta, body))
        files.append(meta["file"])
        print("✔", meta["file"])
    # sitemap
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for fn in files:
            if fn in ("404.html",): continue
            f.write(f"  <url><loc>{SITE_URL}/{'' if fn=='index.html' else fn}</loc></url>\n")
        f.write("</urlset>\n")
    # photo brief
    with open(os.path.join(ROOT, "PHOTOS-A-AJOUTER.md"), "w", encoding="utf-8") as f:
        f.write("# Photos à déposer dans `assets/img/`\n\n")
        f.write("Le site fonctionne déjà avec des photos d'attente (Unsplash, chargées en ligne). Dès qu'un fichier portant EXACTEMENT le nom ci-dessous est déposé dans `assets/img/`, il remplace automatiquement la photo d'attente, sans toucher au code.\n\n")
        f.write("Sources à piller pour le client : la fiche Google Business (photos), Booking.com (fiche « Tropical Dream - Gîte Touristique »), Instagram @tropical_dream_locations_971, la page Facebook. Format conseillé : JPG, 1600 px de large (2000 px pour le hero), poids < 400 ko (compresser sur squoosh.app).\n\n")
        f.write("| Fichier | Ce qu'il faut dessus |\n|---|---|\n")
        for k, (d, _) in PHOTOS.items():
            f.write(f"| `{k}` | {d} |\n")
        f.write("\nQuand toutes les photos sont en place, supprimer les attributs `data-fallback` est facultatif : ils ne servent plus.\n")

if __name__ == "__main__":
    build()
