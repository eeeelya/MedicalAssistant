from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets

from core.mixins import DeactivateModelMixin
from doctor.filters import DoctorFilter
from doctor.models import Doctor
from doctor.permissions import PermissionsForDoctor
from doctor.serializers import DoctorSerializer


class DoctorViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    DeactivateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = DoctorSerializer
    permission_classes = (PermissionsForDoctor,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DoctorFilter

    def get_queryset(self):
        return Doctor.objects.filter(is_active=True)
