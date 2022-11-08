from rest_framework import permissions
from rest_framework.views import Request, View


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj) -> bool:
        return request.method == "GET" or obj.id == request.user.id


class ListUsersValidation(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method == "POST" or request.user and request.user.is_authenticated
        )

class isAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, req, view, obj) -> bool:
        if req.method in permissions.SAFE_METHODS:
            return True
            
        return (
            req.user.is_authenticated
            and req.user.is_superuser
            or req.user.is_authenticated
            and obj.id == req.user.id
        )