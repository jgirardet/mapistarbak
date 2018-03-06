# Third Party Libraries
from apistar import http
from apistar.exceptions import BadRequest, Forbidden
from apistar.interfaces import Auth
from django.utils import timezone
from utils.shortcuts import get_or_404


class ActesWritePermission():
    def __init__(self, models):
        self.models = models

    def has_permission(self, obj_id: int, path: http.Path, auth: Auth):

        model_name = path.split('/')[2]

        try:
            model = self.models[model_name]
        except KeyError:
            raise BadRequest("model inconnu au bataillon")

        obs = get_or_404(model, obj_id)

        if obs.created.date() != timezone.localdate():
            raise BadRequest("Observation can't be edited another day")

        if auth.user != obs.owner:
            raise Forbidden('Only owner can edit an Observation')

        return True
