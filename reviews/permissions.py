from rest_framework import permissions
from django.shortcuts import get_object_or_404
from .models import Review

class CustomReviewPermission(permissions.BasePermission):
     def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return (
            request.user.is_authenticated or request.user.is_superuser
        )

class CustomIdReviewPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser and not request.method == 'PATCH' :
            return True

        return request.user.id == obj.id
    