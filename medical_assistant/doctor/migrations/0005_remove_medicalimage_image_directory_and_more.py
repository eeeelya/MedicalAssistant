# Generated by Django 4.1.3 on 2022-11-14 00:30

import core.storage_backends
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0004_medicalimage_image_directory_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="medicalimage",
            name="image_directory",
        ),
        migrations.AlterField(
            model_name="medicalimage",
            name="image",
            field=models.ImageField(max_length=500, storage=core.storage_backends.ImageStorage(), upload_to=""),
        ),
    ]
