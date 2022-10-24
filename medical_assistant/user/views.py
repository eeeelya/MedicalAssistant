import requests
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from user.models import User
from user.serializers import UserInfoSerializer
from user.permissions import PermissionsForUser
from core.mixins import DeactivateModelMixin


class UserInfoViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    DeactivateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = UserInfoSerializer
    permission_classes = (IsAuthenticated, PermissionsForUser)

    def get_queryset(self):
        return User.objects.filter(is_active=True)


class UserAuthViewSet(viewsets.GenericViewSet):
    permission_classes = (AllowAny,)

    @action(detail=False, methods=["get"], url_path=r"activate/(?P<uid>[\w-]+)/(?P<token>[\w-]+)")
    def activate_account(self, request, uid, token):
        protocol = "https://" if request.is_secure() else "http://"
        web_url = protocol + request.get_host()
        post_url = web_url + "/api/v1/activation/"
        post_data = {"uid": uid, "token": token}
        response = requests.post(post_url, data=post_data)

        return Response(response.text, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"], url_path=r"password/reset/confirm/(?P<uid>[\w-]+)/(?P<token>[\w-]+)")
    def reset_password(self, request, uid, token):
        protocol = "https://" if request.is_secure() else "http://"
        web_url = protocol + request.get_host()
        post_url = web_url + "/api/v1/user/reset-password-confirm/"
        post_data = {
            "uid": uid,
            "token": token,
            "new_password": request.data["new_password"],
            "confirmation_new_password": request.data["confirmation_new_password"],
        }
        response = requests.post(post_url, data=post_data)

        return Response(response.content, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"], url_path=r"username/reset/confirm/(?P<uid>[\w-]+)/(?P<token>[\w-]+)")
    def reset_username(self, request, uid, token):
        protocol = "https://" if request.is_secure() else "http://"
        web_url = protocol + request.get_host()
        post_url = web_url + "/api/v1/user/reset-username-confirm/"
        post_data = {"uid": uid, "token": token, "new_email": request.data["new_email"]}
        response = requests.post(post_url, data=post_data)

        return Response(response.content, status=status.HTTP_200_OK)
