# Third Party Libraries
from apistar import http, Settings
from apistar.exceptions import BadRequest, Forbidden
from apistar.interfaces import Auth
from django.utils import timezone
from utils.shortcuts import get_or_404
import re


def get_act_model_from_url(url:str, instances:dict, settings: Settings):
    """
    Recupère le modèle en cours via l url demandé
    Le nom des models issus d'acte ne peuvent apparaître 2 fois dans
    une même url.
    Fouille dans ActesViews.instances
    """


    model_name = []
    for name in instances:
        regex = fr"^.*{re.escape(settings['ACTES_URL'])}/({re.escape(name)})/[0-9]+/$"
        a = re.findall(regex, url)
        if a:
            model_name.append(*a)

    if not len(model_name)  == 1:
        raise BadRequest("Erreur d'url ou de model")

    try:
        model = instances[model_name[0]]
    except KeyError:
        raise BadRequest("model inconnu au bataillon")

    return model


class ActesWritePermission():
    def __init__(self, model):
        self.model = model
        print(self.model)

    def has_permission(self, obj_id: int, path: http.Path, auth: Auth,
                       settings: Settings):
        
        

        model = get_act_model_from_url(path, self.models, settings)

        obj = get_or_404(model, obj_id)

        if obj.created.date() != timezone.localdate():
            raise BadRequest("Observation can't be edited another day")

        if auth.user != obj.owner:
            raise Forbidden('Only owner can edit an Observation')

        return True
