from flask import Flask
from datetime import timedelta
import os


def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), "templates"),
        static_folder=os.path.join(os.path.dirname(__file__), "static"),
    )
    app.secret_key = "iatsa-local-secret-key"
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(hours=4)

    from .routes import bp
    app.register_blueprint(bp)

    return app
