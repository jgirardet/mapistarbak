from .get_env import env
from users.authen import BasicAuthentication, IsMyAuthenticated, TokenAuthentication
from apistar.authentication import Authenticated
from apistar.permissions import IsAuthenticated

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
    TokenAuthentication(),
]
PERMISSIONS = [
    IsMyAuthenticated(),
]

# added for manage.py only
DEBUG = env['DEBUG']
