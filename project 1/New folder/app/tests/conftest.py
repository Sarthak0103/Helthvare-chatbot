import pytest

from app.app import create_app


@pytest.fixture
def app():
    app = create_app('testing')
    app.config.update({"TESTING": True})
    yield app


@pytest.fixture
def client(app):
    return app.test_client()