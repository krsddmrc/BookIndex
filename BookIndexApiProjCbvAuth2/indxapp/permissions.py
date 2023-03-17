from rest_framework import permissions


class IsAuth(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user)