from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class FlowerPost(models.Model):
    title = models.CharField(max_length=100)
    category = ArrayField(models.CharField(max_length=20), size=8)
    upload_image = models.URLField()
    text = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.title}'