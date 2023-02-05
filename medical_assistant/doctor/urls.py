from django.urls import include, path
from rest_framework.routers import DefaultRouter

from doctor.views import DoctorViewSet

router = DefaultRouter()
router.register("", DoctorViewSet, basename="doctor")

urlpatterns = [
    path("doctor/", include(router.urls)),
]
