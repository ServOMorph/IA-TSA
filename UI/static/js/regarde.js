/* Activité 5 : jeu dyadique "Regarde où je regarde" — balayage + touche unique. */
(function () {
  const PREFIX = "iatsa.regarde.";
  const ORDER_2 = ["gauche", "droite"];
  const ORDER_4 = ["haut", "droite", "bas", "gauche"];

  const PALIERS = {
    1: { zones: 2, vitesse: 1600, pause: 500, memoire: false, inversion: false },
    2: { zones: 2, vitesse: 800, pause: 400, memoire: false, inversion: false },
    3: { zones: 4, vitesse: 900, pause: 400, memoire: false, inversion: false },
    4: { zones: 4, vitesse: 900, pause: 400, memoire: true, inversion: false },
    5: { zones: 4, vitesse: 900, pause: 400, memoire: true, inversion: true },
  };

  const ADULT_KEY = "Enter";
  const JEUNE_KEY = "Space";

  function loadNum(key, fallback) {
    const raw = localStorage.getItem(PREFIX + key);
    if (raw === null) return fallback;
    const v = +raw;
    return Number.isFinite(v) ? v : fallback;
  }

  function loadBool(key, fallback) {
    const v = localStorage.getItem(PREFIX + key);
    return v === null ? fallback : v === "true";
  }

  function saveVal(key, value) {
    localStorage.setItem(PREFIX + key, String(value));
  }

  const state = {
    palier: Math.min(5, Math.max(1, loadNum("palier", 1))),
    zones: loadNum("zones", 2),
    vitesse: loadNum("vitesse", 1600),
    pause: loadNum("pause", 500),
    antirebond: loadNum("antirebond", 300),
    memoire: loadBool("memoire", false),
    inversion: loadBool("inversion", false),
    designatedZone: null,
  };

  let zoneEls = {};
  let currentOrder = state.zones === 4 ? ORDER_4 : ORDER_2;
  let sweepIndex = 0;
  let sweepTimer = null;
  const lastKeyTime = {};

  let statusEl;

  function updateStatus() {
    const zonesTxt = state.zones + " zones";
    const roleTxt = state.inversion
      ? "jeune désigne, adulte valide"
      : "adulte désigne, jeune valide";
    statusEl.textContent = "Palier " + state.palier + " · " + zonesTxt + " · " + roleTxt;
  }

  function setZonesVisibility() {
    ["haut", "droite", "bas", "gauche"].forEach(function (pos) {
      const el = zoneEls[pos];
      el.hidden = currentOrder.indexOf(pos) === -1;
    });
  }

  function clearDesignation() {
    if (state.designatedZone) {
      const el = zoneEls[state.designatedZone];
      if (el) el.classList.remove("designated", "memory-hide");
    }
    state.designatedZone = null;
  }

  function restartSweep() {
    clearTimeout(sweepTimer);
    currentOrder = state.zones === 4 ? ORDER_4 : ORDER_2;
    setZonesVisibility();
    sweepIndex = 0;
    render();
    scheduleTick();
  }

  function render() {
    currentOrder.forEach(function (pos, i) {
      zoneEls[pos].classList.toggle("sweep-active", i === sweepIndex);
    });
  }

  function scheduleTick() {
    const isLast = sweepIndex === currentOrder.length - 1;
    const delay = state.vitesse + (isLast ? state.pause : 0);
    sweepTimer = setTimeout(function () {
      sweepIndex = (sweepIndex + 1) % currentOrder.length;
      render();
      scheduleTick();
    }, delay);
  }

  function match(zone) {
    zone.classList.add("match");
    zone.classList.remove("designated", "memory-hide");
    ActivityCore.playTone(660, 500);
    ActivityCore.logEvent("match", "palier-" + state.palier);
    setTimeout(function () { zone.classList.remove("match"); }, 700);
    state.designatedZone = null;
    updateStatus();
  }

  function designate(zone) {
    if (state.designatedZone && state.designatedZone !== zone.dataset.pos) {
      const prev = zoneEls[state.designatedZone];
      if (prev) prev.classList.remove("designated", "memory-hide");
    }
    state.designatedZone = zone.dataset.pos;
    zone.classList.add("designated");
    zone.classList.remove("memory-hide");
    ActivityCore.playTone(+zone.dataset.tone || 392, 300);
    ActivityCore.logEvent("designation", zone.dataset.pos);
    if (state.memoire) {
      const pos = zone.dataset.pos;
      setTimeout(function () {
        if (state.designatedZone === pos) zone.classList.add("memory-hide");
      }, 900);
    }
    updateStatus();
  }

  function onKeyDown(e) {
    if (e.code !== ADULT_KEY && e.code !== JEUNE_KEY) return;
    e.preventDefault();
    const now = Date.now();
    if (now - (lastKeyTime[e.code] || 0) < state.antirebond) return;
    lastKeyTime[e.code] = now;
    const activeZone = zoneEls[currentOrder[sweepIndex]];
    if (!activeZone) return;
    const designatorKey = state.inversion ? JEUNE_KEY : ADULT_KEY;
    const validatorKey = state.inversion ? ADULT_KEY : JEUNE_KEY;
    if (e.code === designatorKey) {
      designate(activeZone);
    } else if (e.code === validatorKey) {
      if (state.designatedZone && state.designatedZone === activeZone.dataset.pos) match(activeZone);
    }
  }

  function applyPalier(n) {
    const preset = PALIERS[n];
    if (!preset) return;
    state.palier = n;
    state.zones = preset.zones;
    state.vitesse = preset.vitesse;
    state.pause = preset.pause;
    state.memoire = preset.memoire;
    state.inversion = preset.inversion;
    saveVal("palier", n);
    saveVal("zones", state.zones);
    saveVal("vitesse", state.vitesse);
    saveVal("pause", state.pause);
    saveVal("memoire", state.memoire);
    saveVal("inversion", state.inversion);
    clearDesignation();
    syncControls();
    restartSweep();
    updateStatus();
    ActivityCore.logEvent("palier", String(n));
  }

  function syncControls() {
    document.getElementById("set-vitesse").value = state.vitesse;
    document.getElementById("set-pause").value = state.pause;
    document.getElementById("set-antirebond").value = state.antirebond;
    document.getElementById("set-memoire").checked = state.memoire;
    document.getElementById("set-inversion").checked = state.inversion;
    document.querySelectorAll("#palier-picker .visual-opt").forEach(function (b) {
      b.classList.toggle("active", +b.dataset.palier === state.palier);
    });
    document.querySelectorAll("#zones-picker .visual-opt").forEach(function (b) {
      b.classList.toggle("active", +b.dataset.zones === state.zones);
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    zoneEls = {
      haut: document.querySelector('.regarde-zone[data-pos="haut"]'),
      droite: document.querySelector('.regarde-zone[data-pos="droite"]'),
      bas: document.querySelector('.regarde-zone[data-pos="bas"]'),
      gauche: document.querySelector('.regarde-zone[data-pos="gauche"]'),
    };
    statusEl = document.getElementById("regarde-status");

    currentOrder = state.zones === 4 ? ORDER_4 : ORDER_2;
    setZonesVisibility();
    syncControls();
    updateStatus();
    render();
    scheduleTick();

    document.querySelectorAll("#palier-picker .visual-opt").forEach(function (btn) {
      btn.addEventListener("click", function () {
        btn.blur();
        applyPalier(+btn.dataset.palier);
      });
    });

    document.querySelectorAll("#zones-picker .visual-opt").forEach(function (btn) {
      btn.addEventListener("click", function () {
        btn.blur();
        state.zones = +btn.dataset.zones;
        saveVal("zones", state.zones);
        clearDesignation();
        syncControls();
        restartSweep();
      });
    });

    document.getElementById("set-vitesse").addEventListener("input", function (e) {
      state.vitesse = +e.target.value;
      saveVal("vitesse", state.vitesse);
    });

    document.getElementById("set-pause").addEventListener("input", function (e) {
      state.pause = +e.target.value;
      saveVal("pause", state.pause);
    });

    document.getElementById("set-antirebond").addEventListener("input", function (e) {
      state.antirebond = +e.target.value;
      saveVal("antirebond", state.antirebond);
    });

    document.getElementById("set-memoire").addEventListener("change", function (e) {
      state.memoire = e.target.checked;
      saveVal("memoire", state.memoire);
      clearDesignation();
      updateStatus();
    });

    document.getElementById("set-inversion").addEventListener("change", function (e) {
      state.inversion = e.target.checked;
      saveVal("inversion", state.inversion);
      clearDesignation();
      updateStatus();
    });

    document.addEventListener("keydown", onKeyDown);
  });
})();
