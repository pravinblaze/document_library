from flask import Flask
from app.config import Config
from app.extensions import db, migrate
from app.routes import blueprint as api_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app
