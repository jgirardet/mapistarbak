"""
Dict Handling various actes
"""

from collections import namedtuple

from actes.schemas import ObservationCreateSchema, ObservationUpdateSchema, ObservationSchema

SchemasCollection = namedtuple('Schemas', 'read create update')

actes_schemas = {
    'Observation':
    SchemasCollection(ObservationSchema, ObservationCreateSchema,
                      ObservationUpdateSchema),
}
