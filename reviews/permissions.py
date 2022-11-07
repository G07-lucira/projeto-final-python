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
        if request.user.is_superuser:
            return True

        return request.user == obj

class CustomReviewRestrictPermission(permissions.BasePermission):
     def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        object = get_object_or_404(Review, id=request.parser_context["kwargs"]["review_id"])
        return (
            request.method == "DELETE" 
            or request.method == "GET" 
            or request.method == 'PATCH' and request.user.is_superuser == False 
            and request.user.is_authenticated
            and object.user_id == request.user.id
        )        