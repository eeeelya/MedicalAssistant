from django.db import models
from django.utils.translation import gettext_lazy as _


class ModelType(models.TextChoices):
    SEGMENTATION = "SEGM", _("Segmentation")
    # TODO: add more models
