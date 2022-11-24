import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django_resized import ResizedImageField


# Create your models here.
def profile_directory_path(instance, filename):
    return f'images/{instance.id}/profileImage/{filename}'


class User(AbstractUser):
    followings = models.ManyToManyField("self", symmetrical=False, related_name='followers')
    profile_image = ResizedImageField(size=[300, 300], upload_to=profile_directory_path, default="images/default.png", blank=True,)