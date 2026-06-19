const TimerActivity = (function () {
  const RADIUS = 130;
  const CIRCUMFERENCE = 2 * Math.PI * RADIUS;
  const DURATION_KEY = "iatsa.timer.duration";
  const VISUAL_KEY = "iatsa.timer.visual";
  const BLOC_COUNT = 30;
  const MIN_SECS = 10;
  const VISUALS = ["anneau", "blocs", "barre", "soleil", "couleur"];

  let duration = Math.max(MIN_SECS, +(localStorage.getItem(DURATION_KEY) || 300));
  let remaining = duration;
  let running = false;
  let tickId = null;
  let pickerMin = Math.floor(duration / 60);
  let pickerSec = duration % 60;
  let currentVisual = localStorage.getItem(VISUAL_KEY) || "anneau";
  let blocCells = [];

  let ring, timeEls, barreEl, soleilOrb, couleurFill, btnStart, btnReset, pickerStage;

  function fmt(secs) {
    return Math.floor(secs / 60) + ":" + String(secs % 60).padStart(2, "0");
  }

  function updateAllTime() {
    var t = fmt(remaining);
    timeEls.forEach(function (el) { el.textContent = t; });
  }

  function updateVisual() {
    var progress = duration > 0 ? remaining / duration : 0;
    if (currentVisual === "anneau")  updateAnneau(progress);
    if (currentVisual === "blocs")   updateBlocs(progress);
    if (currentVisual === "barre")   updateBarre(progress);
    if (currentVisual === "soleil")  updateSoleil(progress);
    if (currentVisual === "couleur") updateCouleur(progress);
  }

  function updateAnneau(p) {
    ring.style.strokeDashoffset = CIRCUMFERENCE * (1 - p);
  }

  function updateBlocs(p) {
    var active = Math.round(p * BLOC_COUNT);
    blocCells.forEach(function (cell, i) {
      cell.classList.toggle("bloc-on", i < active);
    });
  }

  function updateBarre(p) {
    barreEl.style.width = (p * 100) + "%";
  }

  function updateSoleil(p) {
    var top = 5 + (1 - p) * 80;
    soleilOrb.style.top = top + "%";
    soleilOrb.style.opacity = p < 0.15 ? (p / 0.15) : 1;
  }

  function updateCouleur(p) {
    couleurFill.style.clipPath = "inset(" + ((1 - p) * 100) + "% 0 0 0)";
  }

  function refreshAll() {
    updateAllTime();
    updateVisual();
  }

  function showPicker(v) {
    pickerStage.style.display = v ? "flex" : "none";
  }

  function onEnd() {
    timeEls.forEach(function (el) { el.classList.add("timer-time-end"); });
    ring.classList.add("timer-ring-end");
    if (!ActivityCore.settings.calme && ActivityCore.settings.son) {
      ActivityCore.playTone(660, 600);
      setTimeout(function () { ActivityCore.playTone(880, 600); }, 350);
      setTimeout(function () { ActivityCore.playTone(1100, 800); }, 700);
    }
    setTimeout(function () {
      timeEls.forEach(function (el) { el.classList.remove("timer-time-end"); });
      ring.classList.remove("timer-ring-end");
    }, 2000);
    btnStart.textContent = "Recommencer";
    showPicker(true);
  }

  function tick() {
    if (!running) return;
    remaining = Math.max(0, remaining - 1);
    refreshAll();
    if (remaining <= 0) {
      running = false;
      clearInterval(tickId);
      onEnd();
    }
  }

  function start() {
    if (remaining <= 0) { remaining = duration; refreshAll(); }
    running = true;
    tickId = setInterval(tick, 1000);
    btnStart.textContent = "Pause";
    showPicker(false);
  }

  function pause() {
    running = false;
    clearInterval(tickId);
    btnStart.textContent = "Continuer";
    showPicker(true);
  }

  function reset() {
    running = false;
    clearInterval(tickId);
    remaining = duration;
    refreshAll();
    btnStart.textContent = "Démarrer";
    showPicker(true);
  }

  function updatePickerLabels() {
    document.getElementById("disp-min-label").textContent = pickerMin + " min";
    document.getElementById("disp-sec-label").textContent = String(pickerSec).padStart(2, "0") + " sec";
  }

  function clampPicker() {
    if (pickerMin < 0) pickerMin = 0;
    if (pickerMin > 99) pickerMin = 99;
    if (pickerSec < 0) pickerSec = 0;
    if (pickerSec > 59) pickerSec = 59;
    if (pickerMin === 0 && pickerSec < MIN_SECS) pickerSec = MIN_SECS;
  }

  function applyPicker() {
    duration = Math.max(MIN_SECS, pickerMin * 60 + pickerSec);
    localStorage.setItem(DURATION_KEY, duration);
    remaining = duration;
    refreshAll();
    btnStart.textContent = "Démarrer";
  }

  function switchVisual(name) {
    VISUALS.forEach(function (v) {
      var el = document.getElementById("visual-" + v);
      if (el) el.hidden = v !== name;
    });
    currentVisual = name;
    localStorage.setItem(VISUAL_KEY, name);
    refreshAll();
  }

  function initBlocs() {
    var grid = document.getElementById("blocs-grid");
    for (var i = 0; i < BLOC_COUNT; i++) {
      var cell = document.createElement("div");
      cell.className = "bloc-cell bloc-on";
      grid.appendChild(cell);
      blocCells.push(cell);
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    ring = document.getElementById("timer-ring");
    ring.style.strokeDasharray = CIRCUMFERENCE;
    timeEls = Array.from(document.querySelectorAll(".timer-time-el"));
    barreEl = document.getElementById("barre-fill");
    soleilOrb = document.getElementById("soleil-orb");
    couleurFill = document.getElementById("couleur-fill");
    btnStart = document.getElementById("btn-timer-start");
    btnReset = document.getElementById("btn-timer-reset");
    pickerStage = document.getElementById("picker-stage");

    initBlocs();

    switchVisual(currentVisual);

    updatePickerLabels();
    refreshAll();
    showPicker(true);

    document.querySelectorAll(".visual-opt").forEach(function (btn) {
      btn.classList.toggle("active", btn.dataset.visual === currentVisual);
      btn.addEventListener("click", function () {
        switchVisual(this.dataset.visual);
        document.querySelectorAll(".visual-opt").forEach(function (b) {
          b.classList.toggle("active", b.dataset.visual === currentVisual);
        });
      });
    });

    document.getElementById("btn-min-p").addEventListener("click", function () {
      pickerMin++; clampPicker(); updatePickerLabels(); applyPicker();
    });
    document.getElementById("btn-min-m").addEventListener("click", function () {
      pickerMin--; clampPicker(); updatePickerLabels(); applyPicker();
    });
    document.getElementById("btn-sec-p").addEventListener("click", function () {
      pickerSec += 5;
      if (pickerSec > 59) { pickerSec = 0; pickerMin++; }
      clampPicker(); updatePickerLabels(); applyPicker();
    });
    document.getElementById("btn-sec-m").addEventListener("click", function () {
      pickerSec -= 5;
      if (pickerSec < 0) { pickerSec = 55; pickerMin = Math.max(0, pickerMin - 1); }
      clampPicker(); updatePickerLabels(); applyPicker();
    });

    btnStart.addEventListener("click", function () { if (running) pause(); else start(); });
    btnReset.addEventListener("click", reset);
  });
})();
