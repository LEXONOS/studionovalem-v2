/* STUDIO NOVALEM : main.js
   Scroll natif, zero dependance. Tout se degrade proprement sans JS. */
(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var WA = 'https://wa.me/590691253449?text=';
  var TEL = 'tel:+590691253449';
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------- Nono, la mascotte : une enseigne sur pattes ---------- */
  function nono(pose, text) {
    var arms = {
      salut:   { l: 'M44 118c-14 10-24 28-24 46', r: 'M156 118c14-12 26-30 30-52', h: [186, 66], rc: 'arm-wave' },
      pointe:  { l: 'M44 118c-14 10-22 28-20 46', r: 'M156 118c20 0 40-2 60-6', h: [216, 112], rc: '' },
      tel:     { l: 'M44 118c-14 10-24 28-24 46', r: 'M156 118c14 0 22-10 18-30', h: [174, 88], rc: '' },
      plan:    { l: 'M44 118c-10 16-6 30 8 40', r: 'M156 118c10 16 6 30-8 40', h: [148, 158], rc: '' },
      marteau: { l: 'M44 118c-14 10-24 28-24 46', r: 'M156 118c18-8 30-24 34-44', h: [190, 74], rc: 'hammer' },
      drapeau: { l: 'M44 118c-14 10-24 28-24 46', r: 'M156 118c16-6 26-16 30-30', h: [186, 88], rc: 'flag' },
      coco:    { l: 'M44 118c-14 10-24 28-24 46', r: 'M156 118c8 4 14 14 12 26', h: [168, 144], rc: '' },
      courrier:{ l: 'M44 118c-14 10-24 28-24 46', r: 'M156 118c20 0 36 8 48 24', h: [204, 142], rc: '' },
      plaque:  { l: 'M44 118c-14 10-24 28-24 46', r: 'M156 118c20 0 34 10 40 26', h: [196, 144], rc: '' },
      loupe:   { l: 'M44 118c-14 10-24 28-24 46', r: 'M156 118c18-4 30-12 38-26', h: [194, 92], rc: '' },
      robot:   { l: 'M44 118c-20 4-30 14-32 30', r: 'M156 118c20 4 30 14 32 30', h: [188, 148], rc: '' }
    }[pose] || {};
    var prop = '';
    if (pose === 'tel') prop = '<g><rect x="164" y="56" width="24" height="42" rx="6" fill="#111"/><rect x="168" y="62" width="16" height="28" rx="3" fill="#F5C400"/></g>';
    if (pose === 'plan') prop = '<g><rect x="60" y="150" width="80" height="54" rx="4" fill="#fff" stroke="#111" stroke-width="4"/><path d="M70 162h60M70 174h40M70 186h50" stroke="#1F4FBF" stroke-width="4" stroke-linecap="round" stroke-dasharray="3 6"/></g>';
    if (pose === 'marteau') prop = '<g class="hammer"><path d="M190 74l6-26" stroke="#111" stroke-width="7" stroke-linecap="round"/><rect x="176" y="34" width="40" height="22" rx="5" fill="#F5C400" stroke="#111" stroke-width="4" transform="rotate(12 196 45)"/></g>';
    if (pose === 'drapeau') prop = '<g class="flag"><path d="M186 88V22" stroke="#111" stroke-width="6" stroke-linecap="round"/><path d="M188 24h50l-10 14 10 14h-50z" fill="#F5C400" stroke="#111" stroke-width="4" stroke-linejoin="round"/><text x="208" y="44" text-anchor="middle" font-family="Anton, Impact, sans-serif" font-size="14" fill="#111">EN LIGNE</text></g>';
    if (pose === 'courrier') prop = '<g><rect x="184" y="126" width="46" height="32" rx="4" fill="#fff" stroke="#111" stroke-width="4"/><path d="M184 128l23 16 23-16" fill="none" stroke="#111" stroke-width="4" stroke-linejoin="round"/><rect x="214" y="129" width="12" height="10" fill="#F5C400" stroke="#111" stroke-width="2"/></g>';
    if (pose === 'plaque') prop = '<g><path d="M196 144v-36" stroke="#111" stroke-width="6" stroke-linecap="round"/><rect x="152" y="52" width="88" height="56" rx="8" fill="#F5C400" stroke="#111" stroke-width="4" transform="rotate(-6 196 80)"/><text x="196" y="90" text-anchor="middle" font-family="Anton, Impact, sans-serif" font-size="26" fill="#111" transform="rotate(-6 196 80)">' + (text || '') + '</text></g>';
    if (pose === 'loupe') prop = '<g><circle cx="214" cy="60" r="20" fill="#E7EDFB" stroke="#111" stroke-width="5"/><path d="M200 74l-8 12" stroke="#111" stroke-width="7" stroke-linecap="round"/><path d="M206 52a10 10 0 0 1 12-4" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/></g>';
    if (pose === 'robot') prop = '<g><path d="M100 38V16" stroke="#111" stroke-width="5" stroke-linecap="round"/><circle cx="100" cy="12" r="7" fill="#F5C400" stroke="#111" stroke-width="3"/><rect x="66" y="88" width="30" height="20" rx="3" fill="#2EE3AF" stroke="#111" stroke-width="3"/><rect x="104" y="88" width="30" height="20" rx="3" fill="#2EE3AF" stroke="#111" stroke-width="3"/></g>';
    if (pose === 'coco') prop = '<g><circle cx="176" cy="152" r="22" fill="#8B5A2B" stroke="#111" stroke-width="4"/><path d="M180 132l14-30" stroke="#F5C400" stroke-width="5" stroke-linecap="round"/><path d="M190 108l10-4" stroke="#F5C400" stroke-width="5" stroke-linecap="round"/><path d="M160 138c8-10 24-10 32 0" fill="none" stroke="#111" stroke-width="3"/></g><g class="steam" opacity=".6"><circle cx="196" cy="98" r="3" fill="#fff"/></g>';
    var glasses = pose === 'coco' ? '<rect x="66" y="92" width="30" height="16" rx="6" fill="#111"/><rect x="104" y="92" width="30" height="16" rx="6" fill="#111"/><path d="M96 100h8" stroke="#111" stroke-width="4"/>' : '';
    var mouth = pose === 'coco' ? '<path d="M88 122c8 8 16 8 24 0" fill="none" stroke="#111" stroke-width="4" stroke-linecap="round"/>' : (pose === 'marteau' ? '<path d="M90 122h20" stroke="#111" stroke-width="4" stroke-linecap="round"/>' : '<path d="M88 118c8 10 16 10 24 0" fill="none" stroke="#111" stroke-width="4" stroke-linecap="round"/>');
    var hand = '<circle cx="' + arms.h[0] + '" cy="' + arms.h[1] + '" r="10" fill="#F5C400" stroke="#111" stroke-width="4"/>';
    return '<svg class="nono" viewBox="0 0 240 260" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' +
      '<g class="bob">' +
      '<g class="leg l"><path d="M84 190l-6 46" stroke="#111" stroke-width="8" stroke-linecap="round"/><ellipse cx="72" cy="240" rx="18" ry="9" fill="#F5C400" stroke="#111" stroke-width="4"/></g>' +
      '<g class="leg r"><path d="M116 190l6 46" stroke="#111" stroke-width="8" stroke-linecap="round"/><ellipse cx="128" cy="240" rx="18" ry="9" fill="#F5C400" stroke="#111" stroke-width="4"/></g>' +
      '<rect x="40" y="62" width="120" height="130" rx="18" fill="#1F4FBF" stroke="#111" stroke-width="5"/>' +
      '<rect x="49" y="71" width="102" height="112" rx="12" fill="none" stroke="#F7F5EF" stroke-width="7"/>' +
      '<path d="M56 62c0-14 12-24 44-24s44 10 44 24z" fill="#F5C400" stroke="#111" stroke-width="5"/><path d="M40 62h130" stroke="#111" stroke-width="6" stroke-linecap="round"/>' +
      '<g class="eye"><ellipse cx="82" cy="100" rx="11" ry="13" fill="#fff" stroke="#111" stroke-width="3"/><circle cx="85" cy="102" r="5" fill="#111"/></g>' +
      '<g class="eye"><ellipse cx="118" cy="100" rx="11" ry="13" fill="#fff" stroke="#111" stroke-width="3"/><circle cx="121" cy="102" r="5" fill="#111"/></g>' +
      glasses + mouth +
      '<text x="103" y="176" text-anchor="middle" font-family="Anton, Impact, sans-serif" font-size="44" fill="#F5C400">N</text><text x="100" y="173" text-anchor="middle" font-family="Anton, Impact, sans-serif" font-size="44" fill="#F7F5EF">N</text>' +
      '<path d="' + arms.l + '" fill="none" stroke="#111" stroke-width="8" stroke-linecap="round"/><circle cx="20" cy="166" r="10" fill="#F5C400" stroke="#111" stroke-width="4"/>' +
      '<g class="' + arms.rc + '"><path d="' + arms.r + '" fill="none" stroke="#111" stroke-width="8" stroke-linecap="round"/>' + prop + hand + '</g>' +
      '</g></svg>';
  }
  function paint(el, pose, text) { if (el) { el.innerHTML = nono(pose, text); el.setAttribute('data-nono', pose); } }
  $$('[data-nono]').forEach(function (el) { paint(el, el.getAttribute('data-nono')); });
  var walker = $('#walker'); if (walker) walker.innerHTML = nono('pointe');
  var walkTimer = null;
  function walking(el, on) { if (el) el.classList.toggle('walking', on); }

  /* Hero : Nono decroche quand on vise le bouton, l'enseigne s'allume au clic */
  var heroNono = $('#nono-hero'), ctaTel = $('#cta-tel'), scene = $('#scene');
  if (ctaTel && heroNono) {
    ctaTel.addEventListener('mouseenter', function () { paint(heroNono, 'tel'); });
    ctaTel.addEventListener('mouseleave', function () { paint(heroNono, 'salut'); });
  }
  if (scene) {
    scene.addEventListener('click', function () {
      scene.classList.remove('flash'); void scene.offsetWidth; scene.classList.add('flash');
      var b = $('.bob', heroNono); if (b) { b.classList.remove('jump'); void b.getBoundingClientRect(); b.classList.add('jump'); }
    });
  }

  /* ---------- Navigation ---------- */
  var toggle = $('.nav-toggle'), overlay = $('#overlay');
  function setMenu(open) {
    overlay.hidden = !open;
    toggle.setAttribute('aria-expanded', String(open));
    document.body.style.overflow = open ? 'hidden' : '';
  }
  if (toggle && overlay) {
    toggle.addEventListener('click', function () { setMenu(overlay.hidden); });
    $$('a', overlay).forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !overlay.hidden) setMenu(false); });
    window.addEventListener('resize', function () { if (window.innerWidth > 980 && !overlay.hidden) setMenu(false); });
  }

  var prog = $('#progress');
  var navLinks = $$('.nav-links a');
  var sections = navLinks.map(function (a) { var h = a.getAttribute('href') || ''; return h.charAt(0) === '#' ? $(h) : null; }).filter(Boolean);
  var ticking = false;
  function onScroll() {
    if (ticking) return; ticking = true;
    requestAnimationFrame(function () {
      var h = document.documentElement;
      var max = h.scrollHeight - h.clientHeight;
      var pc = max > 0 ? (h.scrollTop / max) * 100 : 0;
      if (prog) prog.style.width = pc + '%';
      if (walker) { walker.style.left = 'clamp(16px, ' + pc + '%, calc(100% - 16px))'; walking(walker, true); clearTimeout(walkTimer); walkTimer = setTimeout(function () { walking(walker, false); }, 180); }
      var hp = $('#helper'); if (hp) hp.classList.toggle('show', h.scrollTop > 420 || (hp.querySelector('.helper-panel') && !hp.querySelector('.helper-panel').hidden));
      var y = h.scrollTop + 160, cur = null;
      sections.forEach(function (s) { if (s.offsetTop <= y) cur = s; });
      navLinks.forEach(function (a) { a.classList.toggle('on', cur && a.getAttribute('href') === '#' + cur.id); });
      ticking = false;
    });
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------- Apparitions ---------- */
  var rv = $$('.rv');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    rv.forEach(function (el) { io.observe(el); });
  } else {
    rv.forEach(function (el) { el.classList.add('in'); });
  }
  var hero = $('.hero');
  if (hero) {
    requestAnimationFrame(function () { hero.classList.add('in'); });
    setTimeout(function () { hero.classList.add('done'); }, reduce ? 0 : 2200);
  }
  function whenVisible(el, cb, margin) {
    if (!el) return;
    if (!('IntersectionObserver' in window)) { cb(); return; }
    var o = new IntersectionObserver(function (entries) {
      if (entries[0].isIntersecting) { cb(); o.disconnect(); }
    }, { rootMargin: margin || '0px 0px -10% 0px', threshold: 0.15 });
    o.observe(el);
  }
  var stepsWalker = $('#steps-walker'); if (stepsWalker) stepsWalker.innerHTML = nono('marteau');
  whenVisible($('#steps'), function () { $('#steps').classList.add('in'); if (stepsWalker) { walking(stepsWalker, true); setTimeout(function () { walking(stepsWalker, false); paint(stepsWalker, 'drapeau'); }, reduce ? 0 : 3600); } });

  /* ---------- Compteurs ---------- */
  function fmt(n) { return String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, '\u00a0'); }
  function countUp(el, to, dur, suffix) {
    suffix = suffix || '';
    if (reduce) { el.textContent = fmt(to) + suffix; return; }
    var start = null;
    function step(t) {
      if (!start) start = t;
      var p = Math.min(1, (t - start) / dur);
      var e = 1 - Math.pow(1 - p, 3);
      el.textContent = fmt(to * e) + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  whenVisible($('.prix-cards') || $('.plans'), function () {
    $$('.count').forEach(function (c, i) { setTimeout(function () { countUp(c, +c.getAttribute('data-to'), 1100); }, i * 120); });
  });

  /* ---------- Votre metier -> votre formule ---------- */
  var RECO = {
    resto:    { label: 'Restaurant, lolo, food truck', plan: 'Vitrine', price: '990 €', delay: 'Livré en 10 à 14 jours', why: ['Votre carte en ligne, lisible sur téléphone', 'Horaires, itinéraire, bouton Appeler et réservation WhatsApp dès le premier écran', 'Trouvé sur Google quand on tape « restaurant + votre commune »'], opts: [['Menu ou carte imprimée', 'dès 120 €'], ['Avis Google en direct', '90 €'], ['Agent IA qui prend les réservations', 'sur devis']] },
    artisan:  { label: 'Artisan, services à domicile', plan: 'Essentiel', price: '490 €', delay: 'Livré en 7 jours', why: ['Une page : ce que vous faites, votre zone, vos tarifs', 'Bouton Appeler et WhatsApp, itinéraire', 'Formulaire pour recevoir les demandes de devis'], opts: [['Formulaire de devis détaillé', '150 €'], ['Fiche Google Business', '150 €'], ['Carte de visite avec QR code', '60 €']] },
    commerce: { label: 'Commerce, boutique', plan: 'Vitrine', price: '990 €', delay: 'Livré en 10 à 14 jours', why: ['Une page par rayon ou par service, avec galerie', 'Horaires, itinéraire, bouton Appeler', 'Référencement Google complet pour être trouvé dans votre commune'], opts: [['Fiche Google Business', '150 €'], ['Avis Google en direct', '90 €'], ['Flyer avec QR code', 'dès 90 €']] },
    tourisme: { label: 'Location, gîte, activité', plan: 'Vitrine', price: '990 €', delay: 'Livré en 10 à 14 jours', why: ['Galerie photo qui donne envie, une page par logement ou activité', 'Demande de réservation directe, sans commission', 'Trouvé sur Google, avant les plateformes'], opts: [['Version anglaise', '290 €'], ['Prise de réservation en ligne', '190 €'], ['Avis Google en direct', '90 €']] },
    beaute:   { label: 'Coiffeur, beauté, bien-être', plan: 'Essentiel', price: '490 €', delay: 'Livré en 7 jours', extra: '+ 190 € prise de rendez-vous', why: ['Une page : prestations, tarifs, horaires, photos', 'Prise de rendez-vous en ligne, sans décrocher (option 190 €)', 'Bouton Appeler et WhatsApp pour ceux qui préfèrent'], opts: [['Prise de rendez-vous', '190 €'], ['Fiche Google Business', '150 €'], ['Avis Google en direct', '90 €']] },
    sante:    { label: 'Santé, cabinet', plan: 'Signature', price: '1 390 €', delay: 'Livré en 3 semaines', why: ['Prise de rendez-vous en ligne comprise, avec rappels automatiques', 'Une page par soin ou par praticien', 'Référencement avancé pour être trouvé sur chaque recherche'], opts: [['Fiche Google Business', '150 €'], ['Réponses WhatsApp automatiques', 'sur devis']], note: 'Plus simple : Essentiel 490 € + prise de rendez-vous 190 €.' },
    refonte:  { label: 'Un site à refaire', plan: 'Vitrine', price: '990 €', delay: 'Livré en 10 à 14 jours', why: ['On reprend votre contenu et vos photos', 'On garde vos adresses de pages : vous ne perdez pas votre référencement', 'Fini l\'abonnement du constructeur en ligne : le site devient à vous'], opts: [['Fiche Google Business', '150 €'], ['Avis Google en direct', '90 €']] },
    boutique: { label: 'Vendre en ligne', plan: 'Sur mesure', price: 'Sur devis', delay: 'Délai selon le périmètre', why: ['Catalogue, panier, paiement sécurisé, suivi des commandes', 'Base de départ : Vitrine 990 € + option boutique dès 900 €', 'Cahier des charges établi ensemble, au téléphone'], opts: [] }
  };
  var metierBtns = $$('#metiers button'), reco = $('#reco'), plans = $$('.plan');
  function showReco(k) {
    var r = RECO[k];
    metierBtns.forEach(function (b) { b.classList.toggle('on', b.getAttribute('data-m') === k); });
    var msg = 'Bonjour Louis, je suis : ' + r.label + '. Formule conseillée : ' + r.plan + ' (' + r.price + (r.extra ? ' ' + r.extra : '') + '). On peut en parler ?';
    var h = '<div class="r-nono" data-nono="plaque"></div><div><div class="eyebrow">' + r.label + '</div><h3>Il vous faut la formule <em>' + r.plan + '</em>.</h3>';
    h += '<div class="r-price"><b>' + r.price + '</b><span>' + (r.extra ? r.extra + ' · ' : '') + r.delay + '</span></div>';
    h += '<ul>' + r.why.map(function (w) { return '<li>' + w + '</li>'; }).join('') + '</ul></div>';
    h += '<div class="r-side"><div class="eyebrow">' + (r.opts.length ? 'Conseillé en plus, si vous voulez' : 'Comment on avance') + '</div>';
    if (r.opts.length) h += '<ul>' + r.opts.map(function (o) { return '<li>' + o[0] + ' <b>' + o[1] + '</b></li>'; }).join('') + '</ul>';
    else h += '<ul><li>Un appel de 30 minutes pour lister ce qu\'il faut</li><li>Devis ferme sous 48 h</li></ul>';
    h += '<p>' + (r.note ? r.note + ' ' : '') + 'Prix ferme, zéro abonnement, site à vous. Seul frais ensuite : ~25 €/an d\'hébergement.</p></div>';
    h += '<div class="r-cta"><a class="btn btn-wa" href="' + WA + encodeURIComponent(msg) + '" target="_blank" rel="noopener">Envoyer ça à Louis sur WhatsApp</a><a class="btn" href="' + TEL + '">Appeler Louis</a><small>On ajuste ensemble au téléphone, rien n\'est figé.</small></div>';
    reco.innerHTML = h; reco.hidden = false; var re = $('#reco-empty'); if (re) re.hidden = true;
    paint($('.r-nono', reco), 'plaque', r.price === 'Sur devis' ? 'DEVIS' : r.price.replace('\u00a0', ' '));
    reco.style.animation = 'none'; void reco.offsetWidth; reco.style.animation = '';
    plans.forEach(function (p) {
      var me = p.getAttribute('data-plan') === r.plan;
      p.classList.toggle('pick', me); p.classList.toggle('dim', !me);
      var old = $('.pick-badge', p); if (old) old.remove();
      if (me) { var b = document.createElement('div'); b.className = 'pick-badge'; b.textContent = 'Pour vous'; p.appendChild(b); }
    });
    var besoin = $('#besoin');
    if (besoin) $$('option', besoin).forEach(function (o) { if (o.textContent.indexOf(r.plan) > -1) besoin.value = o.value; });
    var top = reco.getBoundingClientRect().top + window.pageYOffset - 100;
    if (window.innerWidth < 980) window.scrollTo({ top: top, behavior: reduce ? 'auto' : 'smooth' });
    var pk = $('.plan.pick'); var pl = $('#plans');
    if (pk && pl && window.innerWidth < 700) setTimeout(function () { pl.scrollTo({ left: pk.offsetLeft - 20, behavior: reduce ? 'auto' : 'smooth' }); }, 400);
  }
  metierBtns.forEach(function (b) { b.addEventListener('click', function () { showReco(b.getAttribute('data-m')); }); });

  /* ---------- Le film : regardez ce qui se passe quand on vous cherche ---------- */
  var bp = $('#bp'), bpScreen = $('#bp-screen'), lvStage = $('#lv-stage'), bpDone = $('#bp-done'), bpCount = $('#bp-count');
  if (bp && bpScreen && lvStage) {
    var LVM = {
      resto:    { lbl: 'Restaurant', q: 'restaurant', ico: '\uD83C\uDF7D', tag: 'Cuisine maison, face à la mer', b2: 'Réserver', msg: 'Bonjour ! Une table pour 4 ce soir vers 20h, c\'est possible ?', rep: 'Avec plaisir, on vous garde la table en terrasse.' },
      artisan:  { lbl: 'Artisan', q: 'climatisation', ico: '\uD83D\uDD27', tag: 'Intervention sur toute la Guadeloupe', b2: 'Devis', msg: 'Bonjour, ma clim ne fait plus de froid. Vous pouvez passer cette semaine ?', rep: 'Oui, je peux passer jeudi matin. Je vous envoie le devis.' },
      commerce: { lbl: 'Boutique', q: 'boutique', ico: '\uD83D\uDECD', tag: 'Ouvert du lundi au samedi', b2: 'Itinéraire', msg: 'Bonjour ! Vous l\'avez encore en stock ? Je passe cet aprem.', rep: 'Oui, je vous le mets de côté.' },
      tourisme: { lbl: 'Location', q: 'gîte', ico: '\uD83C\uDFDD', tag: 'À 5 minutes de la plage', b2: 'Réserver', msg: 'Bonjour, c\'est dispo du 10 au 14 pour 2 personnes ?', rep: 'C\'est libre ! Je vous envoie le lien pour réserver.' },
      beaute:   { lbl: 'Beauté', q: 'coiffeur', ico: '\u2702', tag: 'Sur rendez-vous, sans attente', b2: 'Prendre RDV', msg: 'Bonjour, un créneau demain matin pour une coupe ?', rep: 'Demain 9h30, c\'est noté !' },
      sante:    { lbl: 'Santé', q: 'kiné', ico: '\u2795', tag: 'Prise de rendez-vous en ligne', b2: 'Prendre RDV', msg: 'Bonjour, vous prenez de nouveaux patients ? Un rdv cette semaine ?', rep: 'Oui, mercredi 10h vous irait ?' },
      autre:    { lbl: 'Autre', q: 'commerce', ico: '\u2B50', tag: 'Ce que vous faites, où, quand', b2: 'WhatsApp', msg: 'Bonjour, je viens de voir votre site. Vous êtes ouvert cet aprem ?', rep: 'Oui, jusqu\'à 18h. À tout à l\'heure !' }
    };
    var LVC = { volet: ['#1F4FBF', '#F5C400'], lagon: ['#0E8F8B', '#FFB347'], corail: ['#D1495B', '#F7E7A6'], nuit: ['#1E1E1E', '#E5B83B'] };
    var lv = { name: '', ville: 'Sainte-Anne', m: 'resto', c: 'volet', state: 'start', timers: [] };
    function later(fn, ms) { lv.timers.push(setTimeout(fn, reduce ? 0 : ms)); }
    function clearTimers() { lv.timers.forEach(clearTimeout); lv.timers = []; }
    function setStep(n) { $$('#film-steps li').forEach(function (li) { var s = +li.getAttribute('data-s'); li.classList.toggle('on', s === n); li.classList.toggle('done', s < n); }); }
    function applyColors() { lvStage.style.setProperty('--a', LVC[lv.c][0]); lvStage.style.setProperty('--b', LVC[lv.c][1]); }
    function setBadge(t) { var b = $('#lv-badge'); if (b.textContent !== t) { b.textContent = t; b.classList.remove('pop'); void b.offsetWidth; b.classList.add('pop'); } }
    function renderStart() {
      clearTimers(); lv.state = 'start'; setStep(0);
      var h = '<div class="st"><h4>Nono a faim.</h4><p>Dites-lui qui vous êtes, il va vous chercher sur Google.</p>';
      h += '<label>Le nom de votre commerce<input type="text" id="lv-name" maxlength="22" placeholder="Ex : Chez Ali" autocomplete="off" value="' + lv.name.replace(/"/g, '') + '"></label>';
      h += '<label>Votre commune<input type="text" id="lv-ville" maxlength="24" placeholder="Ex : Sainte-Anne" autocomplete="off" value="' + lv.ville.replace(/"/g, '') + '" style="font-size:16px"></label>';
      h += '<label>Votre activité<div class="chips">' + Object.keys(LVM).map(function (k) { return '<button type="button" data-m="' + k + '"' + (k === lv.m ? ' class="on"' : '') + '>' + LVM[k].lbl + '</button>'; }).join('') + '</div></label>';
      h += '<label>Vos couleurs<div class="dots">' + Object.keys(LVC).map(function (k) { return '<button type="button" data-c="' + k + '" style="--a:' + LVC[k][0] + ';--b:' + LVC[k][1] + '"' + (k === lv.c ? ' class="on"' : '') + ' aria-label="' + k + '"></button>'; }).join('') + '</div></label>';
      h += '<button type="button" class="go" id="lv-go"' + (lv.name.length >= 2 ? '' : ' disabled') + '>Lancer Nono</button></div>';
      bpScreen.innerHTML = h;
      var inp = $('#lv-name'), vil = $('#lv-ville');
      inp.addEventListener('input', function () { lv.name = inp.value.trim(); $('#lv-go').disabled = lv.name.length < 2; });
      vil.addEventListener('input', function () { lv.ville = vil.value.trim() || 'Sainte-Anne'; });
      inp.addEventListener('keydown', function (e) { if (e.key === 'Enter' && lv.name.length >= 2) film(); });
      $$('.st .chips button').forEach(function (b) { b.addEventListener('click', function () { $$('.st .chips button').forEach(function (x) { x.classList.remove('on'); }); b.classList.add('on'); lv.m = b.getAttribute('data-m'); }); });
      $$('.st .dots button').forEach(function (b) { b.addEventListener('click', function () { $$('.st .dots button').forEach(function (x) { x.classList.remove('on'); }); b.classList.add('on'); lv.c = b.getAttribute('data-c'); applyColors(); }); });
      $('#lv-go').addEventListener('click', film);
      bp.classList.remove('ready', 'boom'); bp.hidden = false; bpDone.hidden = true; bpCount.hidden = true; lvStage.classList.remove('boom');
      paint($('#lv-nono'), 'coco'); setBadge('Commencez ici'); applyColors();
    }
    function finger(x, y, tap) {
      var f = $('.finger', bpScreen); if (!f) { f = document.createElement('div'); f.className = 'finger'; f.textContent = '\uD83D\uDC46'; f.style.left = '60%'; f.style.top = '92%'; bpScreen.appendChild(f); void f.offsetWidth; }
      f.style.left = x; f.style.top = y;
      if (tap) later(function () { f.classList.add('tap'); var r = document.createElement('div'); r.className = 'ripple'; r.style.left = 'calc(' + x + ' - 4px)'; r.style.top = 'calc(' + y + ' - 6px)'; bpScreen.appendChild(r); later(function () { f.classList.remove('tap'); r.remove(); }, 400); }, 700);
    }
    function film() {
      clearTimers(); lv.state = 'film';
      var name = lv.name.toUpperCase(), M = LVM[lv.m], ville = lv.ville, q = M.q + ' ' + ville.toLowerCase();
      paint($('#lv-nono'), 'loupe'); setBadge('Nono cherche'); setStep(1); bpCount.hidden = true;
      // scene 1 : Google
      var g = '<div class="sc sc-g on"><div class="g-top"><div class="g-logo"><i>G</i><i>o</i><i>o</i><i>g</i><i>l</i><i>e</i></div></div><div class="g-bar"><span><span id="g-q"></span><span class="cur"></span></span><span>\uD83D\uDD0D</span></div>';
      g += '<div class="g-res first" id="g-first"><b>' + name + '</b><span class="st">\u2605\u2605\u2605\u2605\u2605 <span style="color:#5B5B57;letter-spacing:0">4,9 · 38 avis · ' + ville + '</span></span><small>' + M.tag + ' · Ouvert</small><div class="g-btns"><span>' + M.b2 + '</span><span>Appeler</span><span>Itinéraire</span></div></div>';
      g += '<div class="g-res weak"><b>Le concurrent d\'en face</b><small>Page Facebook · dernier post en 2023 · horaires ?</small></div>';
      g += '<div class="g-res weak"><b>L\'autre, plus loin</b><small>Annuaire · numéro peut-être à jour</small></div></div>';
      bpScreen.innerHTML = g;
      var qEl = $('#g-q'), i = 0;
      (function type() { if (i <= q.length) { qEl.textContent = q.slice(0, i); i++; later(type, 55 + Math.random() * 60); } else { later(function () { $$('.g-res', bpScreen).forEach(function (r, k) { later(function () { r.classList.add('show'); }, k * 220); }); later(function () { setStep(2); setBadge('Il vous trouve'); paint($('#lv-nono'), 'salut'); finger('52%', '34%', true); later(function () { $('#g-first').classList.add('hit'); later(scene2, 500); }, 900); }, 900); }, 300); } })();
      function scene2() {
        var s = '<div class="sc sc-s"><div class="ms"><div class="ms-nav" style="--i:0"><b>' + name + '</b><i></i></div>';
        s += '<div class="ms-hero" style="--i:1"><div class="ico">' + M.ico + '</div><h4>' + name + '</h4><p>' + M.tag + ' · ' + ville + '</p><div class="bt"><span>Appeler</span><span class="w" id="ms-act">' + M.b2 + ' sur WhatsApp</span></div></div>';
        s += '<div class="ms-strip" style="--i:2"><span class="hot">Ouvert maintenant</span><span>Itinéraire 4 min</span></div>';
        s += '<div class="ms-avis" style="--i:3"><b>\u2605\u2605\u2605\u2605\u2605</b> « On y retourne dès demain. »<br><span style="color:#5B5B57">Avis Google</span></div>';
        s += '<div class="ms-map" style="--i:4"></div></div></div>';
        var g1 = $('.sc-g', bpScreen); g1.classList.remove('on'); g1.classList.add('off');
        bpScreen.insertAdjacentHTML('beforeend', s);
        var sc = $('.sc-s', bpScreen); requestAnimationFrame(function () { sc.classList.add('on'); $('.ms', sc).classList.add('on'); });
        later(function () { g1.remove(); }, 500);
        later(function () { finger('66%', '33%', true); later(scene3, 1100); }, 1500);
      }
      function scene3() {
        setStep(3); setBadge('Il vous écrit'); paint($('#lv-nono'), 'tel'); var fg = $('.finger', bpScreen); if (fg) fg.remove();
        var w = '<div class="sc sc-w"><div class="wa-top"><div class="av">\uD83D\uDE0B</div><div><b>Nono, client</b><small>en ligne</small></div></div><div class="wa-body" id="wa-body"><div class="wa-typing"><i></i><i></i><i></i></div></div></div>';
        var s1 = $('.sc-s', bpScreen); s1.classList.remove('on'); s1.classList.add('off');
        bpScreen.insertAdjacentHTML('beforeend', w);
        var sc = $('.sc-w', bpScreen); requestAnimationFrame(function () { sc.classList.add('on'); });
        later(function () { s1.remove(); }, 500);
        later(function () {
          var body = $('#wa-body'); body.innerHTML = '<div class="wa-b">' + M.msg + '<time>19:42</time></div>';
          later(function () { bpScreen.insertAdjacentHTML('beforeend', '<div class="wa-notif"><i>\uD83D\uDD14</i><div><b>Nouveau client pour ' + name + '</b>Depuis votre site, en 42 secondes.</div></div>'); bpCount.hidden = false; }, 700);
          later(function () { body.insertAdjacentHTML('beforeend', '<div class="wa-b me">' + M.rep + '<time>19:43</time></div>'); }, 1800);
          later(function () { body.insertAdjacentHTML('beforeend', '<div class="wa-b">Parfait, à tout à l\'heure \uD83D\uDE4F<time>19:43</time></div>'); lv.state = 'site'; bp.classList.add('ready'); paint($('#lv-nono'), 'pointe'); setBadge('Touchez le téléphone'); bpScreen.insertAdjacentHTML('beforeend', '<div class="film-touch" style="position:absolute;left:8px;right:8px;bottom:8px">Ce client, il est à vous. Touchez</div>'); }, 3000);
        }, 1400);
      }
      var wa = $('#lv-wa');
      if (wa) wa.href = WA + encodeURIComponent('Bonjour Louis, je veux l\'aperçu gratuit de mon site. Mon commerce : ' + lv.name + ', ' + ville + ' (' + M.lbl.toLowerCase() + '). J\'ai vu Nono sur votre site.');
    }
    function boom() {
      if (lv.state !== 'site') return;
      lv.state = 'boom'; clearTimers();
      bp.classList.remove('ready'); bp.classList.add('boom'); lvStage.classList.add('boom'); bpCount.hidden = true;
      var cols = [LVC[lv.c][0], LVC[lv.c][1], '#F5C400', '#1F4FBF', '#F7F5EF', '#25D366'];
      if (!reduce) for (var i = 0; i < 42; i++) {
        var d = document.createElement('span'); d.className = 'confetti';
        var ang = Math.random() * Math.PI * 2, dist = 120 + Math.random() * 220;
        d.style.setProperty('--x', Math.cos(ang) * dist + 'px'); d.style.setProperty('--y', Math.sin(ang) * dist - 40 + 'px'); d.style.setProperty('--r', (Math.random() * 720 - 360) + 'deg');
        d.style.background = cols[i % cols.length]; d.style.width = d.style.height = (8 + Math.random() * 10) + 'px'; d.style.animationDelay = (Math.random() * 120) + 'ms';
        lvStage.appendChild(d); setTimeout(function (el) { el.remove(); }, 1400, d);
      }
      setTimeout(function () { bp.hidden = true; bpDone.hidden = false; paint($('#lv-nono'), 'drapeau'); setBadge('À vous de jouer'); }, reduce ? 0 : 520);
    }
    bp.addEventListener('click', function () { if (bp.classList.contains('ready')) boom(); });
    var again = $('#lv-again'); if (again) again.addEventListener('click', renderStart);
    renderStart();
  }

  /* ---------- Realisations : apercus en direct ---------- */
  var works = $$('.work[data-url]');
  var canIframe = window.innerWidth >= 760 && !reduce;
  function sizeIframe(w) {
    var f = $('iframe', w), view = $('.view', w);
    if (!f || !view) return;
    var s = view.clientWidth / 1100;
    f.style.transform = 'scale(' + s + ')';
    f.dataset.scale = s;
    f.style.height = Math.ceil(view.clientHeight / s + 400) + 'px';
  }
  if (canIframe) {
    works.forEach(function (w) {
      whenVisible(w, function () {
        var view = $('.view', w);
        var f = document.createElement('iframe');
        f.setAttribute('title', 'Aperçu du site ' + w.getAttribute('data-url'));
        f.setAttribute('loading', 'lazy');
        f.setAttribute('tabindex', '-1');
        f.setAttribute('aria-hidden', 'true');
        f.src = w.getAttribute('data-url');
        f.addEventListener('load', function () { w.classList.add('loaded'); sizeIframe(w); });
        view.insertBefore(f, view.firstChild);
        sizeIframe(w);
        w.addEventListener('mouseenter', function () { var s = f.dataset.scale || 1; f.style.transform = 'scale(' + s + ') translateY(-360px)'; });
        w.addEventListener('mouseleave', function () { var s = f.dataset.scale || 1; f.style.transform = 'scale(' + s + ')'; });
      }, '200px 0px 200px 0px');
    });
    window.addEventListener('resize', function () { works.forEach(sizeIframe); });
  }

  /* ---------- Le vrai cout ---------- */
  var COST = {
    nova: function (y) { return 990 + 25 * y; },
    nocode: function (y) { return 35 * 12 * y; },
    agence: function (y) { return 3500 + 50 * 12 * y; }
  };
  var segBtns = $$('.seg button'), coutYears = $('#cout-years'), coutSaving = $('#cout-saving'), badgeOk = $('#badge-ok');
  var coutStarted = false, curYears = 5;
  function renderCout(y) {
    curYears = y;
    var vals = { nova: COST.nova(y), nocode: COST.nocode(y), agence: COST.agence(y) };
    var max = Math.max(vals.nova, vals.nocode, vals.agence);
    Object.keys(vals).forEach(function (k) {
      var bar = $('.bar[data-key="' + k + '"] i'), tot = $('.total[data-total="' + k + '"]');
      if (bar) bar.style.width = Math.max(4, vals[k] / max * 100) + '%';
      if (k === 'nova') { var bn = $('#bar-nono'); if (bn) { bn.style.left = Math.max(4, vals[k] / max * 100) + '%'; var bb = $('.bob', bn); if (bb) { bb.classList.remove('jump'); void bb.getBoundingClientRect(); bb.classList.add('jump'); } } }
      if (tot) countUp(tot, vals[k], 800, ' €');
    });
    if (coutYears) coutYears.textContent = y + (y > 1 ? ' ans' : ' an');
    var diffA = vals.agence - vals.nova, diffN = vals.nocode - vals.nova;
    if (coutSaving) {
      if (diffN > 0) coutSaving.textContent = 'Vous gardez ' + fmt(diffA) + ' € face à une agence, et ' + fmt(diffN) + ' € face à un constructeur en ligne.';
      else coutSaving.textContent = 'Vous gardez ' + fmt(diffA) + ' € face à une agence. Dès la 3e année, vous passez aussi devant le constructeur en ligne.';
    }
    if (badgeOk) { badgeOk.textContent = diffN > 0 ? 'Remboursé, site à vous' : 'Site à vous'; badgeOk.classList.add('on'); }
  }
  segBtns.forEach(function (b) {
    b.addEventListener('click', function () {
      segBtns.forEach(function (x) { x.classList.remove('on'); x.setAttribute('aria-selected', 'false'); });
      b.classList.add('on'); b.setAttribute('aria-selected', 'true');
      renderCout(+b.getAttribute('data-years'));
    });
  });
  whenVisible($('.cout-card'), function () { if (!coutStarted) { coutStarted = true; renderCout(curYears); } });

  /* ---------- A la carte : onglets ---------- */
  var tabs = $$('.tabs button'), panels = $$('.panels .panel');
  tabs.forEach(function (t) {
    t.addEventListener('click', function () {
      tabs.forEach(function (x) { x.classList.remove('on'); x.setAttribute('aria-selected', 'false'); });
      t.classList.add('on'); t.setAttribute('aria-selected', 'true');
      panels.forEach(function (p) { p.classList.toggle('on', p.getAttribute('data-panel') === t.getAttribute('data-tab')); });
      var tn = $('#tabs-nono');
      if (tn) { paint(tn, { fonc: 'marteau', ia: 'robot', visi: 'loupe', print: 'courrier', abo: 'coco', apres: 'tel' }[t.getAttribute('data-tab')] || 'salut'); tn.classList.remove('pop'); void tn.offsetWidth; tn.classList.add('pop'); }
    });
  });
  var tn0 = $('#tabs-nono'); if (tn0) paint(tn0, 'marteau');

  /* ---------- Louis repond ---------- */
  var helper = $('#helper'), hBtn = $('#helper-btn'), hPanel = $('#helper-panel'), hBody = $('#helper-body'), hChips = $('#helper-chips'), hClose = $('#helper-close');
  var ANSWERS = [
    ['Combien ça coûte ?', 'Trois formules : 490 € pour une page, 990 € pour un site complet, 1 390 € pour un site qui prend les rendez-vous tout seul. Prix ferme, payé une fois, aucun abonnement. Le seul frais ensuite : environ 25 € par an d\'hébergement, à votre nom.'],
    ['C\'est long ?', '7 jours pour un site une page à partir de notre rendez-vous, 10 à 14 jours pour un site complet. Le délai est écrit sur le devis, et un retard de ma faute vous donne droit à une remise.'],
    ['Je n\'ai ni logo ni photos', 'Aucun souci, la plupart de mes clients démarrent comme ça. Je vous guide pour prendre les photos avec votre téléphone, j\'écris les textes avec vous, et si besoin je vous fais un logo simple et propre.'],
    ['Je peux le modifier moi-même ?', 'Un site codé se modifie par moi : une photo ou un horaire à changer, ça coûte quelques dizaines d\'euros et c\'est fait vite. Si quelque chose change tout le temps (carte du jour, dispos), j\'ajoute un petit espace où vous le faites vous-même.'],
    ['Vous venez sur place ?', 'Oui, en Guadeloupe je me déplace pour le cadrage et la remise. Pour la Martinique, Saint-Martin et Saint-Barth, tout se fait très bien par téléphone et WhatsApp, et je viens si le projet le justifie.'],
    ['Le site est vraiment à moi ?', 'Oui, à 100 %. Domaine et hébergement à votre nom, fichiers du site remis sur clé ou par lien. Vous pouvez partir demain avec, sans me demander la permission.']
  ];
  function addMsg(txt, me) {
    if (!hBody) return;
    var d = document.createElement('div');
    d.className = 'hp-msg' + (me ? ' me' : '');
    d.textContent = txt;
    hBody.appendChild(d);
    hBody.scrollTop = hBody.scrollHeight;
  }
  function openHelper() {
    hPanel.hidden = false; hBtn.setAttribute('aria-expanded', 'true');
    if (!hBody.childElementCount) addMsg('Bonjour, je suis Louis. Posez-moi une question, ou écrivez-moi directement sur WhatsApp : je réponds dans la journée.');
  }
  function closeHelper() { hPanel.hidden = true; hBtn.setAttribute('aria-expanded', 'false'); }
  if (helper && hBtn && hPanel) {
    ANSWERS.forEach(function (a) {
      var b = document.createElement('button'); b.type = 'button'; b.textContent = a[0];
      b.addEventListener('click', function () { addMsg(a[0], true); setTimeout(function () { addMsg(a[1]); }, reduce ? 0 : 350); });
      hChips.appendChild(b);
    });
    hBtn.addEventListener('click', function () { hPanel.hidden ? openHelper() : closeHelper(); });
    hClose.addEventListener('click', closeHelper);
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !hPanel.hidden) closeHelper(); });
  }

  /* ---------- Formulaire ---------- */
  var form = $('#form'), ile = $('#ile'), villeWrap = $('#ville-wrap'), ville = $('#ville');
  if (ile && villeWrap) {
    ile.addEventListener('change', function () {
      var autre = ile.value === 'Autre';
      villeWrap.hidden = !autre;
      if (autre) { ville.required = true; ville.focus(); } else { ville.required = false; ville.value = ''; }
    });
  }
  var MAILBOX = '<svg class="mailbox" viewBox="0 0 160 200" aria-hidden="true"><path d="M78 110v80" stroke="#111" stroke-width="8" stroke-linecap="round"/><rect x="18" y="40" width="124" height="74" rx="30" fill="#1F4FBF" stroke="#111" stroke-width="5"/><rect x="26" y="48" width="108" height="58" rx="24" fill="none" stroke="#F7F5EF" stroke-width="5"/><rect x="52" y="66" width="56" height="10" rx="4" fill="#111"/><g class="mb-flag"><path d="M132 74v-38" stroke="#111" stroke-width="6" stroke-linecap="round"/><path d="M134 36h26l-6 10 6 10h-26z" fill="#F5C400" stroke="#111" stroke-width="4" stroke-linejoin="round"/></g><text x="80" y="96" text-anchor="middle" font-family="Anton, Impact, sans-serif" font-size="14" fill="#F7F5EF">LOUIS</text></svg>';
  var ENV = '<svg class="env" viewBox="0 0 60 44" aria-hidden="true"><rect x="2" y="2" width="56" height="40" rx="5" fill="#fff" stroke="#111" stroke-width="4"/><path d="M2 6l28 20L58 6" fill="none" stroke="#111" stroke-width="4" stroke-linejoin="round"/><rect x="40" y="6" width="14" height="12" fill="#F5C400" stroke="#111" stroke-width="2"/></svg>';
  var formHTML = form ? form.innerHTML : '';
  function bindForm() {
    ile = $('#ile'); villeWrap = $('#ville-wrap'); ville = $('#ville');
    if (ile) ile.addEventListener('change', function () { var a = ile.value === 'Autre'; villeWrap.hidden = !a; ville.required = a; if (a) ville.focus(); });
  }
  function showDone(prenom) {
    form.classList.remove('sending');
    form.innerHTML = '<div class="form-done">' +
      '<div class="done-nono" data-nono="tel"></div>' +
      '<div><div class="eyebrow">Bien reçu' + (prenom ? ', ' + prenom : '') + '</div><b class="sign">C\'est envoyé.</b>' +
      '<p>Je vous rappelle dans la journée, en semaine. Trente minutes, et vous repartez avec un prix ferme sous 48 h.</p>' +
      '<ol><li>Je vous rappelle</li><li>On cadre en 30 minutes</li><li>Devis ferme sous 48 h</li></ol>' +
      '<div class="form-done-cta"><a class="btn btn-wa" href="' + WA + encodeURIComponent('Bonjour Louis, je viens de remplir le formulaire sur votre site.') + '" target="_blank" rel="noopener">Si c\'est urgent : WhatsApp</a><button type="button" class="link-reset" id="form-reset">Envoyer une autre demande</button></div></div></div>';
    $('.done-nono', form).innerHTML = nono('tel');
    $('#form-reset').addEventListener('click', function () { form.innerHTML = formHTML; form.classList.remove('is-done'); form.style.minHeight = ''; bindForm(); $('input', form).focus(); });
    form.classList.add('is-done');
  }
  if (form && window.fetch) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var btn = $('button[type="submit"]', form);
      var old = btn.textContent, prenom = (form.prenom && form.prenom.value || '').trim();
      btn.disabled = true; btn.textContent = 'Envoi en cours…';
      var data = new FormData(form);
      var stage = document.createElement('div');
      stage.className = 'stage';
      stage.innerHTML = '<div class="stage-sky"><span></span><span></span><span></span></div><div class="stage-ground"></div><div class="stage-nono">' + nono('courrier') + '</div>' + ENV + MAILBOX + '<div class="stage-stamp">Reçu !</div>';
      form.appendChild(stage); form.classList.add('sending');
      var t0 = Date.now(), minWait = reduce ? 0 : 3700;
      form.style.minHeight = form.offsetHeight + 'px';
      fetch('https://formsubmit.co/ajax/contact@studionovalem.fr', { method: 'POST', headers: { 'Accept': 'application/json' }, body: data })
        .then(function (r) { return r.json(); })
        .then(function () { setTimeout(function () { showDone(prenom); }, Math.max(0, minWait - (Date.now() - t0))); })
        .catch(function () { stage.remove(); form.classList.remove('sending'); btn.disabled = false; btn.textContent = old; form.submit(); });
    });
  }
})();

