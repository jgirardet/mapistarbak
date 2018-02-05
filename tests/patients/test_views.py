# Third Party Libraries
from patients.models import Patient
from patients.schemas import PatientSchema
from patients.views import patients_create
from patients.views import patients_detail
from patients.views import patients_list


def test_patient_list(ss):
    a = Patient.objects.create(name="mlokmk", firstname="mokmok")
    assert patients_list(ss) == [PatientSchema(Patient.objects.get(id=1))]


def test_patient_list2(ss):

    a = Patient.objects.create(name="mlokmk", firstname="mokmok")
    assert patients_list(ss) == [PatientSchema(Patient.objects.get(id=1))]


def test_patient_list3(ss):

    a = [1, 2, 3, 4]

    b = [1, 2, 3, 4]

    assert a == b


def test_patient_list4(ss):
    a = Patient.objects.create(name="mlokmk", firstname="mokmok")
    assert patients_list(ss) == [PatientSchema(Patient.objects.get(id=1))]
