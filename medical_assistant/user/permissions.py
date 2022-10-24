from rest_framework import permissions


class PermissionsForUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # only Admin role can do all actions
        if request.user.type == 4:
            return True

        if view.action == ("retrieve" or "update" or "partial_update" or "delete") and request.user.type == 1:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        # only owner can retrieve his own account
        return obj.id == request.user.id

