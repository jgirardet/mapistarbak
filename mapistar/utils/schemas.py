# Third Party Libraries
from apistar import typesystem


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
    errors['pattern'] = " mauvaise pattern"
    min_length = 1
    pattern = "^[a-zA-ZáàâäãåçéèêëíìîïñóòôöõúùûüýÿæœÁÀÂÄÃÅÇÉÈÊËÍÌÎÏÑÓÒÔÖÕÚÙÛÜÝŸÆŒ -]+$"
    description = "a non empty charfield"


class Date(typesystem.String):
    """
    date formated yyyy-mm-dd
    """
    pattern = "^([0-9]{4})(-)?(1[0-2]|0[1-9])(?(2)-)(3[0-1]|0[1-9]|[1-2][0-9])$"
    errors = typesystem.String.errors.copy()
    errors['pattern'] = "The following fomrat should be used : yyyy-mm-dd"
    min_length = 1
    description = "Date formated yyyy-mm-dd"
