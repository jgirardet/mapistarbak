# Standard Libraries
import json

# Third Party Libraries
from apistar import reverse_url
from patients.models import Patient
from patients.schemas import PatientSchema
from patients.views import patients_detail, patients_list

# pytestmark = pytest.mark.django_db()


# patients_detail
def test_patient_detail(client, patient):
    """
    Testing a view, using the test client with
    """
    print(patient)
    response = client.get(
        reverse_url('patients_detail', patient_id=patient.id))
    resp = json.loads(response.content.decode())
    assert resp == PatientSchema(patient)


def test_patient_detail(ss):
    "fail if false schema to read"
    a = Patient(name="ùlùlù#", firstname="mkljlij", birthdate="1234-12-12")
    a.save()
    b = patients_detail(ss, a.id)
    c = patients_list(ss)


#
def test_patient_create(client, patientd):
    a = {
        'name': "mokmomokok",
        'firstname': "ljlijjlj ll",
        'birthdate': "1234-12-12"
    }

    response = client.post(reverse_url('patients_create'), a)
    resp = json.loads(response.content.decode())

    assert response.status_code == 201
    assert Patient.objects.get(id=resp['id']).name.lower() == a['name'].lower()


def test_patient_list(client, patient10):
    response = client.get(reverse_url('patients_list'))
    resp = json.loads(response.content.decode())
    assert resp == [PatientSchema(p) for p in Patient.objects.all()]


def test_patient_update(patient, client):
    response = client.put(
        reverse_url('patients_update', patient_id=patient.id), {
            "city": "Nevers"
        })
    a = Patient.objects.get(id=patient.id)
    assert a.city == "Nevers"