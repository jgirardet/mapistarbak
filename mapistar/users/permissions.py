# Third Party Libraries
from apistar.backends.django_orm import Session as DB
from apistar.exceptions import BadRequest, Forbidden
from apistar.interfaces import Auth
from django.utils import timezone
from utils.shortcuts import get_or_404


class ActesWritePermission():
    def has_permission(self, obj_id: int, auth: Auth, db: DB):

        obs = get_or_404(db.Observation, obj_id)

        if obs.created.date() != timezone.localdate():
            raise BadRequest("Observation can't be edited another day")

        if auth.user != obs.owner:
            raise Forbidden('Only owner can edit an Observation')

        return True
