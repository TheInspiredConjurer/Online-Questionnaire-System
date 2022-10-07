from django.contrib.auth.models import AbstractUser
from django.db import models

from .choices import ROLE_CHOICES
from .managers import UserManager


class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=45)
    username = models.CharField(max_length=12, blank=True)
    full_name = models.CharField(max_length=60, blank=True)
    address = models.CharField(max_length=80, blank=True)
    role = models.CharField(max_length=25, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, editable=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = ("id", )

    def __str__(self):
        return self.email
