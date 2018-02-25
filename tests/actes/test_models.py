import pytest
from tests.factories import FacObservation

pytestmark = pytest.mark.django_db


class TestObservation:
    """
    Class to test observtion model
    """

    def test_string(self, observation):
        # test __str__
        obs = observation()
        assert str(obs) == obs.motif

    def test_save(self):
        observation = FacObservation()
        import time
        time.sleep(1 / 100)
        observation.save()
        assert observation.created < observation.modified
