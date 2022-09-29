from django.core.validators import RegexValidator
from django.db import models

from core.abstract_models import UserInformation, SpecialInformation


class Receptionist(UserInformation, SpecialInformation):
    work_phone_number = models.CharField(
        null=True, validators=[RegexValidator(regex=r"^\+?1?\d{9,15}$")], max_length=12
    )

    class Meta:
        db_table = "receptionist"
