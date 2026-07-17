/* Socle commun aux activités IA-TSA : réglages persistés, son, mode calme. */
const ActivityCore = (function () {
  const slug = document.body.dataset.activity || "default";
  const KEY = "iatsa.activity." + slug;
  const defaults = { son: true, intensite: 3, taille: 3, calme: false };

  function load() {
    try {
      return Object.assign({}, defaults, JSON.parse(localStorage.getItem(KEY)) || {});
    } catch (e) {
      return Object.assign({}, defaults);
    }
  }

  const settings = load();
  let audioCtx = null;
  const listeners = [];

  function save() {
    localStorage.setItem(KEY, JSON.stringify(settings));
  }

  function ctx() {
    if (!audioCtx) {
      const C = window.AudioContext || window.webkitAudioContext;
      if (C) audioCtx = new C();
    }
    return audioCtx;
  }

  function playTone(freq, durationMs) {
    if (!settings.son || settings.calme) return;
    const c = ctx();
    if (!c) return;
    if (c.state === "suspended") c.resume();
    const dur = (durationMs || 320) / 1000;
    const o = c.createOscillator();
    const g = c.createGain();
    o.type = "sine";
    o.frequency.value = freq;
    o.connect(g);
    g.connect(c.destination);
    const now = c.currentTime;
    const vol = 0.04 + settings.intensite * 0.025;
    g.gain.setValueAtTime(0.0001, now);
    g.gain.exponentialRampToValueAtTime(vol, now + 0.02);
    g.gain.exponentialRampToValueAtTime(0.0001, now + dur);
    o.start(now);
    o.stop(now + dur + 0.05);
  }

  function applyCalme() {
    document.body.classList.toggle("calme", settings.calme);
  }

  function notify() {
    listeners.forEach(function (fn) { fn(settings); });
  }

  function onChange(fn) {
    listeners.push(fn);
  }

  function initControls() {
    const panel = document.getElementById("panel");
    const btnSettings = document.getElementById("btn-settings");
    const btnClose = document.getElementById("panel-close");
    const btnCalme = document.getElementById("btn-calme");
    const son = document.getElementById("set-son");
    const intensite = document.getElementById("set-intensite");
    const taille = document.getElementById("set-taille");
    const calme = document.getElementById("set-calme");

    son.checked = settings.son;
    intensite.value = settings.intensite;
    taille.value = settings.taille;
    calme.checked = settings.calme;
    btnCalme.setAttribute("aria-pressed", String(settings.calme));
    applyCalme();

    btnSettings.addEventListener("click", function () { panel.hidden = !panel.hidden; });
    btnClose.addEventListener("click", function () { panel.hidden = true; });

    son.addEventListener("change", function () { settings.son = son.checked; save(); notify(); });
    intensite.addEventListener("input", function () { settings.intensite = +intensite.value; save(); notify(); });
    taille.addEventListener("input", function () { settings.taille = +taille.value; save(); notify(); });

    function setCalme(v) {
      settings.calme = v;
      calme.checked = v;
      btnCalme.setAttribute("aria-pressed", String(v));
      applyCalme();
      save();
      notify();
    }
    calme.addEventListener("change", function () { setCalme(calme.checked); });
    btnCalme.addEventListener("click", function () { setCalme(!settings.calme); });
  }

  // Empêche les contrôles d'interférer avec l'aire d'activité.
  function isControl(el) {
    return el.closest(".activity-controls") || el.closest(".activity-panel");
  }

  function logEvent(event, detail) {
    try {
      fetch("/api/log-event", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        keepalive: true,
        body: JSON.stringify({ activite: slug, event: event, detail: detail }),
      });
    } catch (e) {}
  }

  function logExit() {
    if (!navigator.sendBeacon) return;
    var blob = new Blob(
      [JSON.stringify({ activite: slug, event: "sortie", detail: null })],
      { type: "application/json" }
    );
    navigator.sendBeacon("/api/log-event", blob);
  }

  document.addEventListener("DOMContentLoaded", initControls);
  document.addEventListener("DOMContentLoaded", function () { logEvent("ouverture", null); });
  document.addEventListener("pagehide", logExit);

  return {
    settings: settings,
    playTone: playTone,
    onChange: onChange,
    isControl: isControl,
    logEvent: logEvent,
  };
})();
