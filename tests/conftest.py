# Third Party Libraries
# Standard Libraries
# Standard Libraries
# Standard Libraries
# Standard Libraries
import typing
from contextlib import contextmanager

import pytest
from apistar import Component
from apistar.backends.django_orm import DjangoORM
from apistar.backends.django_orm import Session
from apistar.frameworks.wsgi import WSGIApp as App
from app import components
from config import settings
from config.urls import routes


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


@pytest.fixture(autouse=True)
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


############################################
#models
############################################
"""""" """""" """""" """""" """""" """""" """""" """""" """""
""" """""" """""" """""" """""" """""" """""" """""" """""" ""
import factory
# from django.contrib.auth import get_user_model
from tests.factories import *

# from pytest_django.fixtures import db

# User = get_user_model()

# assert 1 == sys.path
"""
PAtients
"""


@pytest.fixture(autouse=True, scope='function')
def patientd():
    """
    just a dict, not saved
    """
    return factory.build(dict, FACTORY_CLASS=FacPatient)


@pytest.fixture(autouse=True)
def patient(db):
    """
    return factory mpdele
    """
    return FacPatient


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
