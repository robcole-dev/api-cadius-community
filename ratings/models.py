from django.db import models
from django.contrib.auth.models import User
from servers.models import Server


class Rating(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    one = models.PositiveIntegerField(default=0, null=True, blank=True)
    two = models.PositiveIntegerField(default=0, null=True, blank=True)
    three = models.PositiveIntegerField(default=0, null=True, blank=True)
    four = models.PositiveIntegerField(default=0, null=True, blank=True)
    five = models.PositiveIntegerField(default=0, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['server']
    
    def __str__(self):
        rating_list = {
            '1': self.one,
            '2': self.two,
            '3': self.three,
            '4': self.four,
            '5': self.five
        }
        return str(max(rating_list, key=rating_list.get))