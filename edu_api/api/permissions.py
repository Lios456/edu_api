from rest_framework.permissions import BasePermission

class IsPariente(BasePermission):
    def has_permission(self, request, view):
        return isinstance(request.user, Pariente)