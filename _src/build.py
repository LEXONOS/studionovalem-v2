# -*- coding: utf-8 -*-
"""Genere les pages SEO de studionovalem.fr a partir de pages.py.
Lancer : python3 _src/build.py (depuis la racine du site). Les pages sortent dans des dossiers
propres (/creation-site-internet-guadeloupe/index.html ...). Aucune dependance."""
import os, re, json, html, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import importlib.util
spec = importlib.util.spec_from_file_location("pages", os.path.join(ROOT, "_src", "pages.py"))
pages = importlib.util.module_from_spec(spec); spec.loader.exec_module(pages)

SITE = "https://studionovalem.fr"
TEL = "+590691253449"
WA = "https://wa.me/590691253449?text="
index = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()

def between(s, a, b):
    i = s.index(a); j = s.index(b, i) + len(b); return s[i:j]

HEADER = between(index, '<header class="nav"', '</header>')
OVERLAY = between(index, '<!-- Menu mobile plein ecran -->', '</div>\n\n<main')
OVERLAY = OVERLAY[:OVERLAY.rindex('</div>')+6]
FOOTER = between(index, '<footer>', '</footer>')
MBAR = between(index, '<div class="mbar">', '<script src="js/main.js" defer></script>')
MBAR = MBAR[:MBAR.rindex('</div>')+6]
HELPER = ''

def rel(block):
    """Passe les liens relatifs de l'accueil en liens depuis un sous-dossier."""
    block = block.replace('href="#', 'href="../#').replace('src="assets/', 'src="../assets/')
    block = block.replace('href="../#top"', 'href="../"')
    return block

def wa(msg):
    from urllib.parse import quote
    return WA + quote(msg)

def faq_html(faq):
    out = ['<div class="acc">']
    for i, (q, a) in enumerate(faq):
        out.append('<details%s><summary>%s</summary><div><p>%s</p></div></details>' % (' open' if i == 0 else '', q, a))
    out.append('</div>')
    return "\n".join(out)

def faq_schema(faq):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": re.sub('<[^>]+>', '', q), "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', a)}} for q, a in faq]}

PLANS = '''
<div class="grid g3 seo-plans">
  <article class="card plan"><div class="name">Essentiel</div><div class="price">490 €</div><p class="for">Une page, livrée en 7 jours. Appeler, WhatsApp, itinéraire, formulaire.</p><a class="btn btn-ghost" href="../#tarifs">Voir le détail</a></article>
  <article class="card plan reco-plan"><div class="badge">Le plus pris</div><div class="name">Vitrine</div><div class="price">990 €</div><p class="for">Jusqu'à 5 pages, galerie, référencement Google complet. 10 à 14 jours.</p><a class="btn" href="../#tarifs">Voir le détail</a></article>
  <article class="card plan"><div class="name">Signature</div><div class="price">1 390 €</div><p class="for">Jusqu'à 10 pages, prise de rendez-vous en ligne, blog. 3 semaines.</p><a class="btn btn-ghost" href="../#tarifs">Voir le détail</a></article>
</div>
<p class="seo-note">Prix fermes, payés une fois, zéro abonnement. Seul frais ensuite : environ 25 € par an d'hébergement, à votre nom. Boutique en ligne, espace client ou outil métier : sur devis.</p>'''

WORKS = '''
<div class="seo-works">
  <a href="https://ifc-guadeloupe.fr" target="_blank" rel="noopener"><b>IFC, Ice Fruits Chocolate</b><span>Sorbets artisanaux, Sainte-Anne. Site vitrine livré en 7 jours.</span></a>
  <a href="https://love-dogs.fr" target="_blank" rel="noopener"><b>Love Dog's</b><span>Éducation canine, Le Gosier. Une page avec simulateur de tarifs.</span></a>
  <a href="https://fontaine-guadeloupe.fr" target="_blank" rel="noopener"><b>Unik'eau</b><span>Fontaines à eau pour entreprises. Offre claire, contact WhatsApp.</span></a>
</div>'''

