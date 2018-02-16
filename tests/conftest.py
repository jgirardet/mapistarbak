# Standard Libraries
import typing
from contextlib import contextmanager

# Third Party Libraries
import factory
import pytest
from apistar import Component
from apistar import TestClient
from apistar.backends.django_orm import DjangoORM
from apistar.backends.django_orm import Session
from apistar.frameworks.wsgi import WSGIApp as App
from app import components
from config import settings
from config.urls import routes
from tests.factories import *
from users.models import User
from apistar_jwt.token import JWT
from django.utils import timezone

################################################
#APISTAR tools
################################################


@pytest.fixture(autouse=True)
def ss(db):
    """
    session from django backend
    may be passed as parameter for testing views with session as argument
    """

    # def get_session(backend: DjangoORM,
    #                 ss) -> typing.Generator[Session, None, None]:
    #     print(dir(ss))
    #     yield ss

    return Session(DjangoORM(settings.__dict__))


@contextmanager
def get_ss(backend: DjangoORM) -> typing.Generator[Session, None, None]:
    yield Session(backend)


@pytest.fixture(autouse=True, scope='session')
def app_fix():
    """
    fixture for apistar app
    Juste mock get_session to get_ss to disable db stuff from apistar
    Use all regular routes and componements of app.py
    All
    """
    comp = []
    for c in components:
        if c.cls is Session:
            c = Component(Session, init=get_ss, preload=False)
        comp.append(c)
    return App(routes=routes, settings=settings.__dict__, components=comp)


# @pytest.fixture(autouse=True)
# def user(django_user_model):
#     a = django_user_model.objects.create(
#         username="someone", password="something")
#     return a


@pytest.fixture(autouse=True)
def user(db):
    # a = User.objects.create(username="someone", password="something")
    return User.objects.create(username="someone", password="something")


@pytest.fixture(autouse=True)
def client(user):
    SECRET = settings.__dict__['JWT'].get('SECRET')

    payload = {
        'user_id': user.id,
        'iat': timezone.now(),
        'exp':
        timezone.now() + timezone.timedelta(seconds=60)  #  ends in 60 minutes
    }

    token = JWT.encode(payload, secret=SECRET)
    t = TestClient(app_fix())
    t.headers['Authorization'] = "Bearer " + token
    return t


# @pytest.fixture(autouse=True, scope='session')
# def client():
#     t = TestClient(app_fix())
#     return t

############################################
#models
############################################
"""""" """""" """""" """""" """""" """""" """""" """""" """""
""" """""" """""" """""" """""" """""" """""" """""" """""" ""
# from django.contrib.auth import get_user_model

# from pytest_django.fixtures import db

# User = get_user_model()

# assert 1 == sys.path
"""
PAtients
"""


@pytest.fixture(autouse=True, scope='session')
def patientd():
    """
    just a dict, not saved
    """
    return factory.build(dict, FACTORY_CLASS=FacPatient).copy()


@pytest.fixture(autouse=True)
def patient(db):
    """
    return factory mpdele

    """

    return FacPatient()


@pytest.fixture(autouse=True)
def patient10(db):
    """
    return 10 patients
    """

    return [FacPatient() for i in range(10)]


# @pytest.fixture(scope='function', autouse=True)
# def apiclient(db):
#     """
#     DRF apiclient
#     """
#     u = FacUnoUser()
#     from rest_framework.test import APIClient
#     client = APIClient()
#     client.force_authenticate(user=u)
#     return client

# """
# USers
# """

# #
# @pytest.fixture(autouse=True, scope='function')
# def testuser(db):

#     return FacUnoUser()

# # """
# # actes
# # """

# @pytest.fixture(autouse=True, scope='function')
# def observation(db):
#     """
#     fixture for observation instance
#     """
#     return FacObservation()

# #"""
# #Ordonnances
# #""""
# @pytest.fixture(autouse=True)
# def medicamentd(db):
#     return factory.build(
#         dict, FACTORY_CLASS=FacMedicament, ordonnance=FacOrdonnance()).copy()
