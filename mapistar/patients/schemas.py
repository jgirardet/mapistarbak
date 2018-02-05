# Standard Libraries
from collections import ChainMap

# Third Party Libraries
from apistar import typesystem


class RequiredText(typesystem.String):
    max_length = 50

    pattern = "^[a-zA-ZáàâäãåçéèêëíìîïñóòôöõúùûüýÿæœÁÀÂÄÃÅÇÉÈÊËÍÌÎÏÑÓÒÔÖÕÚÙÛÜÝŸÆŒ]+$"


class PatientSchema(typesystem.Object):
    properties = {
        'name': RequiredText,
        'firstname': RequiredText,
        # 'birthdate': typesystem.string(max_length=50)
    }
    required = ['name', 'firstname']


class PatientSchemaId(typesystem.Object):
    properties = dict(
        ChainMap(
            PatientSchema.properties,
            {
                'id': typesystem.Integer,
                # 'name': typesystem.string(max_length=50),
                # 'firstname': typesystem.string(max_length=50),
                # 'birthdate': typesystem.string(max_length=50)
            }))
