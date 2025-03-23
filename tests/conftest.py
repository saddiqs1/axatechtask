import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import pytest
from src.app import create_app

@pytest.fixture(scope="session")
def flask_app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    client = app.test_client()

    ctx = app.test_request_context()
    ctx.push()

    yield client

    ctx.pop()