/* ---------- Animations premium : mots, tilt, aimant ---------- */
(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var touch = window.matchMedia('(hover: none)').matches;
  function $$(s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); }

  /* Révélation mot à mot des grands titres (uniquement les titres sans balise enfant) */
  var heads = $$('h2.sign').filter(function (h) { return h.children.length === 0; });
  if (!reduce && 'IntersectionObserver' in window) {
    heads.forEach(function (h) {
      var words = h.textContent.trim().split(/\s+/);
      h.innerHTML = words.map(function (w, i) {
        return '<span class="w"><i style="--wi:' + i + '">' + w + '</i></span>';
      }).join(' ');
      h.classList.add('sw');
    });
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.4 });
    heads.forEach(function (h) { io.observe(h); });
  }

  /* Tilt 3D léger sur les cartes marquées data-tilt */
  if (!reduce && !touch) {
    $$('[data-tilt]').forEach(function (card) {
      var raf = null;
      card.addEventListener('mousemove', function (e) {
        if (raf) return;
        raf = requestAnimationFrame(function () {
          var r = card.getBoundingClientRect();
          var x = (e.clientX - r.left) / r.width - 0.5;
          var y = (e.clientY - r.top) / r.height - 0.5;
          card.style.transform = 'perspective(800px) rotateY(' + (x * 5) + 'deg) rotateX(' + (y * -5) + 'deg) translateY(-3px)';
          raf = null;
        });
      });
      card.addEventListener('mouseleave', function () {
        card.style.transition = 'transform 400ms cubic-bezier(0.16,1,0.3,1), box-shadow 200ms';
        card.style.transform = '';
        setTimeout(function () { card.style.transition = ''; }, 420);
      });
    });
  }

  /* Boutons aimantés : les gros boutons suivent doucement la souris */
  if (!reduce && !touch) {
    $$('.btn-xl').forEach(function (b) {
      b.addEventListener('mousemove', function (e) {
        var r = b.getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width - 0.5;
        var y = (e.clientY - r.top) / r.height - 0.5;
        b.style.transform = 'translate(' + (x * 6) + 'px,' + (y * 5) + 'px)';
      });
      b.addEventListener('mouseleave', function () { b.style.transform = ''; });
    });
  }
})();

