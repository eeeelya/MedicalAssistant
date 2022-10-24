from django.urls import path, include
from rest_framework.routers import DefaultRouter

from medcard.views import MedCardViewSet, MedCardAppointmentViewSet

router = DefaultRouter()
router.register("", MedCardViewSet, basename="med-card")
router.register("appointments", MedCardAppointmentViewSet, basename="med-card-appointment")

urlpatterns = [
    path("medcard/", include(router.urls))
]
