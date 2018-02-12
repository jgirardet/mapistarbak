# Standard Libraries
import json

# Third Party Libraries
from apistar import reverse_url
from patients.models import Patient
from patients.schemas import PatientSchema

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


#
def test_patient_create(client, patientd):
    a = {
        k: v
        for k, v in patientd.items()
        if k in ['name', 'firstname', 'birthdate']
    }
    response = client.post(reverse_url('patients_create'), a)
    resp = json.loads(response.content.decode())

    assert response.status_code == 201
    assert Patient.objects.get(id=resp['id']).name.lower() == a['name'].lower()


def test_patient_list(client, patient10):
    response = client.get(reverse_url('patients_list'))
    resp = json.loads(response.content.decode())
    assert resp == [PatientSchema(p) for p in Patient.objects.all()]


# def test_http_request(app_fix):
#     """
#     Testing a view, using the test client with
#     """
#     client = TestClient(app_fix)
#     response = client.get('http://local
