from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from user.views import UserAuthViewSet, UserInfoViewSet

router = DefaultRouter()
router.register("info", UserInfoViewSet, basename="user-info")
router.register("", UserAuthViewSet, basename="user-auth")

urlpatterns = [
    path("user/", include(router.urls)),
    path("register/", UserViewSet.as_view({"post": "create"}), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("activation/", UserViewSet.as_view({"post": "activation"}), name="activation"),
    path("resend-activation/", UserViewSet.as_view({"post": "resend_activation"}), name="resend_activation"),
    path("user/reset-username/", UserViewSet.as_view({"post": "reset_username"}), name="reset_username"),
    path("user/reset-username-confirm/", UserViewSet.as_view({"post": "reset_username_confirm"})),
    path("user/reset-password/", UserViewSet.as_view({"post": "reset_password"}), name="reset_password"),
    path("user/reset-password-confirm/", UserViewSet.as_view({"post": "reset_password_confirm"})),
]
