import datetime

from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from appointment.models import Appointment
from client.models import Client
from doctor.models import Doctor


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = (
            "client",
            "doctor",
            "type",
            "visiting_datetime",
            "approved",
        )
        read_only_fields = ("approved", )
        extra_kwargs = {
            "client": {"required": True},
            "doctor": {"required": True},
            "type": {"required": True},
            "visiting_datetime": {"required": True},
        }

    def update(self, instance, validated_data):
        instance.updated = datetime.datetime.now()

        return super().update(instance, validated_data)


class AppointmentSerializerForClient(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = (
            "client",
            "doctor",
            "type",
            "visiting_datetime",
            "approved",
        )
        read_only_fields = ("client", "approved")
        extra_kwargs = {
            "doctor": {"required": True},
            "type": {"required": True},
            "visiting_datetime": {"required": True},
        }

    def create(self, validated_data):
        client = get_object_or_404(Client, user__id=self.context["request"].user.id)

        return Appointment.objects.create(client=client, **validated_data)

    def update(self, instance, validated_data):
        instance.updated = datetime.datetime.now()

        return super().update(instance, validated_data)


class AppointmentSerializerForDoctor(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = (
            "client",
            "doctor",
            "type",
            "visiting_datetime",
            "approved",
        )
        read_only_fields = ("doctor", "approved")
        extra_kwargs = {
            "client": {"required": True},
            "type": {"required": True},
            "visiting_datetime": {"required": True},
        }

    def create(self, validated_data):
        doctor = get_object_or_404(Doctor, user__id=self.context["request"].user.id)

        return Appointment.objects.create(doctor=doctor, **validated_data)

    def update(self, instance, validated_data):
        instance.updated = datetime.datetime.now()

        return super().update(instance, validated_data)
