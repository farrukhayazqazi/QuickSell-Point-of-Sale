from django.urls import path
from . import views

app_name = 'orders'


urlpatterns = [

    path('add_order/',views.add_order,name='add_order'),

    path('add_item/',views.add_item,name='add_item'),


    path('clear_item/',views.clear_item,name='clear_item'),
    
    path('action/<int:pk>/',views.action,name='action'),
    
    path('delete_takeorder/<int:pk>/',views.delete_takeorder,name='delete_takeorder'),
    
    path('checkout/',views.checkout,name='checkout'),


    path('current-order-list/',views.current_order_list,name='current-order-list'),

    path('view-order/',views.view_orders,name='view-order'),
]