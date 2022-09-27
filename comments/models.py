from django.db import models
from django.contrib.auth.models import User
from tutorials.models import Tutorial


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_date']
