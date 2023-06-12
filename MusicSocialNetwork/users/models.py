from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', default='avatars/User.png')
    phone = models.CharField(max_length=20, blank=True, null=True)
    bio = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