def render(page):
    slug = page["slug"]; url = SITE + "/" + slug + "/"
    crumbs = [("Accueil", SITE + "/")] + [(c[0], SITE + "/" + c[1] + "/") for c in page.get("crumbs", [])] + [(page["crumb"], url)]
    bc_html = '<nav class="crumbs" aria-label="Fil d\'Ariane">' + ' <span aria-hidden="true">›</span> '.join(
        ('<a href="%s">%s</a>' % (('../' if i == 0 else '../' + c[1].replace(SITE + '/', '')), c[0])) if i < len(crumbs) - 1 else '<span>%s</span>' % c[0]
        for i, c in enumerate(crumbs)) + '</nav>'
    schema = [
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": c[0], "item": c[1]} for i, c in enumerate(crumbs)]},
    ]
    if page.get("faq"):
        f = faq_schema(page["faq"]); f["@context"] = "https://schema.org"; schema.append(f)
    if page.get("service"):
        schema.append({"@context": "https://schema.org", "@type": "Service", "name": page["service"], "serviceType": "Création de site internet",
                       "provider": {"@type": "LocalBusiness", "name": "Studio Novalem", "url": SITE + "/", "telephone": TEL, "email": "contact@studionovalem.fr"},
                       "areaServed": page.get("area", ["Guadeloupe", "Martinique", "Saint-Martin", "Saint-Barthélemy"]),
                       "url": url, "offers": {"@type": "AggregateOffer", "priceCurrency": "EUR", "lowPrice": "490", "highPrice": "1390", "offerCount": "3"}})
    if page.get("article"):
        schema.append({"@context": "https://schema.org", "@type": "Article", "headline": page["h1"], "description": page["desc"], "url": url,
                       "datePublished": page.get("date", "2026-08-27"), "dateModified": page.get("date", "2026-08-27"),
                       "author": {"@type": "Person", "name": "Louis", "url": SITE + "/#louis"},
                       "publisher": {"@type": "Organization", "name": "Studio Novalem", "url": SITE + "/", "logo": {"@type": "ImageObject", "url": SITE + "/assets/logo-monogramme.png"}},
                       "inLanguage": "fr-FR", "about": page.get("about", "Création de sites internet aux Antilles")})
    body = page["body"].replace("{PLANS}", PLANS).replace("{WORKS}", WORKS).replace("{WA}", wa(page.get("wa", "Bonjour Louis, je voudrais un site pour mon commerce.")))
    related = ''
    if page.get("related"):
        related = '<div class="seo-related"><div class="eyebrow">À lire aussi</div><ul>' + ''.join('<li><a href="../%s/">%s</a></li>' % (s, t) for s, t in page["related"]) + '</ul></div>'
    zones = '<div class="seo-zones"><div class="eyebrow">Je travaille sur les quatre îles</div><ul>' + ''.join(
        '<li><a href="../%s/"%s>%s</a></li>' % (s, ' aria-current="page"' if s == slug else '', t) for s, t in pages.ZONES) + '</ul></div>'
    html_out = '''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(url)s">
<meta name="theme-color" content="#1F4FBF">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<link rel="icon" href="../assets/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="../assets/apple-touch-icon.png">
<meta property="og:type" content="%(ogtype)s">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(url)s">
<meta property="og:image" content="%(site)s/assets/og.png">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="Studio Novalem">
<meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="%(georegion)s">
<meta name="geo.placename" content="%(geoplace)s">
<link rel="preload" href="../assets/fonts/anton.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="../assets/fonts/worksans.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="../css/style.css">
<script type="application/ld+json">%(schema)s</script>
</head>
<body class="sub">
<a class="skip" href="#top">Aller au contenu</a>
%(header)s
%(overlay)s
<main id="top">
<section class="seo-hero" aria-labelledby="h1">
  <div class="wrap">
    %(crumbs)s
    <div class="seo-hero-grid">
      <div>
        <div class="kicker"><span class="k-what">%(kicker)s</span><span class="k-where">%(where)s</span></div>
        <h1 id="h1" class="sign sh-j">%(h1)s</h1>
        <p class="lead">%(lead)s</p>
        <div class="cta">
          <a class="btn btn-xl" href="tel:%(tel)s"><span>Appeler Louis<small>0691 25 34 49</small></span></a>
          <a class="btn btn-xl btn-wa" href="%(wa)s" target="_blank" rel="noopener">WhatsApp</a>
        </div>
        <ul class="iles" aria-label="Zones desservies"><li>Guadeloupe</li><li>Martinique</li><li>Saint-Martin</li><li>Saint-Barthélemy</li></ul>
      </div>
      <div class="seo-hero-nono" data-nono="%(pose)s" aria-hidden="true"></div>
    </div>
  </div>
</section>
<section class="seo-body">
  <div class="wrap">
    <div class="seo-grid">
      <article class="seo-content">
        %(body)s
      </article>
      <aside class="seo-aside">
        <div class="seo-card">
          <div class="eyebrow">En bref</div>
          <ul class="seo-facts">
            <li><b>Dès 490 €</b> prix ferme, zéro abonnement</li>
            <li><b>7 jours</b> pour un site une page</li>
            <li><b>Le site vous appartient</b> fichiers remis</li>
            <li><b>SAV gratuit à vie</b> sur les bugs</li>
            <li><b>Sur place</b> en Guadeloupe, à distance sur les autres îles</li>
          </ul>
          <a class="btn" href="tel:%(tel)s">Appeler Louis</a>
          <a class="btn btn-wa" href="%(wa)s" target="_blank" rel="noopener">WhatsApp</a>
        </div>
        %(related)s
        %(zones)s
      </aside>
    </div>
  </div>
</section>
<section class="seo-cta">
  <div class="wrap">
    <div class="works-cta">
      <div class="nono-side" data-nono="coco" aria-hidden="true"></div>
      <div><b class="sign">On en parle ?</b><p>Un appel de 30 minutes, un prix ferme sous 48 h, et votre site en ligne dans les jours qui suivent.</p></div>
      <a class="btn btn-lg" href="tel:%(tel)s">Appeler Louis</a>
    </div>
  </div>
</section>
</main>
%(footer)s
%(mbar)s
%(helper)s
<script src="../js/main.js" defer></script>
</body>
</html>''' % dict(
        title=html.escape(page["title"], quote=True), desc=html.escape(page["desc"], quote=True), url=url, site=SITE,
        ogtype="article" if page.get("article") else "website",
        georegion=page.get("georegion", "GP"), geoplace=html.escape(page.get("geoplace", "Guadeloupe"), quote=True),
        schema=json.dumps(schema, ensure_ascii=False), header=rel(HEADER), overlay=rel(OVERLAY), crumbs=bc_html,
        kicker=page.get("kicker", "Création de sites internet"), where=page.get("where", "aux Antilles"), h1=page["h1"], lead=page["lead"],
        tel=TEL, wa=wa(page.get("wa", "Bonjour Louis, je voudrais un site pour mon commerce.")), pose=page.get("pose", "salut"),
        body=body, related=related, zones=zones, footer=rel(FOOTER), mbar=rel(MBAR), helper=rel(HELPER))
    d = os.path.join(ROOT, slug); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(html_out)
    return url

urls = [SITE + "/"]
for p in pages.PAGES:
    urls.append(render(p))

today = datetime.date.today().isoformat()
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for i, u in enumerate(urls):
    pr = "1.0" if i == 0 else ("0.9" if "creation-site-internet" in u else "0.7")
    sm.append('  <url><loc>%s</loc><lastmod>%s</lastmod><changefreq>%s</changefreq><priority>%s</priority></url>' % (u, today, "weekly" if i == 0 else "monthly", pr))
sm.append('</urlset>')
open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(sm))
print("pages:", len(urls))
