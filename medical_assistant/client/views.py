from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from client.serializers import ClientSerializer
from client.models import Client
from client.permissions import PermissionsForClient
from client.filters import ClientFilter
from client.tasks import create_medcard
from core.mixins import DeactivateModelMixin


class ClientViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    DeactivateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated, PermissionsForClient)
    filter_backends = (DjangoFilterBackend, )
    filterset_class = ClientFilter

    def get_queryset(self):
        return Client.objects.filter(is_active=True)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        create_medcard.delay(id=request.user.id)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
