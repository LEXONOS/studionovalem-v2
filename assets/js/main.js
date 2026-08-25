/* Tropical Dream — main.js (vanilla, sans dépendance) */
(function () {
  "use strict";

  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => Array.from(c.querySelectorAll(s));

  /* ---------- Coordonnées (une seule source de vérité) ---------- */
  window.TD = window.TD || {};
  TD.tel = "+590690702529";
  TD.telAffiche = "+590 690 70 25 29";
  TD.email = "tropicaldream971@gmail.com";
  TD.wa = "https://wa.me/590690702529";

  /* ---------- Images : repli automatique ----------
     Si la photo locale n'est pas encore dans assets/img/, on affiche
     l'image d'attente indiquée dans data-fallback. Une fois la vraie
     photo déposée avec le bon nom de fichier, elle prend le dessus. */
  function initImageFallback() {
    $$("img[data-fallback]").forEach((img) => {
      const fb = img.getAttribute("data-fallback");
      const apply = () => {
        if (img.dataset.fbDone) return;
        img.dataset.fbDone = "1";
        img.src = fb;
        const a = img.closest("a[data-lightbox]");
        if (a) a.dataset.src = fb;
      };
      img.addEventListener("error", apply, { once: true });
      if (img.complete && img.naturalWidth === 0) apply();
    });
  }

  /* ---------- Header ---------- */
  function initHeader() {
    const header = $(".site-header");
    if (!header) return;
    const light = header.dataset.light === "true";
    const onScroll = () => {
      header.classList.toggle("is-solid", window.scrollY > 40 || light);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });

    const toggle = $(".nav-toggle");
    if (toggle) {
      toggle.addEventListener("click", () => {
        const open = document.body.classList.toggle("nav-open");
        toggle.setAttribute("aria-expanded", String(open));
        document.body.style.overflow = open ? "hidden" : "";
      });
      $$(".nav a").forEach((a) =>
        a.addEventListener("click", () => {
          document.body.classList.remove("nav-open");
          document.body.style.overflow = "";
        })
      );
    }

    // Page courante
    const here = location.pathname.split("/").pop() || "index.html";
    $$(".nav a").forEach((a) => {
      const href = a.getAttribute("href");
      if (href === here || (here === "" && href === "index.html")) a.setAttribute("aria-current", "page");
    });
  }

  /* ---------- Bouton flottant masqué tant que le hero est visible ---------- */
  function initFab() {
    const hero = $(".hero");
    if (!hero || !("IntersectionObserver" in window)) return;
    const io = new IntersectionObserver((en) => {
      document.body.classList.toggle("hero-visible", en[0].isIntersecting && en[0].intersectionRatio > 0.15);
    }, { threshold: [0, 0.15, 0.5] });
    io.observe(hero);
  }

  /* ---------- Apparitions ---------- */
  function initReveal() {
    const els = $$(".reveal");
    if (!("IntersectionObserver" in window) || !els.length) {
      els.forEach((e) => e.classList.add("is-in"));
      return;
    }
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((en) => {
          if (en.isIntersecting) {
            en.target.classList.add("is-in");
            io.unobserve(en.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -6% 0px" }
    );
    els.forEach((e) => io.observe(e));
  }

  /* ---------- Lightbox ---------- */
  function initLightbox() {
    const links = $$("a[data-lightbox]");
    if (!links.length) return;
    const lb = document.createElement("div");
    lb.className = "lightbox";
    lb.setAttribute("role", "dialog");
    lb.setAttribute("aria-label", "Galerie photos");
    lb.innerHTML =
      '<button class="lb-close" aria-label="Fermer">×</button>' +
      '<button class="lb-prev" aria-label="Photo précédente">‹</button>' +
      '<img alt="">' +
      '<button class="lb-next" aria-label="Photo suivante">›</button>' +
      "<figcaption></figcaption>";
    document.body.appendChild(lb);
    const img = $("img", lb), cap = $("figcaption", lb);
    let i = 0;
    const src = (a) => a.dataset.src || a.getAttribute("href");
    const show = (n) => {
      i = (n + links.length) % links.length;
      img.src = src(links[i]);
      img.alt = links[i].dataset.caption || "";
      cap.textContent = (links[i].dataset.caption || "") + "  ·  " + (i + 1) + " / " + links.length;
    };
    const open = (n) => { show(n); lb.classList.add("is-open"); document.body.style.overflow = "hidden"; };
    const close = () => { lb.classList.remove("is-open"); document.body.style.overflow = ""; };
    links.forEach((a, n) => a.addEventListener("click", (e) => { e.preventDefault(); open(n); }));
    $(".lb-close", lb).addEventListener("click", close);
    $(".lb-prev", lb).addEventListener("click", () => show(i - 1));
    $(".lb-next", lb).addEventListener("click", () => show(i + 1));
    lb.addEventListener("click", (e) => { if (e.target === lb) close(); });
    document.addEventListener("keydown", (e) => {
      if (!lb.classList.contains("is-open")) return;
      if (e.key === "Escape") close();
      if (e.key === "ArrowLeft") show(i - 1);
      if (e.key === "ArrowRight") show(i + 1);
    });
  }

  /* ---------- Tiroir de réservation ---------- */
  function initDrawer() {
    const drawer = $(".drawer");
    if (!drawer) return;
    const openers = $$("[data-open-resa]");
    const close = () => { document.body.classList.remove("drawer-open"); document.body.style.overflow = ""; };
    const open = (tab) => {
      document.body.classList.add("drawer-open");
      document.body.style.overflow = "hidden";
      if (tab && window.TD.selectTab) window.TD.selectTab(drawer, tab);
      const first = $("input, select, button", $(".guichet-panel.is-active", drawer) || drawer);
      if (first) setTimeout(() => first.focus(), 350);
    };
    openers.forEach((b) => b.addEventListener("click", (e) => { e.preventDefault(); open(b.dataset.openResa); }));
    $(".drawer-close", drawer)?.addEventListener("click", close);
    $(".drawer-backdrop")?.addEventListener("click", close);
    document.addEventListener("keydown", (e) => { if (e.key === "Escape") close(); });
  }

  /* ---------- Toast ---------- */
  TD.toast = function (msg) {
    let t = $(".toast");
    if (!t) { t = document.createElement("div"); t.className = "toast"; document.body.appendChild(t); }
    t.textContent = msg;
    t.classList.add("is-on");
    clearTimeout(t._h);
    t._h = setTimeout(() => t.classList.remove("is-on"), 2600);
  };

  /* ---------- Formulaire de contact (sans serveur) ----------
     Le message part par WhatsApp ou par e-mail depuis l'appareil du visiteur. */
  function initContactForm() {
    const form = $("#form-contact");
    if (!form) return;
    const build = () => {
      const d = new FormData(form);
      return (
        "Bonjour Tropical Dream,\n\n" +
        "Nom : " + (d.get("nom") || "") + "\n" +
        "Téléphone : " + (d.get("tel") || "") + "\n" +
        "E-mail : " + (d.get("email") || "") + "\n" +
        "Sujet : " + (d.get("sujet") || "") + "\n\n" +
        (d.get("message") || "")
      );
    };
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      if (!form.reportValidity()) return;
      const msg = build();
      const via = e.submitter?.dataset.via || "email";
      if (via === "whatsapp") {
        window.open(TD.wa + "?text=" + encodeURIComponent(msg), "_blank", "noopener");
      } else {
        location.href = "mailto:" + TD.email + "?subject=" + encodeURIComponent("Contact via le site — " + (new FormData(form).get("sujet") || "")) + "&body=" + encodeURIComponent(msg);
      }
      TD.toast("Votre message s'ouvre dans votre application. Il ne reste qu'à l'envoyer.");
    });
  }

  /* ---------- Année du footer ---------- */
  function initYear() { $$("[data-year]").forEach((e) => (e.textContent = new Date().getFullYear())); }

  document.addEventListener("DOMContentLoaded", () => {
    initImageFallback();
    initHeader();
    initFab();
    initReveal();
    initLightbox();
    initDrawer();
    initContactForm();
    initYear();
  });
})();
