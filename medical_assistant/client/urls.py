from django.urls import path, include
from rest_framework.routers import DefaultRouter

from client.views import ClientViewSet

router = DefaultRouter()
router.register("", ClientViewSet, basename="client")

urlpatterns = [
    path("client/", include(router.urls))
]
