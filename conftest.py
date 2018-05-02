from main import create_app
import requests
import pytest


@pytest.fixture
def app():

    app = create_app()
    return app


@pytest.fixture
def req():
    res = requests.get('http://127.0.0.1:5000/repo/areebahmed04')
    return res
