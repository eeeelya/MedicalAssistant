from rest_framework import permissions


class PermissionsForMedCard(permissions.BasePermission):
    actions_for_doctor = ("list", "retrieve", "update", "partial_update")

    def has_permission(self, request, view):
        # only Users with confirmed email can take actions
        if not request.user.email_confirmed:
            return False

        if request.user.type == (2 or 4):
            return True

        # role Doctor can view one or all appointments
        if view.action == "retrieve" and request.user.type == 1:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        # role Doctor, Receptionist and Admin can do everything with appointments
        if request.user.type == (2 or 3 or 4):
            return True

        # role Client can do everything only with his own appointments
        if request.user.type == 1:
            return obj.client == request.user


class PermissionsForMedCardAppointment(permissions.BasePermission):
    def has_permission(self, request, view):
        # only Users with confirmed email can take actions
        if not request.user.email_confirmed:
            return False

        if request.user.type == (3 or 4):
            return True

        if view.action == "list" and request.user.type == 1:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        # role Doctor and Admin can do everything with appointments
        if request.user.type == (3 or 4):
            return True

        # role Client can do everything only with his own appointments
        if request.user.type == 1:
            return obj.client == request.user
