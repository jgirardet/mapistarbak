# Third Party Libraries
from apistar import Route

from .views import VObs
from apistar import Include

actes_urls = [
    # Route('/{patient_id}/', 'GET', patients_detail),
    # Include('/observation', observation_urls),
    *VObs.urls(),
    # Route('/{obj_id}/', 'PUT', observation_update),
]
