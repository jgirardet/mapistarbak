from .index import ActeViews
from .models import Observation, PrescriptionLibre

VObs = ActeViews(Observation)
VPrescriptionLibre = ActeViews(PrescriptionLibre)

print(ActeViews.instances)
