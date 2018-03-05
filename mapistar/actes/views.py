# Standard Libraries
from typing import List

# Third Party Libraries
from apistar import Response, annotate
from apistar.backends.django_orm import Session as DB
from apistar.exceptions import BadRequest
from apistar.interfaces import Auth
from apistar.permissions import IsAuthenticated
from users.permissions import ActesWritePermission
from utils.shortcuts import get_or_404, get_model
from string import capwords
from .schemas import BaseActeSchema, BaseActeCreateSchema, ObservationCreateSchema, ObservationSchema, ObservationUpdateSchema
from .index import actes_schemas, ActeViews

from .models import Observation

VObs = ActeViews(Observation)


@annotate(permissions=[IsAuthenticated(), ActesWritePermission()])
def observation_update(obj_id: int, new_data: ObservationUpdateSchema, db: DB,
                       auth: Auth) -> Response:

    # check against empty data
    if not new_data:
        raise BadRequest("empty query")

    obs = db.Observation.objects.get(id=obj_id)

    try:
        obs.update(**new_data)
    except AttributeError as e:
        # request should be for valide fields
        raise BadRequest from e
    return Response(ObservationSchema(obs), status=201)


@annotate(permissions=[IsAuthenticated(), ActesWritePermission()])
def observation_delete(obj_id: int, db: DB, auth: Auth) -> Response:
    obs = db.Observation.objects.get(id=obj_id)
    obs.delete()
    return Response({'message': 'deleted'}, status=201)
