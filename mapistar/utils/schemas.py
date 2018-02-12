# Third Party Libraries
from apistar import typesystem
import typing


class RegularText(typesystem.String):
    """
    standard text
    pattern : can't be empty, and usual character
    """

    # def __new__(self, *args, **kwargs):
    #     value = super().__new__(cls, *args, **kwargs)
    #     obj = typesystem.String.__new__(self, *args, **kwargs)
    #     obj.errors['patter'] = "seuls les lettres, - et espaces sont valides"
    #     return obj
    errors = typesystem.String.errors.copy()
    errors[
        'pattern'] = "Seuls les lettres, - et espace sont des charactères valides"
    min_length = 1
    pattern = r"^[a-zA-ZáàâäãåçéèêëíìîïñóòôöõúùûüýÿæœÁÀÂÄÃÅÇÉÈÊËÍÌÎÏÑÓÒÔÖÕÚÙÛÜÝŸÆŒ -]*$"
    description = "a non empty charfield"


class FormattedDate(typesystem.String):
    """
    date formated yyyy-mm-dd
    """
    pattern = r"^([0-9]{4})(-)?(1[0-2]|0[1-9])(?(2)-)(3[0-1]|0[1-9]|[1-2][0-9])$"
    errors = typesystem.String.errors.copy()
    errors['pattern'] = "The following fomrat should be used : yyyy-mm-dd"
    min_length = 1
    description = "Date formated yyyy-mm-dd"


class EmailSchema(typesystem.String):
    """
    Email
    """
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)?"
    errors = typesystem.String.errors.copy()
    errors['pattern'] = "Please enter a valid e-mail adress"
    description = "Email"


def regular_text(**kwargs) -> typing.Type:
    return type('RegularText', (RegularText, ), kwargs)


def formatted_date(**kwargs) -> typing.Type:
    return type('FormattedDate', (FormattedDate, ), kwargs)


def email_schema(**kwargs) -> typing.Type:
    return type('EmailSchema', (EmailSchema, ), kwargs)
