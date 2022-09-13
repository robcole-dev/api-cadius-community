from django.db import models
from django.contrib.auth.models import User
from servers.models import Server


class Rating(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['server']
        