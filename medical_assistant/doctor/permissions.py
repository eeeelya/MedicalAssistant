from rest_framework import permissions


class PermissionsForDoctor(permissions.BasePermission):
    actions_for_doctor = ("create", "update", "partial_update", "delete", "retrieve")

    def has_permission(self, request, view):
        # only Users with confirmed email can take actions
        if not request.user.email_confirmed:
            return False

        # role Admin can do everything with doctors
        if request.user.type == 4:
            return True

        # role Receptionist and Client can view all or one doctor
        if view.action == ("retrieve" or "list") and request.user.type == (1 or 2):
            return True

        # role Doctor can create, update, partial_update, delete and retrieve only his own profile
        if view.action in self.actions_for_doctor and request.user.type == 3:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        # role Admin can do everything with clients
        if request.user.type == 4:
            return True

        return obj.user == request.user
