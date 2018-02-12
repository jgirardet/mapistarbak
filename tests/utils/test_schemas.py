# Third Party Libraries
import pytest
from apistar.exceptions import TypeSystemError
from utils.schemas import EmailSchema
from utils.schemas import RegularText
from utils.schemas import formatted_date
from utils.schemas import regular_text


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
        try:
            RegularText('zefzefzefzef####')
        except TypeSystemError as e:
            assert str(e) == RegularText.errors['pattern'].format(
                RegularText.pattern)

    def test_regular_text_function(self):
        a = regular_text(description="la description")
        b = a('le content')
        assert a.description == "la description"
        assert b == 'le content'


class TestDate:
    def test_new_pattern(self):
        """
        """
        try:
            formatted_date()('12-12-1925')
        except TypeSystemError as e:
            assert str(e) == formatted_date().errors['pattern'].format(
                formatted_date().pattern)


class TestEmail:
    def test_email_regex(self):
        """
        not exception should be raise.
        fixed :"-" in regex
        """
        a = [
            'hugues-garnier@rocher.fr',
            'gpERrre@letellier.fr',
            'imbe-rtan-dree@gregoire.fr',
            'ubonneau@perrier.org',
            'alain88@sfr.fr',
            'malletau_relie@dbmail.com',
            'chauvetrene@mon-nier.fr',
            'bouch-et_andr²e@thibault.org',
            'catherinemarch and@club-internet.fr',
            'mjulien@tisc ali.fr',
        ]
        for i in a:
            EmailSc hema(i)
