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
    request, redirect, url_for, Response, session,
)

bp = Blueprint("main", __name__)

DOCS_ROOT = os.path.join(os.path.dirname(__file__), "..", "docs")

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
RETOURS_FILE = os.path.join(DATA_DIR, "retours_terrain.json")
USERS_FILE = os.path.join(DATA_DIR, "users.json")
LOGS_DIR = os.path.join(DATA_DIR, "logs")

UTILISATEUR_ENDPOINTS = (
    "main.utilisateur",
    "main.utilisateur_supprimer",
    "main.utilisateur_renommer",
)

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
    {
        "slug": "regarde-ou-je-regarde",
        "endpoint": "activite_regarde",
        "name": "Regarde où je regarde",
        "desc": "Jeu à deux : l'accompagnant désigne une zone, l'apprenant valide au "
                "bon moment pendant le balayage automatique. 5 paliers, contacteur "
                "une touche.",
        "profil": "Jeu dyadique accompagnant/apprenant, attention conjointe, alternance des rôles",
    },
]

ENGAGEMENTS = ["engage", "neutre", "retrait"]

THEORIE = {
    "cause-effet": {
        "cible": "Établir le lien de causalité « mon action produit un effet »",
        "fondement": [
            "Le numérique convient au TSA pour des raisons structurelles : prévisibilité de la "
            "machine, absence de charge sociale et de jugement, réaction constante et immédiate "
            "(projet_pedagogique.md §2, ancrage HAS 2026).",
            "Le mapping fixe action → effet est la piste la mieux soutenue par la littérature : "
            "une correspondance stable entre action et réaction réduit l'anxiété et facilite "
            "l'anticipation. Trois touches actives seulement (Espace, Entrée, Ctrl), toute autre "
            "touche est ignorée pour éviter le bruit d'interaction.",
            "La variation progressive du stimulus a été explicitement écartée : les enfants TSA "
            "présentent une habituation neuronale plus lente voire absente aux stimuli répétés, "
            "et les guides de conception recommandent la constance plutôt que la nouveauté.",
        ],
        "reserve": "Le désengagement observé en séance ne relève probablement pas d'une "
                   "habituation classique — plutôt fatigue ou pause sensorielle volontaire.",
        "source": "docs/reference/analyses/analyse_activite_cause_effet.md",
    },
    "choix-a-deux": {
        "cible": "Exercer la décision intentionnelle et la communication par le choix (proto-CAA)",
        "fondement": [
            "Première étape vers la communication alternative et augmentée : la dichotomie "
            "gauche/droite peut représenter n'importe quelle paire réelle (activité, objet, lieu), "
            "les formes et couleurs étant substituables selon le profil.",
            "Les ressources sur les dispositifs de communication alternative soulignent l'intérêt "
            "de motifs moteurs cohérents et d'une charge cognitive minimisée dans la conception "
            "des interactions.",
            "Aucune bonne réponse : les deux zones sont équivalentes. Seul l'acte de choisir est "
            "l'objet de l'activité, ce qui exclut toute connotation d'échec.",
        ],
        "reserve": "L'adulte valide le choix — le risque est d'anticiper à la place du jeune et "
                   "de transformer un choix en simple confirmation.",
        "source": "docs/pedagogie/projet_pedagogique.md §4.2",
    },
    "timer": {
        "cible": "Matérialiser l'attente et rendre les transitions prévisibles",
        "fondement": [
            "Recommandation HAS §3.5 : rendre visible ce qui va se passer avant et après une "
            "activité, matérialiser la durée via des supports visuels.",
            "La prévisibilité et la structure sont l'un des trois principes fondateurs retenus "
            "pour tout le projet — réduire les surprises, rendre visible ce qui va se passer.",
            "Cinq visuels sélectionnables car les profils sont hétérogènes : l'adaptation au "
            "profil de chaque enfant n'est pas un confort mais une condition d'efficacité.",
        ],
        "reserve": "L'outil rend la durée visible, pas la suite prévisible : ce qui se passe "
                   "après le timer doit être annoncé à l'oral par l'accompagnant.",
        "source": "docs/pedagogie/projet_pedagogique.md §4.3",
    },
    "ecrire-ecoute": {
        "cible": "Associer le mot écrit au mot entendu, exercer la motricité fine au clavier",
        "fondement": [
            "Le support visuel est natif au numérique et la machine ne porte aucun jugement sur "
            "la production : l'enfant peut explorer librement le lien lettres/sons.",
            "Synthèse vocale neuronale exécutée localement (Piper) plutôt qu'une API navigateur, "
            "pour un rendu plus proche d'une voix humaine et sans transmission externe.",
            "Toute saisie est lisible, y compris les suites de lettres sans signification : "
            "l'activité n'impose pas de bonne réponse.",
        ],
        "reserve": "Intérêt pédagogique et qualité perçue de la voix non encore évalués en "
                   "séance réelle.",
        "source": "docs/pedagogie/projet_pedagogique.md §4, décision du 2026-07-08",
    },
    "regarde-ou-je-regarde": {
        "cible": "Attention conjointe et alternance des rôles initiateur/suiveur",
        "fondement": [
            "Les formats collaboratifs sont plus efficaces que les formats compétitifs. Les jeux "
            "à tour de rôle enseignent la réciprocité ; les jeux multijoueurs construisent "
            "naturellement l'attention conjointe, les joueurs imitant le comportement du partenaire.",
            "Une revue systématique de 9 interventions rapporte une amélioration significative sur "
            "au moins un construit lié aux compétences sociales dans 100 % des études, l'attention "
            "conjointe et la direction du regard faisant partie des domaines touchés.",
            "Le balayage automatique découle d'une contrainte terrain : les jeunes n'étant pas "
            "autonomes à la souris, l'entrée est limitée à une touche unique (contacteur). Sans "
            "balayage, le jeu dégénérerait en cause-effet à deux sans exigence attentionnelle.",
            "Aucun échec punitif, aucune limite de tentatives, progression par paliers déclenchée "
            "manuellement par l'adulte et jamais par un timer.",
        ],
        "reserve": "La revue critique de Walsh, Linehan & Ryan (2025, Autism) tempère fortement "
                   "l'optimisme des revues antérieures : cibles mal définies, mesures hétérogènes, "
                   "transfert vers la vie réelle non démontré, petits échantillons. Ce jeu est un "
                   "support d'interaction pour l'accompagnant, jamais une intervention validée.",
        "source": "docs/reference/jeux_video_tsa.md",
    },
}


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


