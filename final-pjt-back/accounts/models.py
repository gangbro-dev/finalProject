from django.contrib.auth.models import AbstractUser
from django.db import models
from django_resized import ResizedImageField

# Create your models here.

class User(AbstractUser):
    followings = models.ManyToManyField("self", symmetrical=False, related_name='followers')
    profile_image = ResizedImageField(size=[300, 300], upload_to='whatever', null=True, blank=True,)
    