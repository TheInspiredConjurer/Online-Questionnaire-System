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

    def create(self, request, *args, **kwargs):
        userprofile = Profile.objects.create(user=User.objects.get(id=request.data.pop('user')), **request.data)
        return Response(
            data={
                "id": userprofile.id,
                "role": userprofile.role,
                "university_name": userprofile.university_name,
                "about": userprofile.about,
                "profile_picture": userprofile.profile_picture if userprofile.profile_picture else None,
                "user": userprofile.user_id
            },
            status=201
        )

    def get_queryset(self):
        user = self.request.user
        queryset = Profile.objects.filter(id=user.id).all()

        if user.is_staff:
            queryset = Profile.objects.all()

        return queryset
