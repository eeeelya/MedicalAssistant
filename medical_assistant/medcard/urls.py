from django.urls import include, path
from rest_framework.routers import DefaultRouter

from medcard.views import MedCardAppointmentViewSet, MedCardViewSet

router = DefaultRouter()
router.register("", MedCardViewSet, basename="med-card")
router.register("appointments", MedCardAppointmentViewSet, basename="med-card-appointment")

urlpatterns = [path("medcard/", include(router.urls))]
