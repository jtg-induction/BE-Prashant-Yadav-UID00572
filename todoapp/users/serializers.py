from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import make_password

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from users import (
    models as user_models
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_models.CustomUser
        fields = ['id', 'first_name', 'last_name', 'email']


class UserSerializerWithoutIdField(serializers.ModelSerializer):
    class Meta:
        model = user_models.CustomUser
        fields = ['first_name', 'last_name', 'email']


class UserPendingTodosSerializer(serializers.ModelSerializer):
    pending_count = serializers.IntegerField()

    class Meta:
        model = user_models.CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'pending_count']


class UserProjectSerializer(serializers.ModelSerializer):
    to_do_projects = serializers.ListField()
    in_progress_projects = serializers.ListField()
    completed_projects = serializers.ListField()

    class Meta:
        model = user_models.CustomUser
        fields = [
            "first_name", "last_name", "email",
            "to_do_projects", "in_progress_projects",
            "completed_projects"
        ]


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=True)
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = user_models.CustomUser
        fields = [
            'email', 'password', 'first_name', 'last_name', 'date_joined', 'token'
        ]
        read_only_fields = ['date_joined']

    def create(self, validated_data):
        user = user_models.CustomUser.objects.create_user(**validated_data)
        return user

    def get_token(self, instance):
        token, _ = Token.objects.get_or_create(user=instance)
        return token.key


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
