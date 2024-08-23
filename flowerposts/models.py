from django.db import models

# Create your models here.
class FlowerPost(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.CASCADE,
        related_name='flowerposts'
    )
    upload_image = models.URLField()
    text = models.TextField(max_length=1000)
    owner = models.ForeignKey(
        'jwt_auth.User',
        on_delete=models.CASCADE,
        related_name='flowerposts_created'
    )

    def __str__(self):
        return f'{self.title}'