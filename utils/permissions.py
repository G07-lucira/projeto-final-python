from rest_framework import permissions
import ipdb


class isAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, req, view, obj) -> bool:
        if req.method in permissions.SAFE_METHODS:
            return True
        ipdb.set_trace()
        return (
            req.user.is_authenticated
            and req.user.is_superuser
            or req.user.is_authenticated
            and obj.id == req.user.id
        )
