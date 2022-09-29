from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class UserType(models.IntegerChoices):
        UNKNOWN = 0
        CLIENT = 1
        RECEPTIONIST = 2
        DOCTOR = 3
        ADMIN = 4

    type = models.IntegerField(choices=UserType.choices, default=UserType.UNKNOWN)
    # email_confirmed = models.BooleanField(default=False)

    class Meta:
        pass

    def __str__(self):
        return self.username.__str__()
