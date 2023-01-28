# Generated by Django 4.1.2 on 2022-10-23 08:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("client", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="passport",
            field=models.CharField(
                max_length=9, null=True, validators=[django.core.validators.RegexValidator(regex="^\\w{2}\\d{7}$")]
            ),
        ),
    ]
