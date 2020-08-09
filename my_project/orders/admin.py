from django.contrib import admin
from .models import TakeOrder, Order, OrderDetail, CurrentOrderList

# Register your models here.

admin.site.register(TakeOrder)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(CurrentOrderList)