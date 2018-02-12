# Standard Libraries
from typing import List

# Third Party Libraries
from apistar import Response
from apistar.backends.django_orm import Session

from .schemas import PatientSchema, PatientNoIdSchema
from apistar.exceptions import NotFound, BadRequest
from django.http import Http404
from django.shortcuts import get_object_or_404


def patients_detail(session: Session, patient_id: int) -> PatientSchema:
    """
    Get patient details
    """
    try:
        pat = get_object_or_404(session.Patient, id=patient_id)
    except Http404 as e:
        raise NotFound(str(e))
    return PatientSchema(pat)


def patients_create(session: Session, patient: PatientNoIdSchema) -> Response:
    """
    create patients
    """
    new_patient = session.Patient.objects.create(**patient)
    return Response(PatientSchema(new_patient), status=201)


def patients_update(session: Session, patient: PatientNoIdSchema,
                    patient_id: int) -> PatientSchema:
    """
    modify patients
    patient_id: l'id du patient
    """
    a = session.Patient.objects.filter(id=patient_id).update(**patient)
    if not a:
        raise NotFound('Patient id not found')
    updated_patient = session.Patient.objects.get(id=patient_id)
    return PatientSchema(updated_patient)


def patients_list(session: Session) -> List[PatientSchema]:
    """
    List patients
    """
    p = session.Patient.objects.all()
    return [PatientSchema(x) for x in p]
