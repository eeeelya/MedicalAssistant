from django_filters import rest_framework as filters

from receptionist.models import Receptionist
from user.models import User


class ReceptionistFilter(filters.FilterSet):
    user = filters.ModelChoiceFilter(queryset=User.objects.all())
    # TODO: create filters

    class Meta:
        model = Receptionist
        fields = ("user",)
