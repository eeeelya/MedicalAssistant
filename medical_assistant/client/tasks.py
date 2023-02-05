from rest_framework.generics import get_object_or_404

from client.models import Client
from medcard.models import MedicalCard
from medical_assistant.celery import app


@app.task
def create_medcard(*args, **kwargs):
    client = get_object_or_404(Client, user__id=kwargs.get("id"))

    MedicalCard.objects.create(client=client)
