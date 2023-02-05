from django.urls import include, path
from rest_framework.routers import DefaultRouter

from receptionist.views import ReceptionistViewSet

router = DefaultRouter()
router.register("", ReceptionistViewSet, basename="receptionist")

urlpatterns = [path("receptionist/", include(router.urls))]
