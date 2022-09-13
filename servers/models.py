from django.db import models
from django.contrib.auth.models import User


class Server(models.Model):
    """
    Server Listing model
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    server_name = models.TextField(max_length=50)
    server_address = models.GenericIPAddressField(protocol='both', unpack_ipv4=True)
    created_date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(
        upload_to='images/', default='../default_server_banner_hfurfy', blank=True
    )

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.id} {self.server_name}'
