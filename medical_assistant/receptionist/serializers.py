from datetime import datetime

from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from receptionist.models import Receptionist
from user.models import User


class ReceptionistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receptionist
        fields = (
            "user",
            "work_phone_number",
        )
        read_only_fields = ("user",)
        extra_kwargs = {
            "work_phone_number": {"required": True},
        }

    def create(self, validated_data):
        user = get_object_or_404(User, id=self.context["request"].user.id)

        return Receptionist.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        instance.updated = datetime.datetime.now()

        return super().update(instance, validated_data)
