# Standard Libraries
from collections import ChainMap
from datetime import date

# Third Party Libraries
from apistar import typesystem
from utils.schemas import regular_text, formatted_date, email_schema


class PatientSchema(typesystem.Object):
    properties = {
        'id': typesystem.Integer,
        'name': regular_text(description="Nom"),
        'firstname': regular_text(description="Prénom"),
        'birthdate': formatted_date(description="Date de naissance"),
        'sexe': typesystem.boolean(description="sexe"),
        'street': typesystem.string(description="rue"),
        'postalcode': typesystem.string(
            description="Code Postal", max_length=5),
        'city': typesystem.string(description="Ville"),
        'phonenumber': typesystem.string(description="Numéro de Téléphone"),
        'email': email_schema(description="email"),
        'alive': typesystem.boolean(description="vivant ?"),
    }
    required = ['name', 'firstname', "birthdate"]
    excluded = []


class PatientNoIdSchema(PatientSchema):
    required = []
    properties = {
        key: value
        for key, value in PatientSchema.properties.items()
        if key not in ['id']
    }