from rest_framework import permissions


class isAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if (
            request.method == "POST"
            and request.user.is_authenticated
            and request.user.is_seller
        ):
            return True
        elif request.method == "GET":
            return True
