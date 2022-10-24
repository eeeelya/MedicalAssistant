from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from client.serializers import ClientSerializer
from client.models import Client
from client.permissions import PermissionsForClient
from client.filters import ClientFilter
from core.mixins import DeactivateModelMixin


class ClientViewSet(
    mixins.CreateModelMixin,
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
