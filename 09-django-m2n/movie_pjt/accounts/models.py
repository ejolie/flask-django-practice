from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __str__(self):
        return self.username

class User_Followers_User(models.Model):
    from_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='to_users')