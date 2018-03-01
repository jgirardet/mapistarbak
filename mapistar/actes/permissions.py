from apistar.interfaces import Auth
from apistar import http
from apistar.exceptions import BadRequest, Forbidden
from utils.shortcuts import get_or_404
from apistar.backends.django_orm import Session as DB
from django.utils import timezone


class IsAdminUser():
    def has_permission(self, auth: Auth):
        if not auth.is_authenticated():
            return False
        return False


class ActesWritePermission():
    def has_permission(self, auth: Auth):
        # if not obj_id:
        #     raise BadRequest('Query obj no defined')

        # obs = get_or_404(db.Observation, obj_id)
        # print('mokkkkkkkkkmokmokmokm mok mok mok omkomkm okomk ')
        # raise Forbidden('mkmokmok')
        # # Update not possible if not today
        # if obs.created.date() != timezone.localdate():
        #     raise BadRequest("Observation can't be edited another day")
        return False


# class ActesWritePermission():
#     def has_permission(self, auth: Auth, db: DB, obj_id: http.QueryParam):
#         if not obj_id:
#             raise BadRequest('Query obj no defined')

#         obs = get_or_404(db.Observation, obj_id)
#         print('mokkkkkkkkkmokmokmokm mok mok mok omkomkm okomk ')
#         raise Forbidden('mkmokmok')
#         # Update not possible if not today
#         if obs.created.date() != timezone.localdate():
#             raise BadRequest("Observation can't be edited another day")
#         return False
