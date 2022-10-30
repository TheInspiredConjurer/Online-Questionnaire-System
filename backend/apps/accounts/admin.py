from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Profile


class UserAdminModel(UserAdmin):
    list_display = (
        "id",
        "email",
        "username",
        "date_joined",
        "last_login",
        "is_active",
        "is_staff",
        "is_superuser"
    )
    ordering = ("-id", )


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "role",
        "university_name",
    )
    ordering = ("-id", )
    search_fields = ("user__email", )


admin.site.register(Profile, ProfileAdmin)
admin.site.register(User, UserAdminModel)
