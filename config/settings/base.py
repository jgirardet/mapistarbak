# Third Party Libraries
from apistar.permissions import IsAuthenticated
from config.get_env import env
from users.authentication import MapistarJWTAuthentication

AUTHENTICATION = [
    MapistarJWTAuthentication(),
]
PERMISSIONS = [
    IsAuthenticated(),
]
JWT = {'SECRET': env['JWT_SECRET'], 'PAYLOAD_DURATION': {'seconds': 300}}
