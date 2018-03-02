# Standard Libraries

# Third Party Libraries
import pytest
from actes.views import list_acte
from apistar.exceptions import BadRequest, Forbidden
from django.utils import timezone
from tests.factories import FacUser
from actes.index import actes_schemas
from actes.schemas import ObservationSchema


def test_list_acte_pass(patient, observation, ss):
    obss = [observation(patient=patient) for i in range(5)]
    req = list_acte('observation', patient.id, ss)
    assert req == [ObservationSchema(item) for item in obss][::-1]


# def test_observation_create(patient, ss, auth_user):
#     req = {"patient_id": patient.id, "motif": "blabla"}
#     a = observation_create(ss, req, auth_user)
#     print(dir(a))
#     assert a.status == 201

# def test_observation_update(observation, ss, user, auth_user):
#     obs = observation(owner=user)
#     params = ObservationUpdateSchema({'motif': "blabla"})
#     o = observation_update(obs.id, params, ss, auth_user)
#     od_db = ss.Observation.objects.get(id=obs.id)
#     assert o.content['motif'] == "blabla" == od_db.motif

# def test_observation_update_bad_new_data(observation, ss, user, auth_user):
#     obs = observation(owner=user)
#     params = {'motidzdzdf': "blabla"}
#     with pytest.raises(BadRequest):
#         observation_update(obs.id, params, ss, auth_user)

# def test_observation_delete(observation, ss, auth_user):
#     obs = observation(owner=auth_user.user)
#     o = observation_delete(obs.id, ss, auth_user)
#     assert o
