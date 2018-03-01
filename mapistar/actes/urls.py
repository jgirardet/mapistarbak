# Third Party Libraries
from apistar import Route

from .views import observation_create, observation_delete, observation_list, observation_update

actes_urls = [
    # Route('/{patient_id}/', 'GET', patients_detail),
    Route('/', 'POST', observation_create),
    Route('/{obj_id}/', 'PUT', observation_update),
    Route('/{obj_id}/', 'DELETE', observation_delete),
    Route('/{patient_id}/', 'GET', observation_list),
]
