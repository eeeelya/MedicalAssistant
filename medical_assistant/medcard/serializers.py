import datetime

from rest_framework import serializers

from medcard.models import MedicalCard, MedicalCardAppointment


class MedCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalCard
        fields = (
            "client",
            "weight",
            "height",
            "blood",
            "allergies",
            "appointments",
        )
        read_only_fields = ("client", "appointments")

    def update(self, instance, validated_data):
        instance.updated = datetime.datetime.now()

        return super().update(instance, validated_data)


class MedCardAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalCardAppointment
        fields = (
            "client",
            "doctor",
            "symptom",
            "therapy",
        )
        read_only_fields = ("client", "doctor")

