from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from functools import wraps

class RolePermission(BasePermission):

    def has_permission(self, request, view):
        # Verificar que el usuario esté autenticado
        if not request.user.is_authenticated:
            return False
        allowed_roles = getattr(view, 'allowed_roles', [])
        return request.user.rol in allowed_roles
    
"""""
def role_required(allowed_roles):
    def decorator(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            if request.user.rol not in allowed_roles:
                raise PermissionDenied("No tienes permiso para acceder a esta vista.")
            return func(request, *args, **kwargs)
        return inner
    return decorator
"""