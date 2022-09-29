from django.db import models
from django.utils.translation import gettext_lazy as _

from core.abstract_models import SpecialInformation, UserInformation


class Doctor(UserInformation, SpecialInformation):
    class Department(models.TextChoices):
        THERAPY = "T", _("Therapy")
        DERMATOLOGY = "D", _("Dermatology")
        GYNECOLOGY = "G", _("Gynecology")
        SURGERY = "S", _("Surgery")
        CHILDREN_THERAPY = "CT", _("Children's therapy")
        NEUROLOGY = "N", _("Neurology")
        PSYCHOTHERAPY = "P", _("Psychotherapy")
        CARDIOLOGY = "C", _("Cardiology")
        ONCOLOGY = "O", _("Oncology")
        DENTISTRY = "D", _("Dentistry")

    class Category(models.TextChoices):
        HIGH = "H", _("High")
        FIRST = "1", _("First")
        SECOND = "2", _("Second")

    category = models.CharField(max_length=1, choices=Category.choices, default=Category.SECOND)
    department = models.CharField(max_length=2, choices=Department.choices, default=Department.THERAPY)

    class Meta:
        db_table = "doctor"
