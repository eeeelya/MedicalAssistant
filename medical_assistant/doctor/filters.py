from django_filters import rest_framework as filters

from doctor.models import Doctor
from user.models import User


class DoctorFilter(filters.FilterSet):
    user = filters.ModelChoiceFilter(queryset=User.objects.all())
    # TODO: create filters

    class Meta:
        model = Doctor
        fields = ("user",)
