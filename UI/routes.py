import io
import os
import json
import wave
import threading
import markdown
from html import escape
from datetime import datetime
from flask import (
    Blueprint, render_template, send_from_directory, abort,
    request, redirect, url_for, Response,
)

bp = Blueprint("main", __name__)

DOCS_ROOT = os.path.join(os.path.dirname(__file__), "..", "docs")

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
RETOURS_FILE = os.path.join(DATA_DIR, "retours_terrain.json")

VOICES_DIR = os.path.join(os.path.dirname(__file__), "..", "voices")
PIPER_MODEL = os.path.join(VOICES_DIR, "fr_FR-siwis-medium.onnx")
TTS_MAX_CHARS = 300

_piper_voice = None
_piper_lock = threading.Lock()

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
    {
        "slug": "ecrire-ecoute",
        "endpoint": "activite_ecoute",
        "name": "Écris et écoute",
        "desc": "L'apprenant tape un mot ou une suite de lettres, puis appuie sur "
                "Entrée ou clique sur le bouton : le mot est lu à voix haute.",
        "profil": "Association mot écrit / mot entendu, motricité fine au clavier",
    },
]

ENGAGEMENTS = ["engage", "neutre", "retrait"]


def _build_docs_tree(path, rel=""):
    entries = []
    for name in sorted(os.listdir(path)):
        full = os.path.join(path, name)
        rel_path = f"{rel}/{name}" if rel else name
        if os.path.isdir(full):
            entries.append({
                "type": "dir",
                "name": name,
                "children": _build_docs_tree(full, rel_path),
            })
        elif os.path.isfile(full):
            stat = os.stat(full)
            entries.append({
                "type": "file",
                "name": name,
                "path": rel_path,
                "ext": os.path.splitext(name)[1].lower().lstrip(".") or "—",
                "size": _human_size(stat.st_size),
            })
    return entries


def _list_docs_tree():
    root = os.path.abspath(DOCS_ROOT)
    if not os.path.isdir(root):
        return []
    return _build_docs_tree(root)


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


def _get_piper_voice():
    global _piper_voice
    if _piper_voice is None:
        with _piper_lock:
            if _piper_voice is None:
                from piper import PiperVoice
                _piper_voice = PiperVoice.load(PIPER_MODEL)
    return _piper_voice


@bp.route("/")
@bp.route("/recherches/docs")
@bp.route("/recherches/docs/<path:filename>")
def docs_view(filename=None):
    root = os.path.abspath(DOCS_ROOT)
    tree = _list_docs_tree()
    content_html = None
    current = None

    if filename:
        full = os.path.abspath(os.path.join(root, filename))
        if not full.startswith(root) or not os.path.isfile(full):
            abort(404)
        with open(full, "r", encoding="utf-8") as f:
            raw = f.read()
        if full.lower().endswith(".md"):
            content_html = markdown.markdown(
                raw, extensions=["extra", "sane_lists", "toc"]
            )
        else:
            content_html = f"<pre>{escape(raw)}</pre>"
        current = filename.replace(os.sep, "/")

    return render_template(
        "docs.html", tree=tree, content=content_html,
        current=current, active="docs",
    )


@bp.route("/recherches/docs-raw/<path:filename>")
def docs_raw(filename):
    root = os.path.abspath(DOCS_ROOT)
    full = os.path.abspath(os.path.join(root, filename))
    if not full.startswith(root):
        abort(403)
    return send_from_directory(root, filename)


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


@bp.route("/activites/ecrire-ecoute")
def activite_ecoute():
    return render_template("activite_ecoute.html")


@bp.route("/api/tts", methods=["POST"])
def tts():
    data = request.get_json(silent=True) or {}
    text = data.get("text", "").strip()[:TTS_MAX_CHARS]
    if not text:
        abort(400)
    if not os.path.isfile(PIPER_MODEL):
        abort(503)

    voice = _get_piper_voice()
    buf = io.BytesIO()
    with wave.open(buf, "wb") as wav_file:
        header_set = False
        for chunk in voice.synthesize(text):
            if not header_set:
                wav_file.setnchannels(chunk.sample_channels)
                wav_file.setsampwidth(chunk.sample_width)
                wav_file.setframerate(chunk.sample_rate)
                header_set = True
            wav_file.writeframes(chunk.audio_int16_bytes)

    return Response(buf.getvalue(), mimetype="audio/wav")


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
