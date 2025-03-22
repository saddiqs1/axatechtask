from dotenv import load_dotenv
from flask import Flask
from blueprints.tasks_api import tasks_api_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.register_blueprint(tasks_api_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
