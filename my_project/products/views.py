from django.shortcuts import render, redirect
from .models import Product
from . import forms

# Create your views here.

def products(request):
    products = Product.objects.all()

    if request.method == 'POST':
        form = forms.AddProduct(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('products:products')
    else:
        form = forms.AddProduct()
    return render(request,'products/products.html',{'products':products,'form':form})