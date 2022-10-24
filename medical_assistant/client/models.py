from django.core.validators import RegexValidator
from django.db import models
from django_countries import fields

from core.abstract_models import UserInformation, SpecialInformation
from user.models import User


class Client(UserInformation, SpecialInformation):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    passport = models.CharField(null=True, max_length=9, validators=[RegexValidator(regex=r"^\w{2}\d{7}$")],)
    phone_number = models.CharField(null=True, validators=[RegexValidator(regex=r"^\+?1?\d{9,15}$")], max_length=12)
    city = models.CharField(null=True, max_length=120)
    country = fields.CountryField()

    class Meta:
        db_table = "client"
