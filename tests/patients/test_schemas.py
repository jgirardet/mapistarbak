from patients.schemas import RegularText
import pytest
from apistar.exceptions import TypeSystemError


def test_space():
    RegularText('lijlijl okmok')


params_test = ["jli#", "fzefzf*", "fzef\tfzef"]


@pytest.mark.parametrize('mot', params_test)
def test_unallowed(mot):
    with pytest.raises(TypeSystemError):
        RegularText(mot)