# -*- coding: utf-8 -*-
"""
test_mapistar
----------------------------------
Tests for `mapistar` module.
"""

# Third Party Libraries
from apistar.test import TestClient
from app import app
from pseudos.models import Pseudo

# mapistar
from mapistar import mapistar


def test_mapistar():
    assert mapistar.main() == "hello"


def test_http_request():
    """
    Testing a view, using the test client with
    """
    client = TestClient(app)
    response = client.get('http://localhost/pseudos/')
    assert response.status_code == 200


def test_http_request_with_fixture(ss):
    """
    Testing a view, using the test client with
    but testing with fixture
    """
    client = TestClient(app)
    e = ss.Pseudo.objects.all()
    response = client.get('http://localhost/pseudos/')
    assert response.status_code == 200
