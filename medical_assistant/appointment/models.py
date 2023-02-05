import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

from client.models import Client
from core.abstract_models import SpecialInformation
from doctor.models import Doctor


class Appointment(SpecialInformation):
    class AppointmentType(models.TextChoices):
        CONSULTATION = "C", _("Consultation")
        SURVEY = "S", _("Survey")
        OPERATION = "O", _("Operation")

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=AppointmentType.choices, default=AppointmentType.CONSULTATION)
    visiting_datetime = models.DateTimeField(default=datetime.datetime.now)
    approved = models.BooleanField(default=False)

    class Meta:
        db_table = "appointment"
