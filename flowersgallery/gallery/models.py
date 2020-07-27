from django.db import models


class Flower(models.Model):
    '''
    title
    image
    description
    '''
    title = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()

