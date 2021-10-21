from django.db import models
from django.contrib.auth.models import AbstractUser
from gallery.models import Flower
from django.conf import settings

class User(AbstractUser, models.Model):
    website = models.URLField(null=False)

    def __str__(self):
        return self.username


class Action(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    flower = models.ForeignKey(to=Flower, on_delete=models.CASCADE, related_name='actions')
    liked = models.BooleanField(null=True)

    class Meta:
        unique_together = ['user', 'flower']

    

