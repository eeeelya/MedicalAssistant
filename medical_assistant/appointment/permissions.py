from rest_framework import permissions


class PermissionsForAppointment(permissions.BasePermission):
    def has_permission(self, request, view):
        # only Users with confirmed email can take actions
        if not request.user.email_confirmed:
            return False

        if request.user.type == (1 or 2 or 4):
            return True

        # role Doctor can view one or all appointments
        if view.action == ("list" or "retrieve") and request.user.type == 3:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        # role Receptionist and Admin can do everything with appointments
        if request.user.type == (2 or 4):
            return True

        # role Client can do everything only with his own appointments
        if request.user.type == 1:
            return obj.client == request.user

        if request.user.type == 3:
            return obj.doctor == request.user
