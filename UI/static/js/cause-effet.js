/* Activité 1 : cause-effet pur. Toute action -> une seule réaction. */
(function () {
  const stage = document.getElementById("stage");
  const palette = ["#A5C9CA", "#F6C177", "#9CCFA1", "#C9A5C7", "#7DA1A2", "#E8A0A0"];
  let lastTrigger = 0;

  function rand(arr) { return arr[Math.floor(Math.random() * arr.length)]; }

  function burst(x, y) {
    const now = Date.now();
    if (now - lastTrigger < 120) return; // anti-rebond, évite le flood switch
    lastTrigger = now;

    const size = 80 + ActivityCore.settings.taille * 50;
    const el = document.createElement("div");
    el.className = "ce-burst";
    el.style.width = size + "px";
    el.style.height = size + "px";
    el.style.left = (x - size / 2) + "px";
    el.style.top = (y - size / 2) + "px";
    el.style.background = rand(palette);
    stage.appendChild(el);
    el.addEventListener("animationend", function () { el.remove(); });

    const tones = [392, 440, 494, 523, 587];
    ActivityCore.playTone(rand(tones), 380);
  }

  function fromCenter() {
    const r = stage.getBoundingClientRect();
    const jitter = (Math.random() - 0.5) * Math.min(r.width, r.height) * 0.4;
    burst(r.width / 2 + jitter, r.height / 2 + jitter * 0.6);
  }

  stage.addEventListener("pointerdown", function (e) {
    if (ActivityCore.isControl(e.target)) return;
    burst(e.clientX, e.clientY);
  });

  document.addEventListener("keydown", function (e) {
    if (e.repeat) return;
    if (e.key === "Escape" || e.key === "Tab") return;
    const panel = document.getElementById("panel");
    if (panel && !panel.hidden) return;
    fromCenter();
  });
})();
