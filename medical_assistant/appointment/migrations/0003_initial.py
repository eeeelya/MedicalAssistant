# Generated by Django 4.1.1 on 2022-09-29 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("appointment", "0002_initial"),
        ("doctor", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="appointment",
            name="doctor",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="doctor.doctor"),
        ),
    ]
