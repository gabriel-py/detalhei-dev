from djoser.serializers import UserCreateSerializer, UserFunctionsMixin
from django.contrib.auth import get_user_model
from .models import UserAccount
from rest_framework import serializers
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserAccount
        fields = '__all__'