from dotenv import load_dotenv
from flask import Flask
from routes.tasks import tasks_bp

load_dotenv(dotenv_path="../")

def create_app():
    app = Flask(__name__)
    app.register_blueprint(tasks_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
