from main import Repo
from flask import jsonify
import requests
import pytest


@pytest.fixture
def req():
    res = requests.get('http://127.0.0.1:5000/repo/areebahmed04')
    return res


def test_return_type(req):

    j = req.json()
    assert type(j) == type(dict())


def test_return_value(req):

    assert req.status_code == 200


def test_return_size(req):

    j = req.json()
    assert len(j) > 0


def test_name_presence(req):

    str = "areebahmed04"
    j = req.json()
    for i in j.values():
        assert str in i