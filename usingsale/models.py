from django.db import models
from django.contrib.auth.models import User


class ProductShop(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='productshop')
    name =models.CharField(max_length=20)
    info = models.CharField(max_length=100)
    price = models.IntegerField(blank=False)
    foto = models.ImageField(upload_to="user_product/", blank=True, default='/media/default.jpg')

    def __str__(self):
        return "/".join((self.name, self.owner))
