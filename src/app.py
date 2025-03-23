import logging
from logging.config import dictConfig
from flask import Flask
from routes.tasks import tasks_bp
from routes.health import health_bp
from routes.errors import error_bp
from db import db
from config import Config

dictConfig(Config.LOGGING)
LOGGER = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
    db.init_app(app)

    app.register_blueprint(tasks_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(error_bp)

    LOGGER.info("App started")
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)