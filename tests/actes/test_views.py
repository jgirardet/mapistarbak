# Standard Libraries

# Third Party Libraries
import pytest
from actes.schemas import ObservationSchema, ObservationUpdateSchema
from actes.views import observation_create, observation_list, observation_update
from apistar.exceptions import BadRequest, Forbidden
from tests.factories import FacUser


def test_observation_create(patient, ss, auth_user):
    req = {"patient_id": patient.id, "motif": "blabla"}
    a = observation_create(ss, req, auth_user)
    print(dir(a))
    assert a.status == 201


def test_observation_list(patient, observation, ss):
    obss = [observation(patient=patient) for i in range(5)]
    req = observation_list(ss, patient_id=patient.id)
    assert req == [ObservationSchema(item) for item in obss][::-1]


def test_observation_update(observation, ss, user, auth_user):
    obs = observation(owner=user)
    params = ObservationUpdateSchema({'motif': "blabla"})
    o = observation_update(obs.id, params, ss, auth_user)
    od_db = ss.Observation.objects.get(id=obs.id)
    assert o.content['motif'] == "blabla" == od_db.motif


def test_observation_update_bad_new_data(observation, ss, user, auth_user):
    obs = observation(owner=user)
    params = {'motidzdzdf': "blabla"}
    with pytest.raises(BadRequest):
        observation_update(obs.id, params, ss, auth_user)


def test_observation_update_not_owner(observation, ss, user, auth_user):
    obs = observation(owner=FacUser())
    params = ObservationUpdateSchema({'motif': "blabla"})
    with pytest.raises(Forbidden):
        observation_update(obs.id, params, ss, auth_user)


def test_observation_update_only_today(observation, ss, user, auth_user):
    # moke timezone
    obs = observation(owner=user)
    params = ObservationUpdateSchema({'motif': "blabla"})
    with pytest.raises(Forbidden):
        observation_update(obs.id, params, ss, auth_user)
