from django.db import models
from django.contrib.auth.models import User


class Tutorial(models.Model):
    """
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=50)
    description = models.TextField(max_length=250)
    video = models.FileField(upload_to='videos/', blank=True, verbose_name='')
    image = models.ImageField(upload_to='images/', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.id} {self.title}'