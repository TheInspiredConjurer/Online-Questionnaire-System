from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class UserAdminModel(UserAdmin):
    list_display = (
        "id",
        "email",
        "username",
        "full_name",
        "date_joined",
        "last_login",
        "is_active",
        "is_staff",
        "is_superuser"
    )
    ordering = ("id", )


admin.site.register(User, UserAdminModel)
