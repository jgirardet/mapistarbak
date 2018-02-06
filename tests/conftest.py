# Third Party Libraries
import pytest
from apistar.backends.django_orm import DjangoORM
from apistar.backends.django_orm import get_session
from config.settings import test

pytestmark = pytest.mark.django_db(transaction=True)


@pytest.fixture(autouse=True)
def ss(transactional_db):
    """
    session from django backend
    may be passed as parameter for testing views with session as argument
    """
    with get_session(DjangoORM(test.__dict__)) as s:
        yield s
