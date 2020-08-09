from django.shortcuts import render, redirect
from products.models import Product
from django.http import HttpResponse
from .models import TakeOrder,Order,OrderDetail,CurrentOrderList
from main_app.models import Customer
from . import forms
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='accounts:login')
def add_order(request):
    

    take_order = TakeOrder()
    products = Product.objects.all()

    items = TakeOrder.objects.all()
    form = forms.Checkout()
    discount = request.GET.get('discount')

    gross_amount = int(0)
    net_amount = gross_amount
    
    
    
    
    if request.method == 'POST':
        product = request.POST.get('product')
        quantity = request.POST.get('quantity')
        
        # amount = None

        
        for p in products:
            if p.title == product:
                quantity = int(quantity)
                amount = p.price*quantity
                rate = p.price
                product = p
        

        
        
        take_order.productID = product
        take_order.quantity = quantity
        take_order.rate = rate
        take_order.total = amount
        take_order.save()
        items = TakeOrder.objects.all()

        # gross_amount = int(0)
        # net_amount = gross_amount

        #Calculating gross amount

        for amount in items:
            if gross_amount:
                gross_amount = gross_amount + amount.total
            else:
                gross_amount = amount.total

        net_amount = gross_amount

        
        # Calculating discount

        if discount:
            discount = int(discount)
            discount = gross_amount*discount/100
            discount = int(discount)
            net_amount = gross_amount - discount
            
        else:
            net_amount = gross_amount
            
            
        # net_amount = gross_amount
        # request.session['net_amount'] = net_amount



        return render(request,'orders/orderform.html',{'products':products,
                                                        'product': product,
                                                        'quantity':quantity,
                                                         'rate':rate,
                                                         'amount':amount,
                                                         'items':items,
                                                         'gross_amount':gross_amount,
                                                         'net_amount':net_amount,
                                                         'form':form
                                                         })

    # gross_amount = int(0)
    # net_amount = gross_amount


    for amount in items:
        if gross_amount:
            gross_amount = gross_amount + amount.total
        else:
            gross_amount = amount.total

    request.session['discount'] = discount

     
    if discount:
        discount = int(discount)
        print('THIS IS THE DISCOUNT: ',discount)
        print(type(discount))
        print('THIS IS THE GROSS AMOUNT: ',gross_amount)
        print(type(gross_amount))
        print('THIS IS THE NET AMOUNT: ',net_amount)
        print('                                 ')

        discount = gross_amount*discount/100
        print('THIS IS THE DISCOUNT AFTER: ',discount)
        discount = int(discount)
        print(type(discount))

        net_amount = gross_amount - discount
        print('THE NET AMOUNT AFTER: ',net_amount)
        print(type(net_amount))
        
    else:
        net_amount = gross_amount
        

    # net_amount = gross_amount


    
        



    return render(request,'orders/orderform.html',{'products':products,
                                                    'items':items,
                                                    'gross_amount':gross_amount,
                                                    'net_amount':net_amount,
                                                    'form':form})


def add_item(request):

    if request.method=='POST':

        product = request.POST['product']
        quantity = request.POST['quantity']
        rate = request.POST['rate']
        amount = request.POST['amount']

        TakeOrder.objects.create(
            productID = product,
            quantity = quantity,
            rate = rate,
            total = amount
        )

    return HttpResponse('')


def clear_item(request):
    TakeOrder.objects.all().delete()
    return redirect('orders:add_order')
    


def delete_takeorder(request, pk):

    product = TakeOrder.objects.filter(id=pk)

    if pk:
        product.delete()
        return redirect('orders:add_order')



    items = TakeOrder.objects.all()

    context = {

        'items':items
    }


    return render(request,'orders/orderform.html',{'context':context})
    



@login_required(login_url='accounts:login')
def checkout(request):


    customer = Customer()
    order = Order()
    order_detail = OrderDetail()
    rough_order = TakeOrder()
    current_order = CurrentOrderList()
    form = forms.Checkout() 

    items = TakeOrder.objects.all()

   
    discount = request.session['discount']
    if discount != None:
        discount = int(discount)
    

    gross_amount = int(0)
    net_amount = gross_amount




    if request.method == 'POST':
        

        for amount in items:
            if gross_amount:
                gross_amount = gross_amount + amount.total
            else:
                gross_amount = amount.total
        
        if discount != None:
            discount = gross_amount*discount/100
            discount = int(discount)
            net_amount = gross_amount - discount
        else:
            net_amount = gross_amount

            
        form = forms.Checkout(request.POST)

        if form.is_valid():

            form.save(commit=True)
            order.CustomerID = Customer.objects.all().last()
            order.discount = discount
            order.net_amount = net_amount
            order.save()

            Rough_Order = TakeOrder.objects.all()

            for item in TakeOrder.objects.all():
                # order_detail.productID = item.productID
                # order_detail.quantity = item.quantity
                # order_detail.rate = item.rate
                # order_detail.total = item.total
                # order_detail.OrderID = Order.objects.all().last().id
                # order_detail.save()
                productID = item.productID
                quantity = item.quantity
                rate = item.rate
                total = item.total
                OrderID = Order.objects.all().last().id
                b=OrderDetail( productID=productID, quantity =quantity, rate =rate, total = total,OrderID =OrderID )
                b.save()
            
            

            TakeOrder.objects.all().delete()

            c = Customer.objects.all().last()
            o = Order.objects.all().last()
            
            current_order.customer_name = c.name
            current_order.order_id = o.id
            current_order.amount = o.net_amount
            current_order.Date_Time = o.order_date
            current_order.save() 



            latest_order = Order.objects.all().last()
            order_id = latest_order.id




            # customer.name = form.cleaned_data['name']
            return render(request,'orders/checkout.html',{'form':form,'order_id':order_id})
            
        
            
    else:
        form = forms.Checkout() 

    return render(request,'orders/checkout.html',{'form':form,'net_amount':net_amount})



def current_order_list(request):

    order_list = CurrentOrderList.objects.all()
    products = OrderDetail.objects.all()


    return render(request,'orders/current-order-list.html',{'order_list':order_list,'products':products})


def action(request, pk):

    row = CurrentOrderList.objects.filter(id=pk)
    order_list = CurrentOrderList.objects.all()
    order_detail = OrderDetail.objects.all()
    # products = OrderDetail.objects.all()



    if request.method == 'POST':

        order_id = request.POST.get('order_id')  
        





        if request.POST.get('confirm'):

            order_id = request.POST.get('order_id')   
            print('THIS IS THE ORDER ID: ',order_id)
            order = Order.objects.filter(id=order_id)
            
            for o in order:
                o.status = 'paid'
                o.save()

            row.delete()
            return redirect('orders:current-order-list')

        elif request.POST.get('cancel'):

            order_id = request.POST.get('order_id')   
            print('THIS IS THE ORDER ID: ',order_id)
            order = Order.objects.filter(id=order_id)
            
            for o in order:
                o.status = 'canceled'
                o.save()

            row.delete()
            return redirect('orders:current-order-list')


        # elif request.POST.get('order_detail'):

        #     order_id = request.POST.get('order_id')
        #     products = OrderDetail.objects.filter(OrderID=row.order_id)

        #     return render(request,'orders/current-order-list.html',{'products':products,})  

        



    return render(request,'orders/current-order-list.html',{'order_list':order_list,'order_detail':order_detail})



def view_orders(request):
    orders = Order.objects.all()


    return render(request,'orders/view-orders.html',{'orders':orders})




