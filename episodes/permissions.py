from rest_framework import permissions
import ipdb

class CustomIsAuthenticated(permissions.BasePermission):
    def has_permission(self, req, view) -> bool:
        if req.method in permissions.SAFE_METHODS:
            return True

        return req.user.is_authenticated and req.user.is_staff