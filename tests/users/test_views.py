import pytest
from users.authentication import MapistarJWTAuthentication
from users.utils import get_payload
from config.settings import test as test_settings
from apistar_jwt.token import JWT
from apistar_jwt.authentication import get_jwt
from apistar_jwt.exceptions import AuthenticationFailed
from jwt.exceptions import ExpiredSignatureError
from apistar.exceptions import BadRequest, Forbidden
from apistar import reverse_url
import json
from apistar import TestClient
from users.models import User
from django.contrib.auth import authenticate


def test_login_pass(app_fix):
    User.objects.create_user(username='hh', password='hh')
    response = TestClient(app_fix).post(
        reverse_url(
            'login', user="hh", pwd="hh", settings=test_settings.__dict__))
    resp = json.loads(response.content.decode())
    assert response.status_code == 201


def test_login_forbiden_bad_user(app_fix):
    response = TestClient(app_fix).post(
        reverse_url(
            'login',
            user="fzefzefzefzef",
            pwd="fzefzefzef",
            settings=test_settings.__dict__))
    resp = json.loads(response.content.decode())
    assert response.status_code == 403


def test_login_forbiden_inactive_user(app_fix):
    a = User.objects.create_user(username='hh', password='hh')
    a.is_active = False
    a.save()
    response = TestClient(app_fix).post(
        reverse_url(
            'login', user="hh", pwd="hh", settings=test_settings.__dict__))
    resp = json.loads(response.content.decode())
    assert response.status_code == 403
