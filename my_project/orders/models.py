from django.db import models
from products.models import Product
import main_app.models

# Create your models here.

class TakeOrder(models.Model):
    productID = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, default=0)
    rate = models.IntegerField(null=True, default=0)
    total = models.IntegerField(null=True)


    def __str__(self):
        return self.productID.title


class OrderDetail(models.Model):
    productID = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, default=0 )
    rate = models.IntegerField(null=True, default=0)
    total = models.IntegerField(null=True)
    OrderID = models.IntegerField(null=True)
    
    


    def __str__(self):
        return self.productID.title

class CurrentOrderList(models.Model):
    customer_name = models.CharField(max_length=100, default='customer')
    order_id = models.IntegerField(null=True, default=0 )
    amount = models.IntegerField(null=True, default=0)
    Date_Time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.order_id)


class Order(models.Model):
    
    CustomerID = models.ForeignKey("main_app.Customer", on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    discount = models.IntegerField(null=True)
    net_amount = models.IntegerField(null=True)
    status = models.CharField(max_length=10, default='not paid')

    def __str__(self):
        return self.CustomerID.name


    


