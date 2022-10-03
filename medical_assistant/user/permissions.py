from rest_framework import permissions


class ListPermissionForAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == "list":
            return request.user.is_superuser or request.user.type == 4

        return True


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action == "retrieve" or "update" or "partial_update" or "delete":
            return obj == request.user

        return True
