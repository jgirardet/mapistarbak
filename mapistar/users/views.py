# Third Party Libraries
from apistar import Response
from apistar import Settings
from apistar import annotate
from apistar import http
from apistar.exceptions import Forbidden
from apistar_jwt.token import JWT
from django.contrib.auth import authenticate
from django.utils import timezone


#login should be authenticated
@annotate(authentication=[], permissions=[])
def login(user: str, pwd: str, settings: Settings) -> Response:
    user_logged = authenticate(username=user, password=pwd)

    if not user_logged:
        raise Forbidden("Utilisateur inactif, mauvais login/mot de passe")

    SECRET = settings['JWT'].get('SECRET')

    payload = {
        'user_id': user_logged.id,
        'iat': timezone.now(),
        'exp':
        timezone.now() + timezone.timedelta(seconds=600)  #  ends in 60 minutes
    }
    token = JWT.encode(payload, secret=SECRET)

    return Response({'token': token}, status=201)
