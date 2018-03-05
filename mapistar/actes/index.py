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

from apistar import Route, annotate
from apistar.permissions import IsAuthenticated
from users.permissions import ActesWritePermission
from utils.shortcuts import get_or_404


class ActeViews:
    def __init__(self, model):
        self.model = model
        self.name = self.model.__name__.lower()
        # setattr(self, "create_" + model.__name__.lower(), create)
        # self.create.__name__ = 'create_obs'

    def create(self):
        def create_acte(patient_id: int,
                        obj: actes_schemas[self.model].creater, auth: Auth,
                        db: DB) -> Response:
            patient = get_or_404(db.Patient, id=patient_id)
            obj = self.model.objects.create(
                patient=patient, owner=auth.user, **obj)
            return Response(actes_schemas[self.model].getter(obj), status=201)

        create_acte.__name__ = "create_" + self.name
        create_acte.__doc__ = f""" Create a new {self.name}"""
        return create_acte

    def liste(self):
        def liste_acte(
                patient_id: int) -> List[actes_schemas[self.model].getter]:
            # model = get_model(type_acte, db)
            print(patient_id)
            objs = self.model.objects.filter(
                patient_id=patient_id).order_by('-created')

            return [actes_schemas[self.model].getter(item) for item in objs]

        liste_acte.__name__ = "liste_" + self.name
        liste_acte.__doc__ = f"""Liste all {self.name} of given patient"""
        return liste_acte

    def update(self):
        @annotate(permissions=[IsAuthenticated(), ActesWritePermission()])
        def acte_update(obj_id: int,
                        new_data: actes_schemas[self.model].updater,
                        auth: Auth) -> Response:

            # check against empty data
            if not new_data:
                raise BadRequest("empty query")

            obj = self.model.objects.get(id=obj_id)

            try:
                obj.update(**new_data)
            except AttributeError as e:
                # request should be for valide fields
                raise BadRequest from e
            return Response(actes_schemas[self.model].getter(obj), status=201)

        acte_update.__name__ = "update_" + self.name
        acte_update.__doc__ = f""" Update  {self.name}"""
        return acte_update

    def delete(self):
        @annotate(permissions=[IsAuthenticated(), ActesWritePermission()])
        def acte_delete(obj_id: int, auth: Auth) -> Response:
            obj = self.model.objects.get(id=obj_id)
            obj.delete()
            return Response({'message': 'deleted'}, status=201)

        acte_delete.__name__ = "delete_" + self.name
        acte_delete.__doc__ = f""" Delete  {self.name}"""
        return acte_delete

    def get_one(self):
        def get_one_acte(obj_id: int,
                         auth: Auth) -> actes_schemas[self.model].getter:
            obj = get_or_404(self.model, id=obj_id)
            print(obj)
            return actes_schemas[self.model].getter(obj)

        get_one_acte.__name__ = "getone_" + self.name
        get_one_acte.__doc__ = f""" Get One  {self.name}"""
        return get_one_acte

    def urls(self):
        return [
            Route('/' + self.name + '/{obj_id}/', 'GET', self.get_one()),
            Route('/' + self.name + '/{patient_id}/', 'POST', self.create()),
            Route('/' + self.name + '/{patient_id}/all/ ', 'GET',
                  self.liste()),
            Route('/' + self.name + '/{obj_id}/', 'PATCH', self.update()),
            Route('/' + self.name + '/{obj_id}/', 'DELETE', self.delete()),
        ]
