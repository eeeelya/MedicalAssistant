from django.db import models
from django.utils.translation import gettext_lazy as _

from core.abstract_models import SpecialInformation, UserInformation


class Doctor(UserInformation, SpecialInformation):
    class Department(models.TextChoices):
        THERAPY = "THER", _("Therapy")
        DERMATOLOGY = "DERM", _("Dermatology")
        GYNECOLOGY = "GYNE", _("Gynecology")
        SURGERY = "SURG", _("Surgery")
        CHILDREN_THERAPY = "CT", _("Children's therapy")
        NEUROLOGY = "NEUR", _("Neurology")
        PSYCHOTHERAPY = "PSYC", _("Psychotherapy")
        CARDIOLOGY = "CARD", _("Cardiology")
        ONCOLOGY = "ONCO", _("Oncology")
        DENTISTRY = "DENT", _("Dentistry")

    class Category(models.TextChoices):
        HIGH = "H", _("High")
        FIRST = "1", _("First")
        SECOND = "2", _("Second")

    category = models.CharField(max_length=1, choices=Category.choices, default=Category.SECOND)
    department = models.CharField(max_length=4, choices=Department.choices, default=Department.THERAPY)

    class Meta:
        db_table = "doctor"
