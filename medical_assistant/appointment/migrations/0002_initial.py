# Generated by Django 4.1.1 on 2022-09-29 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("appointment", "0001_initial"),
        ("client", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="appointment",
            name="client",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="client.client"),
        ),
    ]