/* ---------- La poignee de main + ambiance du heros ---------- */
(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var touch = window.matchMedia('(hover: none)').matches;

  /* Etoiles de la nuit */
  var starsBox = document.querySelector('.pacte-stars');
  if (starsBox) {
    var frag = document.createDocumentFragment();
    for (var i = 0; i < 46; i++) {
      var s = document.createElement('i');
      s.style.left = (Math.random() * 100) + '%';
      s.style.top = (Math.random() * 100) + '%';
      s.style.setProperty('--td', (Math.random() * 3.4).toFixed(2) + 's');
      if (Math.random() < 0.18) s.className = 'big';
      frag.appendChild(s);
    }
    starsBox.appendChild(frag);
  }

  /* Progression au defilement : les bras se rejoignent, l'etincelle s'allume */
  var pacte = document.getElementById('pacte');
  if (pacte && !reduce) {
    var ticking = false;
    function update() {
      ticking = false;
      var r = pacte.getBoundingClientRect();
      var vh = window.innerHeight;
      var p = (vh - r.top) / (vh * 0.85);
      p = Math.max(0, Math.min(1, p));
      pacte.style.setProperty('--hs', p.toFixed(3));
      pacte.classList.toggle('lit', p > 0.93);
    }
    window.addEventListener('scroll', function () {
      if (!ticking) { ticking = true; requestAnimationFrame(update); }
    }, { passive: true });
    update();
  } else if (pacte) {
    pacte.classList.add('lit');
  }

  /* Lucioles dans le heros */
  var heroScene = document.querySelector('.hero .scene');
  var hero = document.querySelector('.hero');
  if (hero && !reduce) {
    var luc = document.createElement('div');
    luc.className = 'lucioles';
    luc.setAttribute('aria-hidden', 'true');
    for (var j = 0; j < 9; j++) {
      var f = document.createElement('i');
      f.style.left = (8 + Math.random() * 84) + '%';
      f.style.top = (20 + Math.random() * 70) + '%';
      f.style.setProperty('--lt', (7 + Math.random() * 6).toFixed(1) + 's');
      f.style.setProperty('--ld', (Math.random() * 6).toFixed(1) + 's');
      f.style.setProperty('--lx', ((Math.random() - 0.5) * 90).toFixed(0) + 'px');
      f.style.setProperty('--ly', (-(30 + Math.random() * 70)).toFixed(0) + 'px');
      luc.appendChild(f);
    }
    hero.style.position = 'relative';
    hero.appendChild(luc);
  }

  /* Parallaxe souris sur la devanture */
  if (heroScene && !reduce && !touch) {
    var layers = [
      [heroScene.querySelector('.sf-facade'), 6],
      [heroScene.querySelector('.sf-sign'), 14],
      [heroScene.querySelector('.sf-phone'), 22],
      [document.getElementById('nono-hero'), 30]
    ];
    var raf2 = null;
    hero.addEventListener('mousemove', function (e) {
      if (raf2) return;
      raf2 = requestAnimationFrame(function () {
        var r = hero.getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width - 0.5;
        var y = (e.clientY - r.top) / r.height - 0.5;
        layers.forEach(function (l) {
          if (l[0]) l[0].style.transform = 'translate(' + (x * l[1]) + 'px,' + (y * l[1] * 0.6) + 'px)';
        });
        raf2 = null;
      });
    });
    hero.addEventListener('mouseleave', function () {
      layers.forEach(function (l) { if (l[0]) l[0].style.transform = ''; });
    });
  }
})();
