# Standard Libraries
import json

# Third Party Libraries
import pytest
from apistar import TestClient
from apistar import reverse_url
from app import settings
from users.models import User

pytestmark = pytest.mark.django_db


def test_login_pass(app_fix):
    User.objects.create_user(username='hh', password='hh')
    response = TestClient(app_fix).post(
        reverse_url('login', user="hh", pwd="hh", settings=settings))
    assert response.status_code == 201


def test_login_forbiden_bad_user(app_fix):
    response = TestClient(app_fix).post(
        reverse_url(
            'login', user="fzefzefzefzef", pwd="fzefzefzef",
            settings=settings))
    assert response.status_code == 403


def test_login_forbiden_inactive_user(app_fix):
    a = User.objects.create_user(username='hh', password='hh')
    a.is_active = False
    a.save()
    response = TestClient(app_fix).post(
        reverse_url('login', user="hh", pwd="hh", settings=settings))
    assert response.status_code == 403
