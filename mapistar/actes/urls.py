# Third Party Libraries
from apistar import Route

from .views import observation_create, observation_delete, observation_update, list_acte

actes_urls = [
    # Route('/{patient_id}/', 'GET', patients_detail),
    Route('/', 'POST', observation_create),
    Route('/{obj_id}/', 'PUT', observation_update),
    Route('/{obj_id}/', 'DELETE', observation_delete),
    Route('/{type_acte}/{patient_id}/', 'GET', list_acte),
]
