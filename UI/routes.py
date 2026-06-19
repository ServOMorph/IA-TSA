import os
from flask import Blueprint, render_template, send_from_directory, abort

bp = Blueprint("main", __name__)

DOCS_WEB_PATH = os.path.join(
    os.path.dirname(__file__), "..", "docs", "web"
)


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
