from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    class Meta:
        verbose_name_plural = 'CustomUser'

    image = models.ImageField(default='NoImage.png')
    profile = models.TextField(verbose_name='プロフィール', null=True)