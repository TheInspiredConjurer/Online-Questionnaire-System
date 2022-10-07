from rest_framework.routers import DefaultRouter

from .views import UserViewSet, RoleViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('roles', RoleViewSet)

urlpatterns = [] + router.urls
