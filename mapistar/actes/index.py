"""
Dict Handling various actes
"""

from apistar.interfaces import Auth
from apistar.backends.django_orm import Session as DB
from apistar import Response

from collections import namedtuple

from actes.schemas import ObservationCreateSchema, ObservationUpdateSchema, ObservationSchema

from typing import List

SchemasCollection = namedtuple('SchemasCollection', 'getter creater updater')

from .models import Observation

actes_schemas = {
    Observation:
    SchemasCollection(ObservationSchema, ObservationCreateSchema,
                      ObservationUpdateSchema),
}

from apistar import Route


def create_acte(model, patient_id: int, auth, **kwargs):
    # model = get_model(type_acte, db)
    obj = model.objects.create(
        patient_id=patient_id, owner=auth.user, **kwargs)
    return obj


class ActeViews:
    def __init__(self, model):
        self.model = model
        # self.create.__name__ = 'create_obs'

    def create(self):
        def create_acte(patient_id: int,
                        obs: actes_schemas[self.model].creater, auth: Auth,
                        db: DB) -> Response:
            """
            crreat actes

            """
            obj = self.model.objects.create(
                patient_id=patient_id, owner=auth.user, **obs)
            return Response(actes_schemas[self.model].getter(obj), status=201)

        return create_acte

    def liste(self):
        def liste_acte(
                patient_id: int) -> List[actes_schemas[self.model].getter]:
            # model = get_model(type_acte, db)

            objs = self.model.objects.filter(
                patient_id=patient_id).order_by('-created')

            return [actes_schemas[self.model].getter(item) for item in objs]

        return liste_acte

    def urls(self):
        return [
            Route('/' + self.model.__name__.lower() + '/{patient_id}/', 'POST',
                  self.create()),
            Route('/{patient_id}/', 'GET', self.liste()),
        ]
