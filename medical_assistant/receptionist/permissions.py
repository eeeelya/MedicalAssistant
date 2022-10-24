from rest_framework import permissions


class PermissionsForReceptionist(permissions.BasePermission):
    def has_permission(self, request, view):
        # only Users with confirmed email can take actions
        if not request.user.email_confirmed:
            return False

        # role Admin can do everything with receptionists
        if request.user.type == 4:
            return True

        # role Receptionist can do everything with receptionists
        if view.action == "create" and request.user.type == 2:
            return True
        elif request.user.type == 2:  # only Receptionist can create Receptionist profile
            return True

        return False

    def has_object_permission(self, request, view, obj):
        # role Admin can do everything with clients
        if request.user.type == 4:
            return True

        return obj.user == request.user
