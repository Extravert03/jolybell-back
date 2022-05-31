from django.contrib.auth import logout, login, authenticate
from rest_framework import views, permissions, authentication, status
from rest_framework.response import Response

from . import models, serializers


class UserProfileView(views.APIView):
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.BasicAuthentication,
    )
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, *args, **kwargs):
        user_profile = models.UserProfile.objects.get(user=self.request.user)
        serializer = serializers.UserProfileSerializer(user_profile)
        return Response(serializer.data)


class LogoutView(views.APIView):

    def get(self, *args, **kwargs):
        logout(self.request)
        return Response(status=status.HTTP_200_OK)


class LoginView(views.APIView):

    def post(self, *args, **kwargs):
        username = self.request.data.get('username')
        password = self.request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        login(self.request, user)
        return Response(status=status.HTTP_200_OK)


class RegisterView(views.APIView):

    def post(self, *args, **kwargs):
        serializer = serializers.UserRegisterSerializer(data=self.request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        user.set_password(self.request.data['password'])
        user.save()
        models.UserProfile.objects.create(user=user)
        login(self.request, user)
        return Response(status=status.HTTP_201_CREATED)
