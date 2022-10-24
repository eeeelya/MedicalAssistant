from rest_framework import permissions


class PermissionsForClient(permissions.BasePermission):
    actions_for_clients = ("retrieve", "create", "update", "partial_update", "delete")

    def has_permission(self, request, view):
        # only Users with confirmed email can take actions
        if not request.user.email_confirmed:
            return False

        # role Admin can do everything with clients
        if request.user.type == 4:
            return True

        # only role Client can create client profile
        if view.action in self.actions_for_clients and request.user.type == 1:
            return True

        # role Receptionist can view all or ano Client
        if view.action == ("list" or "retrieve") and request.user.type == 2:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        # role Admin can do everything with clients
        if request.user.type == 4:
            return True

        if view.action == "retrieve" and request.user.type == 2:
            return True

        return obj.user == request.user
