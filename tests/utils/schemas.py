# Third Party Libraries
import pytest
from apistar.exceptions import TypeSystemError
from utils.schemas import RegularText


class TestRegularText:
    def test_space(self):
        a = RegularText('lijlijl okmok')
        assert a

    params_test = ["jli#", "fzefzf*", "fzef\tfzef"]

    @pytest.mark.parametrize('mot', params_test)
    def test_unallowed(self, mot):
        with pytest.raises(TypeSystemError):
            RegularText(mot)

    def test__not_empty_required(self):
        with pytest.raises(TypeSystemError):
            RegularText('')

    def test_new_pattern(self):
        """
        text pattern modification in new
        """
        a = ""
        try:
            a = RegularText('zefzefzefzef####')
        except TypeSystemError as e:
            assert str(e) == RegularText.errors['pattern'].format(
                RegularText.pattern)


class TestDate:
    def test_pattern(self):
        pass