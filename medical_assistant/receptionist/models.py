from django.core.validators import RegexValidator
from django.db import models

from core.abstract_models import UserInformation, SpecialInformation
from user.models import User


class Receptionist(UserInformation, SpecialInformation):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    work_phone_number = models.CharField(
        null=True, validators=[RegexValidator(regex=r"^\+?1?\d{9,15}$")], max_length=12
    )

    class Meta:
        db_table = "receptionist"
