from django import forms
from main_app.models import Customer
from .models import Order


class Checkout(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','address','email','phone','city','state','country']




class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['discount','net_amount']
