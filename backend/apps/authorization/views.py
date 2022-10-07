from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import CustomTokenObtainPairSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = AllowAny
    serializer_class = CustomTokenObtainPairSerializer
