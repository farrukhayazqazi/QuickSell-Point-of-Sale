from django.conf.urls import url
from . import views

app_name = 'products'


urlpatterns = [

    url(r'^products/$',views.products,name='products'),
]