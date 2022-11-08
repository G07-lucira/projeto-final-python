from rest_framework import permissions


class CustomIdCommentsPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if (
            request.method in permissions.SAFE_METHODS
            or request.user.is_superuser
            and not request.method == "PATCH"
        ):
            return True

        return request.user.id == obj.user.id
