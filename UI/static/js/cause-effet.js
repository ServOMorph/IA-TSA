/* Activité 1 : cause-effet pur. Toute action -> une seule réaction. */
(function () {
  const stage = document.getElementById("stage");
  const palette = ["#A5C9CA", "#F6C177", "#9CCFA1", "#C9A5C7", "#7DA1A2", "#E8A0A0"];
  let lastTrigger = 0;

  const effects = {
    espace: { shape: "ce-burst-circle", tones: [392, 440, 494, 523, 587] },
    entree: { shape: "ce-burst-square", tones: [262, 294, 330, 349] },
    ctrl:   { shape: "ce-burst-diamond", tones: [523, 587, 659, 698, 784] }
  };

  function rand(arr) { return arr[Math.floor(Math.random() * arr.length)]; }

  function burst(x, y, kind) {
    const now = Date.now();
    if (now - lastTrigger < 120) return; // anti-rebond, évite le flood switch
    lastTrigger = now;

    const effect = effects[kind] || effects.espace;
    const size = 80 + ActivityCore.settings.taille * 50;
    const el = document.createElement("div");
    el.className = "ce-burst " + effect.shape;
    el.style.width = size + "px";
    el.style.height = size + "px";
    el.style.left = (x - size / 2) + "px";
    el.style.top = (y - size / 2) + "px";
    el.style.background = rand(palette);
    stage.appendChild(el);
    el.addEventListener("animationend", function () { el.remove(); });

    ActivityCore.playTone(rand(effect.tones), 380);
  }

  function fromCenter(kind) {
    const r = stage.getBoundingClientRect();
    const jitter = (Math.random() - 0.5) * Math.min(r.width, r.height) * 0.4;
    burst(r.width / 2 + jitter, r.height / 2 + jitter * 0.6, kind);
  }

  stage.addEventListener("pointerdown", function (e) {
    if (ActivityCore.isControl(e.target)) return;
    burst(e.clientX, e.clientY, "espace");
  });

  document.addEventListener("keydown", function (e) {
    if (e.repeat) return;
    if (e.key === "Escape" || e.key === "Tab") return;
    const panel = document.getElementById("panel");
    if (panel && !panel.hidden) return;

    let kind;
    if (e.key === " " || e.key === "Spacebar") kind = "espace";
    else if (e.key === "Enter") kind = "entree";
    else if (e.key === "Control") kind = "ctrl";
    else return;

    fromCenter(kind);
  });
})();
