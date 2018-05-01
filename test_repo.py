from main import Repo
from flask import jsonify
import requests

def test_return_type():

    res = requests.get('http://127.0.0.1:5000/repo')
    j = res.json()
    assert(type(j)==type(dict()))
    # print("type" , type(dict()))

def test_repo():
    assert 1==1
