# Generated by Django 4.1.3 on 2022-11-13 15:40

import core.storage_backends
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0003_medicalimage"),
    ]

    operations = [
        migrations.AddField(
            model_name="medicalimage",
            name="image_directory",
            field=models.CharField(default="", max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="medicalimage",
            name="image",
            field=models.ImageField(
                max_length=500, storage=core.storage_backends.ImageStorage(), upload_to=models.CharField(max_length=50)
            ),
        ),
    ]
