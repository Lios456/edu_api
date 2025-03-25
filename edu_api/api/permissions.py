from rest_framework.permissions import BasePermission

class UsuarioActivoOPariente(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        # Si es Usuario, verificar is_active
        if hasattr(user, 'is_active'):
            return user.is_active
        # Si es Pariente, siempre permitir
        return True