from django.core.validators import RegexValidator
from django.db import models
from django_countries import fields

from core.abstract_models import UserInformation, SpecialInformation


class Client(UserInformation, SpecialInformation):
    passport = models.CharField(max_length=9, validators=[RegexValidator(regex=r"^\s{2}\d{7}$")],)
    phone_number = models.CharField(null=True, validators=[RegexValidator(regex=r"^\+?1?\d{9,15}$")], max_length=12)
    city = models.CharField(max_length=120, default="")
    country = fields.CountryField()

    class Meta:
        db_table = "client"
