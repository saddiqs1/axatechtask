import os
from dotenv import load_dotenv
from flask import Flask
from routes.tasks import tasks_bp
from db import db

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
    db.init_app(app)

    app.register_blueprint(tasks_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)