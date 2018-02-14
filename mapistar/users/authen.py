import base64
from apistar import http
from apistar.authentication import Authenticated, Unauthenticated
import typing
from apistar.interfaces import Auth
from django.contrib.auth import authenticate
from apistar.exceptions import BadRequest


class BasicAuthentication():
    def authenticate(self, authorization: http.Header):
        """
        Determine the user associated with a request, using HTTP Basic Authentication.
        """
        print("Basic authentication")
        if authorization is None:
            return None

        scheme, token = authorization.split()
        if scheme.lower() != 'basic':
            return None
        try:
            username, password = base64.b64decode(token).decode('utf-8').split(
                ':')
        except:
            raise BadRequest

        user = authenticate(username=username, password=password)

        if user:
            print(user, username)
            return AuthenticatedUser(username, user=user)
        else:
            print('fail')
            return Unauthenticated()


class TokenAuthentication():
    def authenticate(self, authorization: http.Header):
        """
        Determine the user associated with a request, using HTTP Basic Authentication.
        """
        print("Basic authentication")
        if authorization is None:
            return None
        try:
            scheme, token = authorization.split()

        except ValueError as e:
            raise BadRequest("invalid token")
        if scheme.lower() != 'mapistar':
            print('pas mapistar')
            return None
        # try:
        token = token
        # except:
        #     raise BadRequest(' pas spit utf8')

        user = authenticate(username='j', password='pwd')

        if user:
            return AuthenticatedUser(user=user, token=token)
        else:
            print('fail')
            return Unauthenticated()


class AuthenticatedUser(Auth):
    def __init__(self, user=None, token=None):
        self.user = user
        self.token = token

    def is_authenticated(self) -> bool:
        return True

    def get_display_name(self) -> str:
        return self.username

    def get_user_id(self) -> str:
        return self.username


class IsMyAuthenticated:
    def has_permission(self, auth: Auth):
        print(auth.user)
        return auth.is_authenticated()
