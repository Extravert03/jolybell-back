from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('username', 'first_name', 'last_name')


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.UserProfile
        fields = '__all__'
        depth = 1


class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=6, max_length=64)
    password = serializers.CharField(min_length=8, max_length=128)

    class Meta:
        model = models.User
        fields = ('username', 'password')
