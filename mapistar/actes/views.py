# Standard Libraries
from typing import List

# Third Party Libraries
from apistar import Response
from apistar.backends.django_orm import Session as DB
from apistar.exceptions import BadRequest, Forbidden
from apistar.interfaces import Auth
from utils.shortcuts import get_or_404

from .schemas import ObservationCreateSchema, ObservationSchema, ObservationUpdateSchema

from django.utils import timezone
from apistar import annotate
from .permissions import ActesWritePermission, IsAdminUser
from users.authentication import MapistarJWTAuthentication


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


def observation_list(db: DB, patient_id: int) -> List[ObservationSchema]:
    """
    Get all observation for a giver patient.
    Most recent  first
    """
    obs = db.Observation.objects.filter(
        patient_id=patient_id).order_by('-created')
    return [ObservationSchema(item) for item in obs]


@annotate(
    authentication=[MapistarJWTAuthentication()], permissions=[IsAdminUser()])
def observation_update(obs_id: int, new_data: ObservationUpdateSchema, db: DB,
                       auth: Auth) -> Response:

    # check against empty data
    if not new_data:
        raise BadRequest("empty query")

    obs = get_or_404(db.Observation, obs_id)

    # Update not possible if not today
    if obs.created.date() != timezone.localdate():
        raise BadRequest("Observation can't be edited another day")

    # cher owner is current_user
    if auth.user != obs.owner:
        raise Forbidden('Only owner can edit an Observation')

    try:
        obs.update(**new_data)
    except AttributeError as e:
        # request should be for valide fields
        raise BadRequest from e
    return Response(ObservationSchema(obs), status=201)


def observation_delete(obs_id, db: DB, auth: Auth) -> bool:
    obs = get_or_404(db.Observation, obs_id)

    if auth.user != obs.owner:
        raise Forbidden('Only owner can edit an Observation')

    obs.delete()
    return True