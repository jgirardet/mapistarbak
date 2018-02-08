# Third Party Libraries
import pytest
from apistar.exceptions import NotFound
from patients.models import Patient
from utils.django_utils import aps_get_list_or_404
from utils.django_utils import aps_get_object_or_404


class TestObject:
    def test_good(self, patient):
        a = patient()
        b = aps_get_object_or_404(Patient, id=a.id)
        assert a == b

    def test_not_fond_is_raised(self):
        with pytest.raises(NotFound):
            aps_get_object_or_404(Patient, id=1)
