from django_filters import rest_framework as filters

from client.models import Client
from user.models import User


class ClientFilter(filters.FilterSet):
    user = filters.ModelChoiceFilter(queryset=User.objects.all())

    # TODO: add more filters

    class Meta:
        model = Client
        fields = ("user",)
