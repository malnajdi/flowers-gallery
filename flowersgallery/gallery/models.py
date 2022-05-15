from django.db import models

class FlowersWithImageManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(image='')


class Flower(models.Model):
    class Meta:
        permissions = [('test_flower', 'Test Flower')]
        
    '''
    title
    image
    description
    '''
    title = models.CharField(max_length=100)
    title_ar = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    description_ar = models.TextField()
    user = models.ForeignKey(
        'interaction.User',
        on_delete=models.CASCADE
        )
    
    objects = models.Manager()
    with_images = FlowersWithImageManager()

    def __str__(self):
        return self.title