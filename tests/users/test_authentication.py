import pytest
from users.authentication import MapistarJWTAuthentication
from users.utils import get_payload
from config.settings import base
from apistar_jwt.token import JWT
from apistar_jwt.exceptions import AuthenticationFailed
from apistar.exceptions import BadRequest, Forbidden
import apistar_jwt
from unittest.mock import MagicMock
from unittest.mock import patch
import users


def testautheticate_pass_with_valid_jwt(user, ss):
    valid_jwt = JWT.encode(
        get_payload(user, {'seconds': 8}), base.__dict__['JWT']['SECRET'])
    header = "Bearer " + valid_jwt
    engine = MapistarJWTAuthentication()
    authed = engine.authenticate(header, base.__dict__, ss)
    assert authed.user == user


def test_authenticate_fails_without_valid_date_payload(user, ss):
    perimed_jwt = JWT.encode(
        get_payload(user, {'seconds': -8}), base.__dict__['JWT']['SECRET'])
    header = "Bearer " + perimed_jwt
    engine = MapistarJWTAuthentication()
    with pytest.raises(AuthenticationFailed):
        authed = engine.authenticate(header, base.__dict__, ss)


def test_invalid_user(user, ss):
    valid_jwt = JWT.encode(
        get_payload(user, {'seconds': 8}), base.__dict__['JWT']['SECRET'])
    header = "Bearer " + valid_jwt
    user.delete()
    engine = MapistarJWTAuthentication()
    with pytest.raises(BadRequest):
        authed = engine.authenticate(header, base.__dict__, ss)


def test_user_is_not_active(user, ss):
    valid_jwt = JWT.encode(
        get_payload(user, {'seconds': 8}), base.__dict__['JWT']['SECRET'])
    header = "Bearer " + valid_jwt
    user.is_active = False
    user.save()
    engine = MapistarJWTAuthentication()
    with pytest.raises(Forbidden):
        authed = engine.authenticate(header, base.__dict__, ss)


def test_payload_returned_is_empty(user, ss, monkeypatch):
    def return_empty_dict(*args):
        a = MagicMock()
        a.payload = {}
        return a

    monkeypatch.setattr('users.authentication.get_jwt', return_empty_dict)
    valid_jwt = JWT.encode(
        get_payload(user, {'seconds': 8}), base.__dict__['JWT']['SECRET'])
    header = "Bearer " + valid_jwt

    engine = MapistarJWTAuthentication()
    with pytest.raises(AuthenticationFailed):
        authed = engine.authenticate(header, base.__dict__, ss)


class TestAuthUser:
    def test_is_authenticated_is_True(self, auth_user):
        assert auth_user.is_authenticated() == True

    def test_get_user_id(self, auth_user):
        assert auth_user.user.id == auth_user.get_user_id()

    def test_get_display_name(self, auth_user):
        assert auth_user.user.username == auth_user.get_display_name()
