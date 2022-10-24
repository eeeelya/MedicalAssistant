from rest_framework import status
from rest_framework.response import Response


class DeactivateModelMixin:
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
