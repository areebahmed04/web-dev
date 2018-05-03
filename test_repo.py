def test_return_type(req):

    j = req.json()
    assert type(j) == type(dict())


def test_status_code(req):

    assert req.status_code == 200


def test_name_presence(req):

    str = "areebahmed04"
    j = req.json()
    for i in j.values():
        assert str in i


def test_return_size(req):

    j = req.json()
    assert len(j) > 0
