import os
import json
from datetime import datetime
from flask import (
    Blueprint, render_template, send_from_directory, abort,
    request, redirect, url_for,
)

bp = Blueprint("main", __name__)

DOCS_WEB_PATH = os.path.join(
    os.path.dirname(__file__), "..", "docs", "web"
)

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
RETOURS_FILE = os.path.join(DATA_DIR, "retours_terrain.json")

ACTIVITES = [
    {
        "slug": "cause-effet",
        "endpoint": "activite_cause_effet",
        "name": "Touche → ça réagit",
        "desc": "Cause-effet pur : toute action déclenche une seule réaction "
                "visuelle et sonore. Écran calme, rien d'autre ne bouge.",
        "profil": "Très grave moteur, attention conjointe, découverte du lien causal",
    },
    {
        "slug": "choix-a-deux",
        "endpoint": "activite_choix",
        "name": "Choix entre deux",
        "desc": "Deux grandes zones. L'apprenant indique un choix, l'accompagnant "
                "valide → la zone choisie s'anime. Proto-CAA par le choix.",
        "profil": "Vers la décision et la communication par le choix",
    },
    {
        "slug": "timer",
        "endpoint": "activite_timer",
        "name": "Timer visuel",
        "desc": "Sablier circulaire qui se vide progressivement. Signal doux en fin "
                "de temps. Durée réglable (1 à 15 min). Matérialise l'attente.",
        "profil": "Structuration du temps, gestion de l'anxiété liée aux transitions",
    },
]

ENGAGEMENTS = ["engage", "neutre", "retrait"]


def _list_docs_web():
    path = os.path.abspath(DOCS_WEB_PATH)
    if not os.path.isdir(path):
        return []
    entries = []
    for name in sorted(os.listdir(path)):
        full = os.path.join(path, name)
        if os.path.isfile(full):
            stat = os.stat(full)
            entries.append({
                "name": name,
                "ext": os.path.splitext(name)[1].lower().lstrip(".") or "—",
                "size": _human_size(stat.st_size),
            })
    return entries


def _human_size(n):
    for unit in ("o", "Ko", "Mo", "Go"):
        if n < 1024:
            return f"{n:.0f} {unit}"
        n /= 1024
    return f"{n:.1f} To"


def _load_retours():
    if not os.path.isfile(RETOURS_FILE):
        return []
    try:
        with open(RETOURS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def _save_retours(retours):
    os.makedirs(os.path.abspath(DATA_DIR), exist_ok=True)
    with open(RETOURS_FILE, "w", encoding="utf-8") as f:
        json.dump(retours, f, ensure_ascii=False, indent=2)


def _activite_name(slug):
    for a in ACTIVITES:
        if a["slug"] == slug:
            return a["name"]
    return slug


@bp.route("/")
@bp.route("/recherches/docs-web")
def docs_web():
    files = _list_docs_web()
    return render_template("docs_web.html", files=files, active="docs_web")


@bp.route("/docs/web/<path:filename>")
def serve_doc(filename):
    path = os.path.abspath(DOCS_WEB_PATH)
    full = os.path.join(path, filename)
    if not full.startswith(path):
        abort(403)
    return send_from_directory(path, filename)


@bp.route("/activites")
def activites():
    return render_template("activites.html", activites=ACTIVITES, active="activites")


@bp.route("/activites/cause-effet")
def activite_cause_effet():
    return render_template("activite_cause_effet.html")


@bp.route("/activites/choix-a-deux")
def activite_choix():
    return render_template("activite_choix.html")


@bp.route("/activites/timer")
def activite_timer():
    return render_template("activite_timer.html")


@bp.route("/retour-terrain", methods=["GET"])
def retour_terrain():
    retours = _load_retours()
    for r in retours:
        r["activite_nom"] = _activite_name(r.get("activite", ""))
    retours = list(reversed(retours))
    return render_template(
        "retour_terrain.html",
        retours=retours,
        activites=ACTIVITES,
        active="retour_terrain",
    )


@bp.route("/retour-terrain", methods=["POST"])
def retour_terrain_save():
    activite = request.form.get("activite", "").strip()
    engagement = request.form.get("engagement", "").strip()
    reglages = request.form.get("reglages", "").strip()
    note = request.form.get("note", "").strip()

    if engagement not in ENGAGEMENTS:
        engagement = "neutre"

    retours = _load_retours()
    retours.append({
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "activite": activite,
        "engagement": engagement,
        "reglages": reglages,
        "note": note,
    })
    _save_retours(retours)
    return redirect(url_for("main.retour_terrain"))
