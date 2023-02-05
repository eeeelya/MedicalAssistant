from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from core.mixins import DeactivateModelMixin
from medcard.filters import MedCardFilter
from medcard.models import MedicalCard, MedicalCardAppointment
from medcard.permissions import PermissionsForMedCard, PermissionsForMedCardAppointment
from medcard.serializers import MedCardAppointmentSerializer, MedCardSerializer


class MedCardViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (PermissionsForMedCard,)
    filter_backends = (IsAuthenticated, DjangoFilterBackend)
    filter_class = MedCardFilter

    def get_queryset(self):
        if self.request.user.type == 1:
            return MedicalCard.objects.filter(client__user=self.request.user, is_active=True)

        return MedicalCard.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.request.user.type == 1:
            return

        return MedCardSerializer


class MedCardAppointmentViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    DeactivateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = MedCardAppointmentSerializer
    permission_classes = (IsAuthenticated, PermissionsForMedCardAppointment)

    def get_queryset(self):
        if self.request.user.type == 1:
            return MedicalCardAppointment.objects.filter(client__user=self.request.user, is_active=True)

        return MedicalCardAppointment.objects.filter(is_active=True)
