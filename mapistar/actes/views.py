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
from .schemas import BaseActeSchema, ObservationCreateSchema, ObservationSchema, ObservationUpdateSchema
from .index import actes_schemas


def observation_create(
        db: DB,
        obs: ObservationCreateSchema,
        auth: Auth,
) -> Response:
    """
    Create Observation
    """
    patient = get_or_404(db.Patient, obs.pop('patient_id'))
    new_obs = db.Observation.objects.create(
        patient=patient, owner=auth.user, **obs)
    return Response(ObservationSchema(new_obs), status=201)


def list_acte(type_acte: str, patient_id: int, db: DB) -> List[BaseActeSchema]:
    model = get_model(type_acte, db)

    objs = model.objects.filter(patient_id=patient_id).order_by('-created')

    return [actes_schemas[model.__name__].read(item) for item in objs]


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
