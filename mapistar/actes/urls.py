# Third Party Libraries
from apistar import Route

from .views import observation_delete, observation_update
from .views import VObs
from apistar import Include

observation_urls = [
    Route('/{patient_id}/', 'POST', VObs.create()),
    Route('/{patient_id}/', 'GET', VObs.liste()),
]

actes_urls = [
    # Route('/{patient_id}/', 'GET', patients_detail),
    # Include('/observation', observation_urls),
    *VObs.urls(),
    Route('/{obj_id}/', 'PUT', observation_update),
    Route('/{obj_id}/', 'DELETE', observation_delete),
]
