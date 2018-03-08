"""
Dict Handling various actes
"""

# Standard Libraries
from typing import List

# Third Party Libraries
from apistar import Response, Route, annotate
from apistar.backends.django_orm import Session as DB
from apistar.exceptions import BadRequest
from apistar.interfaces import Auth
from apistar.permissions import IsAuthenticated
from utils.shortcuts import get_or_404

from .permissions import ActesWritePermission
from .schemas import actes_schemas


class ActesViews:
    def __init__(self, model):
        # from .permissions import ActesWritePermission
        self.model = model
        self.model_name = model.__name__
        self.name = "".join(str(self.model._meta.verbose_name_plural).split())
        print(self.model_name)
        # setattr(self, "create_" + model.__name__.lower(), create)
        # self.create.__name__ = 'create_obs'

    def create(self):
        def create_acte(obj: actes_schemas[self.model_name].creater,
                        auth: Auth, db: DB) -> Response:
            patient = get_or_404(db.Patient, id=obj.pop('patient_id'))
            obj = self.model.objects.create(
                patient=patient, owner=auth.user, **obj)
            return Response(
                actes_schemas[self.model_name].getter(obj), status=201)

        create_acte.__doc__ = f""" Create a new {self.name}"""
        return create_acte

    def liste(self):
        def liste_acte(patient_id: int
                       ) -> List[actes_schemas[self.model_name].getter]:
            # model = get_model(type_acte, db)
            print(patient_id)
            objs = self.model.objects.filter(
                patient_id=patient_id).order_by('-created')

            return [
                actes_schemas[self.model_name].getter(item) for item in objs
            ]

        liste_acte.__doc__ = f"""Liste all {self.name} of given patient"""
        return liste_acte

    def update(self):
        @annotate(permissions=[IsAuthenticated(), ActesWritePermission(self)])
        def acte_update(obj_id: int,
                        new_data: actes_schemas[self.model_name].updater,
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
            return Response(
                actes_schemas[self.model_name].getter(obj), status=201)

        acte_update.__doc__ = f""" Update  {self.name}"""
        return acte_update

    def delete(self):
        @annotate(permissions=[IsAuthenticated(), ActesWritePermission(self)])
        def acte_delete(obj_id: int, auth: Auth) -> Response:
            obj = self.model.objects.get(id=obj_id)
            obj.delete()
            return Response({'message': 'deleted'}, status=201)

        acte_delete.__doc__ = f""" Delete  {self.name}"""
        return acte_delete

    def get_one(self):
        def get_one_acte(obj_id: int,
                         auth: Auth) -> actes_schemas[self.model_name].getter:
            obj = get_or_404(self.model, id=obj_id)
            print(obj)
            return actes_schemas[self.model_name].getter(obj)

        get_one_acte.__doc__ = f""" Get One  {self.name}"""
        return get_one_acte

    def urls(self):
        return [
            Route('/' + self.name + '/{obj_id}/', 'GET', self.get_one(),
                  "get_one_" + self.name),
            Route('/' + self.name + '/', 'POST', self.create(),
                  "create_" + self.name),
            Route('/' + self.name + '/patient/{patient_id}/', 'GET',
                  self.liste(), "liste_" + self.name),
            Route('/' + self.name + '/{obj_id}/', 'PATCH', self.update(),
                  "update_" + self.name),
            Route('/' + self.name + '/{obj_id}/', 'DELETE', self.delete(),
                  "delete_" + self.name),
        ]
