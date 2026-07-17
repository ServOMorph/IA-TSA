/* Activité 3 : choix entre deux. Une zone activée s'anime, l'autre s'estompe. */
(function () {
  const zones = Array.prototype.slice.call(document.querySelectorAll(".choix-zone"));
  const grid = document.querySelector(".choix-grid");
  let busy = false;

  function applyTaille() {
    const scale = 0.6 + ActivityCore.settings.taille * 0.18;
    document.querySelectorAll(".choix-shape").forEach(function (s) {
      s.style.transform = "scale(" + scale + ")";
    });
  }
  applyTaille();
  ActivityCore.onChange(applyTaille);

  function activate(zone) {
    if (busy || !zone) return;
    busy = true;
    const other = zones.filter(function (z) { return z !== zone; })[0];
    zone.classList.add("active");
    if (other) other.classList.add("dim");
    ActivityCore.playTone(+zone.dataset.tone || 440, 460);
    ActivityCore.logEvent("choix", zone === zones[0] ? "gauche" : "droite");
    setTimeout(function () {
      zone.classList.remove("active");
      if (other) other.classList.remove("dim");
      busy = false;
    }, 900);
  }

  zones.forEach(function (z) {
    z.addEventListener("pointerdown", function (e) {
      e.preventDefault();
      activate(z);
    });
  });

  document.addEventListener("keydown", function (e) {
    const panel = document.getElementById("panel");
    if (panel && !panel.hidden) return;
    if (e.repeat) return;
    if (e.key === "ArrowLeft" || e.key === "1" || e.key === "q") activate(zones[0]);
    else if (e.key === "ArrowRight" || e.key === "2" || e.key === "p") activate(zones[1]);
  });
})();
