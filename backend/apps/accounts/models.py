import os

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from PIL import Image

from .choices import ROLE_CHOICES
from .managers import UserManager
from .validators import path_and_rename


class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=45)
    username = models.CharField(max_length=12, blank=True)
    first_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = ("-id", )

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    university_name = models.CharField(max_length=2000, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to=path_and_rename, blank=True, null=True)

    class Meta:
        ordering = ("-id", )

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        super().save()

        if self.profile_picture:
            img = Image.open(self.profile_picture.path)
            if img.height > 512 or img.height > 512:
                output_size = (512, 512)
                img.thumbnail(output_size)
                img.save(self.profile_picture.path)


@receiver(pre_save, sender=Profile)
def delete_old_profile_picture(sender, instance, **kwargs):
    # on creation, signal callback won't be triggered
    if instance._state.adding and not instance.pk:
        return False

    try:
        old_profile_picture = sender.objects.get(pk=instance.pk).profile_picture
    except sender.DoesNotExist:
        return False

    # comparing the new file with the old one
    profile_picture = instance.profile_picture or None

    try:
        if not old_profile_picture == profile_picture:
            if os.path.isfile(old_profile_picture.path):
                os.remove(old_profile_picture.path)
    except Exception as e:
        return False
