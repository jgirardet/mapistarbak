# -*- coding: utf-8 -*-
"""
test_mapistar
----------------------------------
Tests for `mapistar` module.
"""

# Third Party Libraries
from apistar.test import TestClient
from pseudos.models import Pseudo

# mapistar
from mapistar import mapistar


def test_mapistar():
    assert mapistar.main() == "hello"


import pytest

pytestmark = pytest.mark.django_db()


def test_http_request(app_fix):
    """
    Testing a view, using the test client with
    """
    # comp = [
    #     Component(DjangoORM),
    #     Component(Session, init=get_ss, preload=False)
    # ]

    # lapp = App(routes=routes, settings=settings.__dict__, components=comp)

    # app.components = {ss, ssf}

    client = TestClient(app_fix)
    response = client.get('http://localhost/pseudos/')
    assert response.status_code == 200


# def test_http_request2():
#     """
#     Testing a view, using the test client with
#     """
#     client = TestClient(app)
#     response = client.get('http://localhost/pseudos/')
#     assert response.status_code == 200


def test_query():
    """
    Testing a db
    """
    a = Pseudo.objects.all()

    assert True


def test_query2():
    """
    Testing a db
    """
    a = Pseudo.objects.all()

    assert True


def test_write():
    """
    Testing a db
    """
    a = Pseudo(name="jilj")
    a.save()
    print('id: ', a.id)
    assert True


# def test_http_request_with_fixture(ss):
#     """
#     Testing a view, using the test client with
#     but testing with fixture
#     """
#     client = TestClient(app)
#     e = ss.Pseudo.objects.all()
#     response = client.get('http://localhost/pseudos/')
#     assert response.status_code == 200
