# Standard Libraries
from string import capwords

# Third Party Libraries
from apistar.backends.django_orm import Session as DB
from apistar.exceptions import NotFound
from django.db import models
from django.http import Http404
from django.shortcuts import get_object_or_404


def get_or_404(model: models, id: [str, int]):
    try:
        item = get_object_or_404(model, id=id)
    except Http404 as e:
        raise NotFound(str(e))
    return item


def get_model(type_acte: str, db: DB) -> models:
    acte = capwords(type_acte)
    try:
        return getattr(db, acte)
    except AttributeError:
        raise BadRequest("Model unknown")
