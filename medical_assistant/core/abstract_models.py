import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _


class UserInformation(models.Model):
    class Sex(models.TextChoices):
        MAN = "M", _("Man")
        WOMAN = "W", _("Woman")
        UNCERTAIN = "-", _("None")

    sex = models.CharField(max_length=1, choices=Sex.choices, default=Sex.UNCERTAIN)
    birthday_date = models.DateField(default=datetime.date.today)

    class Meta:
        abstract = True


class SpecialInformation(models.Model):
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(default=datetime.datetime.now)
    updated = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        abstract = True
