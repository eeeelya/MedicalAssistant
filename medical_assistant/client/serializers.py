import datetime

from rest_framework.serializers import ModelSerializer
from rest_framework.generics import get_object_or_404

from client.models import Client
from user.models import User


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "user",
            "passport",
            "phone_number",
            "city",
            "country",
            "sex",
            "birthday_date",
        )
        read_only_fields = ("user", )
        extra_kwargs = {
            "passport": {"required": True},
            "phone_number": {"required": True},
            "sex": {"required": True},
            "birthday_date": {"required": True},
        }

    def create(self, validated_data):
        user = get_object_or_404(User, id=self.context["request"].user.id)

        return Client.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        instance.updated = datetime.datetime.now()

        return super().update(instance, validated_data)
