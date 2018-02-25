# Third Party Libraries
from apistar import Route

from .views import observation_create
from .views import observation_list
from .views import observation_update

actes_urls = [
    # Route('/{patient_id}/', 'GET', patients_detail),
    Route('/', 'POST', observation_create),
    Route('/{obs_id}/', 'PUT', observation_update),
    Route('/{patient_id}/', 'GET', observation_list),
]
