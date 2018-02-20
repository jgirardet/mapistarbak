# Third Party Libraries
from apistar.permissions import IsAuthenticated
from users.authentication import MapistarJWTAuthentication

from .get_env import env

DATABASES = {
    'default': {
        'ENGINE': env['DB_ENGINE'],
        'PORT': env['DB_PORT'],
        'NAME': env['DB_NAME'],
        'HOST': env['DB_HOST'],
        'USER': env['DB_USER'],
        'PASSWORD': env['DB_PASSWORD'],
    }
}

DJANGO_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',
    # 'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = []

LOCAL_APPS = [
    'patients',
    'users',
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# change default user
AUTH_USER_MODEL = 'users.User'

SECRET_KEY = env['SECRET_KEY']

AUTHENTICATION = [
    MapistarJWTAuthentication(),
]
PERMISSIONS = [
    IsAuthenticated(),
]
JWT = {'SECRET': env['JWT_SECRET'], 'PAYLOAD_DURATION': {'seconds': 300}}

# added for manage.py only
DEBUG = env['DEBUG']

USE_TZ = True

TIME_ZONE = "Europe/Paris"
