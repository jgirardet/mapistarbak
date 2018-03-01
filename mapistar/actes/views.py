# Standard Libraries
from typing import List

# Third Party Libraries
from apistar import Response, annotate
from apistar.backends.django_orm import Session as DB
from apistar.exceptions import BadRequest
from apistar.interfaces import Auth
from apistar.permissions import IsAuthenticated
from users.permissions import ActesWritePermission
from utils.shortcuts import get_or_404

from .schemas import ObservationCreateSchema, ObservationSchema, ObservationUpdateSchema


def observation_create(
        db: DB,
        obs: ObservationCreateSchema,
        auth: Auth,
) -> Response:
    """
    Create Observation
    """
    patient = get_or_404(db.Patient, obs.pop('patient_id'))
    new_obs = db.Observation.objects.create(patient=patient, owner=auth.user, **obs)
    return Response(ObservationSchema(new_obs), status=201)


def observation_list(db: DB, patient_id: int) -> List[ObservationSchema]:
    """
    Get all observation for a giver patient.
    Most recent  first
    """
    obs = db.Observation.objects.filter(patient_id=patient_id).order_by('-created')
    return [ObservationSchema(item) for item in obs]


@annotate(permissions=[IsAuthenticated, ActesWritePermission()])
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


@annotate(permissions=[IsAuthenticated, ActesWritePermission()])
def observation_delete(obj_id: int, db: DB, auth: Auth) -> Response:
    obs = db.Observation.objects.get(id=obj_id)
    obs.delete()
    return Response({'message': 'deleted'}, status=201)
