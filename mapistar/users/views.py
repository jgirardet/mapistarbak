from apistar import Response, http
from django.contrib.auth import authenticate
from apistar.backends.django_orm import Session
from apistar.http import Response
from apistar.exceptions import Forbidden


def login(username: str, password: str, headers: http.Headers,
          session: Session) -> Response:
    if authenticate(username=username, password=password):
        return Response(
            status=302, headers={
                'Authorization': '123',
                'location': '/'
            })
    raise Forbidden


def logout(session: http.Session):
    if 'username' in session:
        del session['username']
    return Response(status=302, headers={'location': '/'})