from django.urls import path, include
from rest_framework.routers import DefaultRouter

from appointment.views import AppointmentViewSet


router = DefaultRouter()
router.register("", AppointmentViewSet, basename="appointment")

urlpatterns = [
    path("appointment/", include(router.urls))
]
