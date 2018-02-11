# Standard Libraries
from typing import List

# Third Party Libraries
from apistar import Response
from apistar.backends.django_orm import Session
from utils.django_utils import aps_get_object_or_404

from .schemas import PatientSchema


def patients_detail(session: Session, patient_id: int) -> PatientSchema:
    """
    Get patient details
    """
    pat = aps_get_object_or_404(session.Patient, id=patient_id)
    return PatientSchema(pat)


def patients_create(session: Session, patient: PatientSchema) -> Response:
    """
    create new patient
    """
    patient.pop('id')
    p = session.Patient.objects.create(**patient)
    return Response(PatientSchema(p), status=201)


def patients_list(session: Session) -> List[PatientSchema]:
    """
    List patients
    """
    p = session.Patient.objects.all()
    return [PatientSchema(x) for x in p]
