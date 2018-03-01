# Third Party Libraries
import pytest
from apistar.exceptions import BadRequest, Forbidden
from django.utils import timezone
from tests.factories import FacUser
from users.permissions import ActesWritePermission

"""
ActesWritePermission Testing
"""

awp = ActesWritePermission()


def test_pass(auth_user, ss, observation):
    obs = observation(owner=auth_user.user)
    assert awp.has_permission(obj_id=obs.id, auth=auth_user, db=ss)


def test_reject_not_owner(auth_user, ss, observation):
    obs = observation(owner=FacUser())
    with pytest.raises(Forbidden):
        awp.has_permission(obj_id=obs.id, auth=auth_user, db=ss)


def test_only_today(observation, ss, auth_user):
    obs = observation(owner=auth_user.user)
    obs.created += timezone.timedelta(days=-1)
    obs.save()
    with pytest.raises(BadRequest):
        awp.has_permission(obs.id, auth_user, ss)
