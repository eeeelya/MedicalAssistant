from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.abstract_models import SpecialInformation
from client.models import Client
from appointment.models import Appointment


class MedicalCard(SpecialInformation):
    class BloodType(models.TextChoices):
        FIRST = "I", _("0")
        SECOND = "II", _("A")
        THIRD = "III", _("B")
        FOURTH = "IV", _("AB")
        UNCERTAIN = "-", _("None")

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    weight = models.DecimalField(
        default=0, max_digits=4, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(1000.0)]
    )
    height = models.DecimalField(
        default=0, max_digits=4, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(300.0)]
    )
    blood = models.CharField(max_length=3, choices=BloodType.choices, default=BloodType.UNCERTAIN)
    allergies = models.TextField(blank=True)
    appointments = models.ManyToManyField(Appointment, through="MedicalCardAppointment")

    class Meta:
        db_table = "medical_card"


class MedicalCardAppointment(SpecialInformation):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    medical_card = models.ForeignKey(MedicalCard, on_delete=models.CASCADE)
    symptom = models.TextField(blank=True)
    therapy = models.TextField(blank=True)

    class Meta:
        db_table = "medical_card_appointment"
