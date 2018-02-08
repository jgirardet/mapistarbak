# Third Party Libraries
import pytest
from patients.models import Patient
from patients.schemas import PatientSchema
from patients.views import patients_create
from patients.views import patients_detail
from patients.views import patients_list

# pytestmark = pytest.mark.django_db()


def test_patient_list(ss, patient):

    a = patient()
    assert patients_list(ss) == [PatientSchema(Patient.objects.get(id=a.id))]
