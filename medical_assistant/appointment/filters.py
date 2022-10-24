from django_filters import rest_framework as filters

from appointment.models import Appointment
from user.models import User


class AppointmentFilter(filters.FilterSet):
    user = filters.ModelChoiceFilter(queryset=User.objects.all())
    # TODO: create filters

    class Meta:
        model = Appointment
        fields = ("user",)
