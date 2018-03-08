from .base import *
from apistar.interfaces import Auth
from apistar.backends.django_orm import Session as DB
# PERMISSIONS.clear()
# AUTHENTICATION.clear()

from mapistar.users.authentication import AuthUser

JWT['PAYLOAD_DURATION'] = {'seconds': 9000}


# change authentication for local use
class LocalAuthentification():
    def authenticate(self, db: DB):
        user = db.User.objects.get(username='j')
        print(user)
        return AuthUser(user=user)


AUTHENTICATION.insert(0, LocalAuthentification())