def _load_users():
    if not os.path.isfile(USERS_FILE):
        users = [{"name": "admin", "created": datetime.now().strftime("%Y-%m-%d %H:%M")}]
        _save_users(users)
        return users
    try:
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def _save_users(users):
    os.makedirs(os.path.abspath(DATA_DIR), exist_ok=True)
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)


def _user_names(users):
    return [u["name"] for u in users]


def _log_event(user, type_, **fields):
    os.makedirs(os.path.abspath(LOGS_DIR), exist_ok=True)
    month = datetime.now().strftime("%Y-%m")
    path = os.path.join(LOGS_DIR, f"activite_{month}.jsonl")
    entry = {"ts": datetime.now().isoformat(timespec="seconds"), "user": user, "type": type_}
    entry.update({k: v for k, v in fields.items() if v is not None})
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def _get_piper_voice():
    global _piper_voice
    if _piper_voice is None:
        with _piper_lock:
            if _piper_voice is None:
                from piper import PiperVoice
                _piper_voice = PiperVoice.load(PIPER_MODEL)
    return _piper_voice


@bp.context_processor
def _inject_current_user():
    return {"current_user": session.get("user")}


@bp.before_request
def _require_user():
    if request.path.startswith("/static/"):
        return
    if request.endpoint in UTILISATEUR_ENDPOINTS:
        return
    user = session.get("user")
    if user and user in _user_names(_load_users()):
        return
    session.pop("user", None)
    return redirect(url_for("main.utilisateur"))


@bp.after_request
def _log_nav(response):
    if request.path.startswith("/static/"):
        return response
    if request.endpoint == "main.log_event":
        return response
    user = session.get("user")
    if user:
        _log_event(user, "nav", route=request.path, method=request.method)
    return response


@bp.route("/utilisateur", methods=["GET", "POST"])
def utilisateur():
    users = _load_users()
    if request.method == "POST":
        nom = request.form.get("nom", "").strip()
        if nom:
            if nom not in _user_names(users):
                users.append({"name": nom, "created": datetime.now().strftime("%Y-%m-%d %H:%M")})
                _save_users(users)
            session["user"] = nom
            session.permanent = True
            return redirect(url_for("main.docs_view"))
        return redirect(url_for("main.utilisateur"))
    return render_template("utilisateur.html", users=users)


@bp.route("/utilisateur/<nom>/supprimer", methods=["POST"])
def utilisateur_supprimer(nom):
    if nom == "admin":
        abort(400)
    users = [u for u in _load_users() if u["name"] != nom]
    _save_users(users)
    if session.get("user") == nom:
        session.pop("user", None)
    return redirect(url_for("main.utilisateur"))


@bp.route("/utilisateur/<nom>/renommer", methods=["POST"])
def utilisateur_renommer(nom):
    nouveau = request.form.get("nouveau", "").strip()
    users = _load_users()
    names = _user_names(users)
    if nouveau and nom in names and nouveau not in names:
        for u in users:
            if u["name"] == nom:
                u["name"] = nouveau
        _save_users(users)
        if session.get("user") == nom:
            session["user"] = nouveau
    return redirect(url_for("main.utilisateur"))


@bp.route("/api/log-event", methods=["POST"])
def log_event():
    user = session.get("user")
    if not user:
        abort(403)
    data = request.get_json(silent=True) or {}
    activite = str(data.get("activite", ""))[:80]
    event = str(data.get("event", ""))[:80]
    detail = data.get("detail")
    if detail is not None:
        detail = str(detail)[:200]
    _log_event(user, "event", activite=activite, event=event, detail=detail)
    return ("", 204)


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
    return render_template(
        "activites.html", activites=ACTIVITES, theorie=THEORIE, active="activites",
    )


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


@bp.route("/activites/regarde-ou-je-regarde")
def activite_regarde():
    return render_template("activite_regarde.html")


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
        "user": session.get("user"),
        "activite": activite,
        "engagement": engagement,
        "reglages": reglages,
        "note": note,
    })
    _save_retours(retours)
    return redirect(url_for("main.retour_terrain"))
