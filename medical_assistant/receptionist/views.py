from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from core.mixins import DeactivateModelMixin
from receptionist.permissions import PermissionsForReceptionist
from receptionist.serializers import ReceptionistSerializer
from receptionist.models import Receptionist
from receptionist.filters import ReceptionistFilter


class ReceptionistViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    DeactivateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ReceptionistSerializer
    permission_classes = (IsAuthenticated, PermissionsForReceptionist)
    filter_backends = (DjangoFilterBackend, )
    filterset_class = ReceptionistFilter

    def get_queryset(self):
        return Receptionist.objects.filter(is_active=True)
