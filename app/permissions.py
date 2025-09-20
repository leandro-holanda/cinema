from rest_framework.permissions import BasePermission, IsAdminUser, IsAuthenticated


class DefaultPermissions(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return IsAuthenticated().has_permission(request, view)
        else:
            return IsAdminUser().has_permission(request, view)