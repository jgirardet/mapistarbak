from apistar import typesystem
from apistar.exceptions import TypeSystemError
from datetime import datetime, date

from dateutil import parser


class DateTime(str):
    native_type = str
    errors = {
        'blank': 'Must not be blank.',
        'parse': 'The value did not successfully parse.'
    }
    trim_whitespace = True

    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)

        if cls.trim_whitespace:
            value = value.strip()

        cls.parse(value)

        return value

    @classmethod
    def parse(cls, value):
        try:
            return datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        except Exception as e:
            raise TypeSystemError(cls=cls, code='parse') from e


class Dd(str):
    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)

        try:
            dt = parser.parse(value)
        except Exception as e:
            raise TypeSystemError from e

        return dt.date().isoformat()