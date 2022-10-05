from rest_framework.viewsets import ModelViewSet


from .models import User
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = User.objects.filter(id=user.id).all()

        if user.is_staff:
            queryset = User.objects.all()

        return queryset
