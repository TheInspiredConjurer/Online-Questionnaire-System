from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = User.objects.filter(id=user.id).all()

        if user.is_staff:
            queryset = User.objects.all()

        return queryset


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = User.objects.filter(id=user.id).all()

        if user.is_staff:
            queryset = User.objects.all()

        return queryset
