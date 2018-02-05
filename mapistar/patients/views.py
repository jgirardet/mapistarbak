# Standard Libraries
from typing import List

# Third Party Libraries
from apistar import Response
from apistar.backends.django_orm import Session
from utils.django_utils import get_object_or_404

from .schemas import PatientSchema
from .schemas import PatientSchemaId


def patients_detail(session: Session, patient_id: int) -> PatientSchema:
    """
    Get patient details
    """
    pat = get_object_or_404(session.Patient, id=patient_id)
    # try:
    #     pat = session.Patient.objects.get(id=patient_id)
    # except ObjectDoesNotExist:
    #     raise NotFound()
    return PatientSchemaId(pat)


def patients_create(session: Session, pati: PatientSchema) -> Response:
    """
    create new patient
    """
    p = session.Patient(**pati)
    p.save()
    return Response(PatientSchemaId(p), status=201)


def patients_list(session: Session) -> List[PatientSchemaId]:

    p = session.Patient.objects.all()
    return [PatientSchema(x) for x in p]
