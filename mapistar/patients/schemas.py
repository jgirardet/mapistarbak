# Standard Libraries
from collections import ChainMap
from datetime import date

# Third Party Libraries
from apistar import typesystem
from utils.schemas import RegularText


class PatientSchema(typesystem.Object):
    properties = {
        'id':
            typesystem.Integer,
        'name':
            RegularText,
        'firstname':
            RegularText,
        'birthdate':
            typesystem.string(
                pattern="^([0-9]{4})(-)?(1[0-2]|0[1-9])(?(2)-)(3[0-1]|0[1-9]|[1-2][0-9])$")
    }
    required = ['name', 'firstname']
