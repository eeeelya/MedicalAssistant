import datetime

from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from doctor.models import Doctor
from user.models import User


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = (
            "user",
            "category",
            "department",
        )
        read_only_fields = ("user",)
        extra_kwargs = {
            "category": {"required": True},
            "department": {"required": True},
        }

    def create(self, validated_data):
        user = get_object_or_404(User, id=self.context["request"].user.id)

        return Doctor.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        instance.updated = datetime.datetime.now()

        return super().update(instance, validated_data)
