from django.db import models
from orders.models import Order



# Create your models here.


class Customer(models.Model):
    name = models.CharField('Full Name',max_length=100)
    address = models.CharField("Address",max_length=1024,default=None)
    phone = models.CharField('Phone',max_length=11,default=None)
    email = models.EmailField(max_length = 254)
    city = models.CharField("City",max_length=1024,)
    state = models.CharField("State",max_length=1024,)
    country = models.CharField("Country",max_length=1024,)

    def __str__(self):
        return self.name
