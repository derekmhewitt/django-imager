from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """This is a custom permission to ensure only the owner of an object
    can edit it."""

    def has_object_permission(self, request, view, obj):
        """Allows everyone to make safe requests, only owner to write."""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
