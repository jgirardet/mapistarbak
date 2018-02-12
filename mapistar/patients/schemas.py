# Third Party Libraries
from apistar import typesystem
from utils.schemas import email_schema
from utils.schemas import formatted_date
from utils.schemas import regular_text


class PatientSchema(typesystem.Object):
    """
    read only schema, for db call purpose
    won't fail if pattern or anything else wrong
    """
    properties = {
        'id': typesystem.Integer,
        'name': typesystem.string(description="Nom"),
        'firstname': typesystem.string(description="Prénom"),
        'birthdate': typesystem.string(description="Date de naissance"),
        'sexe': typesystem.boolean(description="sexe"),
        'street': typesystem.string(description="rue"),
        'postalcode': typesystem.string(description="Code Postal"),
        'city': typesystem.string(description="Ville"),
        'phonenumber': typesystem.string(description="Numéro de Téléphone"),
        'email': typesystem.string(description="email"),
        'alive': typesystem.boolean(description="vivant ?"),
    }
    required = []


class PatientWriteSchema(PatientSchema):
    "write schema, enforce validation"
    updated_properties = {
        'name': regular_text(description="Nom"),
        'firstname': regular_text(description="Prénom"),
        'birthdate': formatted_date(description="Date de naissance"),
        'email': email_schema(description="email"),
    }
    properties = dict(PatientSchema.properties, **updated_properties)
    required = []


class PatientCreateSchema(PatientWriteSchema):
    properties = {
        k: v
        for k, v in PatientWriteSchema.properties.items()
        if k not in ['id', 'alive']
    }

    required = [
        'name',
        'firstname',
        'birthdate',
    ]


class PatientUpdateSchema(PatientWriteSchema):
    properties = {
        k: v
        for k, v in PatientSchema.properties.items() if k != 'id'
    }

    required = []
