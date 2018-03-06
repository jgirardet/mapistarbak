# Third Party Libraries
from apistar import Include, Route

from .views import VObs, VPrescriptionLibre

actes_urls = [
    # Route('/{patient_id}/', 'GET', patients_detail),
    # Include('/observation', observation_urls),
    *VObs.urls(),
    *VPrescriptionLibre.urls(),
    # Route('/{obj_id}/', 'PUT', observation_update),
]
