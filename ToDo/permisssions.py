from rest_framework.permissions import BasePermission
from .models import User

class IsSAdmin(BaseException):

    def has_permission(self, request, view):
        return request.user.role == User.SUPERADMIN
    
class IsCLIENT(BaseException):

    def has_permission(self, request, view):
        return request.user.role == User.CLIENT

class IsClientorSAdmin(BasePermission):
    def has_permission(self, request, view):
        return IsCLIENT().has_permission(request, view) or IsSAdmin().has_permission(request, view)

