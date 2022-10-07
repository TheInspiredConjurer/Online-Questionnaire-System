from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Role


class UserAdminModel(UserAdmin):
    list_display = (
        "id",
        "email",
        "username",
        "full_name",
        "date_joined",
        "last_login",
        # "role",
        "is_active",
        "is_staff",
        "is_superuser"
    )
    ordering = ("-id", )


class RoleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "role",
        "user"
    )
    ordering = ("-id", )
    list_filter = ("user", )


admin.site.register(User, UserAdminModel)
admin.site.register(Role, RoleAdmin)
