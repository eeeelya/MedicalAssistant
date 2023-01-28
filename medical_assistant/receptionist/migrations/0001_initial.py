# Generated by Django 4.1.1 on 2022-09-29 20:37

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Receptionist",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "sex",
                    models.CharField(choices=[("M", "Man"), ("W", "Woman"), ("-", "None")], default="-", max_length=1),
                ),
                ("birthday_date", models.DateField(default=datetime.date.today)),
                ("is_active", models.BooleanField(default=True)),
                ("created", models.DateTimeField(default=datetime.datetime.now)),
                ("updated", models.DateTimeField(default=datetime.datetime.now)),
                (
                    "work_phone_number",
                    models.CharField(
                        max_length=12,
                        null=True,
                        validators=[django.core.validators.RegexValidator(regex="^\\+?1?\\d{9,15}$")],
                    ),
                ),
            ],
            options={
                "db_table": "receptionist",
            },
        ),
    ]