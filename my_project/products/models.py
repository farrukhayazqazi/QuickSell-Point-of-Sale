from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.ImageField(default='default.png')

    def __str__(self):
        return self.title

    def snippet(self):
        return self.description[0:50] + '...'