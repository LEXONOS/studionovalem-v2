/* Tropical Dream — reservation.js
   Gère le guichet (hero + tiroir) et la page Réservation.
   Aucun serveur : la demande est composée puis envoyée par WhatsApp ou e-mail
   depuis l'appareil du visiteur. Christophe et Astrid confirment ensuite. */
(function () {
  "use strict";
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => Array.from(c.querySelectorAll(s));
  window.TD = window.TD || {};

  const fmtDate = (v) => {
    if (!v) return "";
    const d = new Date(v + "T12:00:00");
    return isNaN(d) ? v : d.toLocaleDateString("fr-FR", { weekday: "short", day: "numeric", month: "long", year: "numeric" });
  };
  const nuits = (a, b) => {
    if (!a || !b) return 0;
    const n = Math.round((new Date(b) - new Date(a)) / 86400000);
    return n > 0 ? n : 0;
  };
  const val = (root, name) => {
    const el = root.querySelector('[name="' + name + '"]');
    if (!el) return "";
    if (el.type === "checkbox") return el.checked ? "oui" : "";
    return (el.value || "").trim();
  };
  const chips = (root, name) => $$('.chip[data-group="' + name + '"][aria-pressed="true"]', root).map((c) => c.textContent.trim());

  /* ---------- Compose le message selon l'onglet ---------- */
  function buildMessage(root, tab) {
    const p = $('.guichet-panel[data-tab="' + tab + '"], .resa-panel[data-tab="' + tab + '"]', root) || root;
    const L = [];
    if (tab === "gite") {
      const a = val(p, "arrivee"), d = val(p, "depart"), n = nuits(a, d);
      L.push("🏡 Demande de réservation — Gîte");
      L.push("Hébergement : " + (val(p, "gite") || "à conseiller"));
      L.push("Arrivée : " + (fmtDate(a) || "—"));
      L.push("Départ : " + (fmtDate(d) || "—") + (n ? " (" + n + " nuit" + (n > 1 ? "s" : "") + ")" : ""));
      L.push("Voyageurs : " + (val(p, "adultes") || "?") + " adulte(s)" + (val(p, "enfants") ? ", " + val(p, "enfants") + " enfant(s)" : ""));
      const opts = chips(p, "options");
      if (opts.length) L.push("Souhaits : " + opts.join(", "));
    } else if (tab === "vehicule") {
      L.push("🚗 Demande de location — Véhicule");
      L.push("Catégorie : " + (val(p, "categorie") || "à conseiller"));
      L.push("Du : " + (fmtDate(val(p, "debut")) || "—") + (val(p, "heure_debut") ? " à " + val(p, "heure_debut") : ""));
      L.push("Au : " + (fmtDate(val(p, "fin")) || "—") + (val(p, "heure_fin") ? " à " + val(p, "heure_fin") : ""));
      L.push("Remise du véhicule : " + (val(p, "livraison") || "au gîte"));
      if (val(p, "vol")) L.push("N° de vol : " + val(p, "vol"));
      const opts = chips(p, "options");
      if (opts.length) L.push("Options : " + opts.join(", "));
    } else if (tab === "bienetre") {
      L.push("🛁 Demande de réservation — Bien-être");
      L.push("Prestation : " + (val(p, "formule") || "à conseiller"));
      L.push("Date souhaitée : " + (fmtDate(val(p, "date")) || "—") + (val(p, "creneau") ? " · " + val(p, "creneau") : ""));
      L.push("Personnes : " + (val(p, "personnes") || "2"));
      const opts = chips(p, "options");
      if (opts.length) L.push("Envies : " + opts.join(", "));
    } else if (tab === "evenement") {
      L.push("🎉 Demande — Événement");
      L.push("Type : " + (val(p, "type") || "—"));
      L.push("Date : " + (fmtDate(val(p, "date")) || "—"));
      L.push("Invités : " + (val(p, "invites") || "?"));
    }
    const nom = val(root, "nom") || val(p, "nom");
    const tel = val(root, "tel") || val(p, "tel");
    const msg = val(root, "message") || val(p, "message");
    if (nom || tel) L.push("", "Contact : " + [nom, tel].filter(Boolean).join(" · "));
    if (msg) L.push("", "Message : " + msg);
    return "Bonjour Tropical Dream,\n\n" + L.join("\n") + "\n\nMerci de me confirmer la disponibilité et le tarif.";
  }

  function send(root, tab, via) {
    const msg = buildMessage(root, tab);
    const subject = {
      gite: "Réservation gîte", vehicule: "Location de véhicule", bienetre: "Réservation bien-être", evenement: "Demande événement",
    }[tab] || "Demande";
    if (via === "email") {
      location.href = "mailto:" + TD.email + "?subject=" + encodeURIComponent(subject + " — via le site") + "&body=" + encodeURIComponent(msg);
    } else {
      window.open(TD.wa + "?text=" + encodeURIComponent(msg), "_blank", "noopener");
    }
    if (TD.toast) TD.toast("Votre demande s'ouvre dans " + (via === "email" ? "votre messagerie" : "WhatsApp") + ". Il ne reste qu'à l'envoyer.");
  }

  /* ---------- Onglets ---------- */
  TD.selectTab = function (root, tab) {
    $$('[role="tab"]', root).forEach((b) => b.setAttribute("aria-selected", String(b.dataset.tab === tab)));
    $$(".guichet-panel, .resa-panel", root).forEach((p) => p.classList.toggle("is-active", p.dataset.tab === tab));
    root.dataset.activeTab = tab;
    refreshRecap(root);
  };

  function refreshRecap(root) {
    const pre = $("[data-recap]", root);
    if (!pre) return;
    pre.textContent = buildMessage(root, root.dataset.activeTab || "gite");
  }

  function initRoot(root) {
    const first = $('[role="tab"]', root);
    const wanted = root.dataset.defaultTab || (first && first.dataset.tab) || "gite";
    TD.selectTab(root, wanted);
    $$('[role="tab"]', root).forEach((b) => b.addEventListener("click", () => TD.selectTab(root, b.dataset.tab)));
    $$(".chip", root).forEach((c) => c.addEventListener("click", () => {
      c.setAttribute("aria-pressed", c.getAttribute("aria-pressed") === "true" ? "false" : "true");
      refreshRecap(root);
    }));
    root.addEventListener("input", () => refreshRecap(root));
    root.addEventListener("change", () => refreshRecap(root));
    $$("[data-send]", root).forEach((b) => b.addEventListener("click", (e) => {
      e.preventDefault();
      const panel = $(".guichet-panel.is-active, .resa-panel.is-active", root);
      const req = panel ? $$("[required]", panel) : [];
      for (const f of req) { if (!f.reportValidity()) return; }
      send(root, root.dataset.activeTab, b.dataset.send);
    }));

    // Dates cohérentes : min = aujourd'hui, départ > arrivée
    const today = new Date().toISOString().slice(0, 10);
    $$('input[type="date"]', root).forEach((i) => { if (!i.min) i.min = today; });
    const pairs = [["arrivee", "depart"], ["debut", "fin"]];
    pairs.forEach(([a, b]) => {
      $$('[name="' + a + '"]', root).forEach((ia) => {
        const ib = ia.closest(".guichet-panel, .resa-panel")?.querySelector('[name="' + b + '"]');
        if (!ib) return;
        ia.addEventListener("change", () => {
          ib.min = ia.value || today;
          if (ib.value && ib.value <= ia.value) ib.value = "";
        });
      });
    });
    refreshRecap(root);
  }

  /* ---------- Pré-sélection depuis l'URL (?resa=vehicule) ---------- */
  document.addEventListener("DOMContentLoaded", () => {
    $$("[data-resa-root]").forEach(initRoot);
    const q = new URLSearchParams(location.search).get("resa");
    const page = $("#resa[data-resa-root]");
    if (q && page) TD.selectTab(page, q);
    const pre = new URLSearchParams(location.search).get("gite");
    if (pre && page) { const s = $('[name="gite"]', page); if (s) { s.value = pre; refreshRecap(page); } }
  });
})();
