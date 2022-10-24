from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from appointment.filters import AppointmentFilter
from appointment.models import Appointment
from appointment.permissions import PermissionsForAppointment
from appointment.serializers import (
    AppointmentSerializer,
    AppointmentSerializerForClient,
    AppointmentSerializerForDoctor,
)
from core.mixins import DeactivateModelMixin


class AppointmentViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    DeactivateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsAuthenticated, PermissionsForAppointment)
    filter_backends = (DjangoFilterBackend,)
    filter_class = AppointmentFilter

    def get_queryset(self):
        if self.request.user.type == 1:
            return Appointment.objects.filter(client__user=self.request.user, is_active=True)
        if self.request.user.type == 3:
            return Appointment.objects.filter(doctor__user=self.request.user, is_active=True)

        return Appointment.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.action == "create" and self.request.user.type == 1:
            return AppointmentSerializerForClient
        if self.action == "create" and self.request.user.type == 3:
            return AppointmentSerializerForDoctor

        return AppointmentSerializer
