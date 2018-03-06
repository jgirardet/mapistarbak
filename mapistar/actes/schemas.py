# Third Party Libraries
# Standard Libraries
from collections import namedtuple

from apistar import typesystem
from apistar.backends.django_orm import Session as DB


class BaseActeSchema(typesystem.Object):
    properties = {
        'id': typesystem.integer(description="Observation id"),
        'patient_id': typesystem.integer(description="Patient id"),
        'created': typesystem.string(description="Created"),
        'modified': typesystem.string(description="Last Modified"),
        'owner_id': typesystem.integer(description="owner id"),
    }
    required = []


class BaseActeCreateSchema(typesystem.Object):

    properties = {
        'patient_id': typesystem.integer(description="Patient id"),
    }
    required = ['patient_id']


class ObservationSchema(typesystem.Object):
    new_properties = {
        'motif': typesystem.string(description="Motif"),
        'body': typesystem.string(description="Texte de l'observation"),
    }
    properties = dict(BaseActeSchema.properties, **new_properties)
    required = []


class ObservationCreateSchema(typesystem.Object):
    """"
    ObservationCreateSchema

    """
    new_properties = {
        'motif': typesystem.string(max_length=60, description="Motif"),
        'body': typesystem.string(description="Texte de l'observation"),
    }
    properties = dict(BaseActeCreateSchema.properties, **new_properties)
    required = BaseActeCreateSchema.required + ['motif']


class ObservationUpdateSchema(typesystem.Object):
    """
    Update only-schema
    """
    properties = ObservationCreateSchema.properties
    # properties = ObservationCreateSchema.new_properties
    required = []


class PrescriptionLibreSchema(typesystem.Object):
    new_properties = {
        'titre': typesystem.string(description="titre"),
        'body': typesystem.string(description="Texte de prescription"),
    }
    properties = dict(BaseActeSchema.properties, **new_properties)
    required = []


class PrescriptionLibreCreateSchema(typesystem.Object):
    """"
    PresciptionLibrecreate

    """
    new_properties = {
        'titre': typesystem.string(max_length=60, description="titre"),
        'body': typesystem.string(description="Texte de prescription"),
    }
    properties = dict(BaseActeCreateSchema.properties, **new_properties)
    required = BaseActeCreateSchema.required + ['titre']


class PrescriptionLibrUpdateSchema(typesystem.Object):
    """
    Update only-schema
    """
    properties = {
        'titre': typesystem.string(max_length=60, description="titre"),
        'body': typesystem.string(description="Texte de prescription"),
    }
    # properties = ObservationCreateSchema.new_properties
    required = []


SchemasCollection = namedtuple('SchemasCollection', 'getter creater updater')

actes_schemas = {
    'Observation':
        SchemasCollection(ObservationSchema, ObservationCreateSchema, ObservationUpdateSchema),
    'PrescriptionLibre':
        SchemasCollection(PrescriptionLibreSchema, PrescriptionLibreCreateSchema,
                          PrescriptionLibrUpdateSchema)
}

# class ObservationCreateSchema(typesystem.Object):
#     """"
#     ObservationCreateSchema

#     """
#     updated_properties = {
#         'motif': typesystem.string(max_length=60, description="Motif"),
#         'body': typesystem.string(description="Texte de l'observation"),
#         'birthdate': formatted_date(description="Date de naissance"),
#     }
#     properties = dict(BaseActeCreateSchema.properties, **updated_properties)
#     # required = BaseActeCreateSchema.required + ['motif,']
#     required = ['motif', 'patient_id']

# class ObservationWriteSchema(ObservationSchema):
#     """"
#     BaseActeSchema with validation
#     enforce validated date at write time
#     """

#     properties = {k,v for k,v in ObservationSchema.properties if k in ['id', 'patient_id']}
#     required = []

# class ActeSerializer(serializers.HyperlinkedModelSerializer):
#     """
#     BaseActe serializer
#     """

#     pk = serializers.IntegerField(label='ID', read_only=True)
#     patient = serializers.HyperlinkedRelatedField(
#         queryset=Patient.objects.all(),
#         view_name='patient-detail',
#     )
#     created = serializers.DateTimeField(read_only=True)
#     modified = serializers.DateTimeField(read_only=True)
#     owner = serializers.HyperlinkedRelatedField(
#         view_name='unouser-detail', read_only=True)

#     class Meta:
#         fields = (
#             'url',
#             'pk',
#             'patient',
#             'created',
#             'modified',
#             'owner',
#         )

# class ObservationSerializer(ActeSerializer):
#     """
#     Observation serializer
#     """
#     url = serializers.HyperlinkedIdentityField(view_name='observation-detail')

#     class Meta(ActeSerializer.Meta):
#         model = Observation
#         fields = ActeSerializer.Meta.fields + ('motif', 'body')
