from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from djoser.serializers import UidAndTokenSerializer
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from rest_framework.validators import UniqueValidator

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True)
    confirmation_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "type",
            "password",
            "confirmation_password",
        )
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
            "type": {"required": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["confirmation_password"]:
            raise serializers.ValidationError({"detail": "Passwords don't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            type=validated_data["type"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "type",
        )
        read_only_fields = ('email',)


class ActivationSerializer(UidAndTokenSerializer):
    def validate(self, attrs):
        attrs = super().validate(attrs)
        if not self.user.email_confirmed:
            self.user.email_confirmed = True
            return attrs
        raise PermissionDenied("stale_token")


class PasswordResetConfirmSerializer(UidAndTokenSerializer):
    new_password = serializers.CharField(style={"input_type": "password"})
    confirmation_new_password = serializers.CharField(style={"input_type": "password"})

    def validate(self, attrs):
        user = self.context["request"].user or self.user
        assert user is not None

        if attrs["new_password"] != attrs["confirmation_new_password"]:
            raise serializers.ValidationError({"detail": "Passwords don't match."})

        try:
            validate_password(attrs["new_password"], user)
        except django_exceptions.ValidationError as e:
            raise serializers.ValidationError({"new_password": list(e.messages)})
        return super().validate(attrs)
