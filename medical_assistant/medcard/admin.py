from django.contrib import admin

from medcard.models import MedicalCard, MedicalCardAppointment

admin.site.register(MedicalCard)
admin.site.register(MedicalCardAppointment)
