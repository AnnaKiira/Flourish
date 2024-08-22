from django.db import models

# Create your models here.
class Comment(models.Model):
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    flowerpost = models.ForeignKey(
        'flowerposts.FlowerPost',
        on_delete=models.CASCADE,
        related_name='comments'
    )