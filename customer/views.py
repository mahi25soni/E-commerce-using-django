from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Consumer,Product, Cart, Order, ShippingAddress, BuyerHistory
from .utils import gettingimfo
from django.contrib.auth.decorators import login_required
from .basicview import *
import json

#REQUEST.POST is a dictionary of our entered data
#request.user.is_authenticated:


@login_required(login_url='login')
def home(request):
    try:
        name = Consumer.objects.get(username = request.user)
    except Consumer.DoesNotExist:
        name = None
    if ( name!=None and name.is_seller==True):
        return HttpResponseRedirect('/seller/')
    else:
        data = Product.objects.all()
        cart = Cart.objects.filter(consumer = request.user)
        total_data = gettingimfo(cart)
        return render(request , 'customer/home.html',{'form':data,'data':total_data})

@login_required(login_url='login')
def cart(request):
    cart = Cart.objects.filter(consumer = request.user)
    total_data = gettingimfo(cart)
    return render(request , 'customer/cart.html', {'cart':cart,'data':total_data})
    

@login_required(login_url='login')
def checkout(request):
    cart = Cart.objects.filter(consumer = request.user)
    total_data = gettingimfo(cart)
    order= Order.objects.get_or_create(consumer=request.user.consumer, shipping=False)

    return render(request , 'customer/checkout.html', {'cart':cart,'data':total_data,'order':order})
   


def add_to_cart(request , pk):
    user = request.user.consumer
    body = json.loads(request.body)
    value = body['value']


    product = Product.objects.get(id=pk)
    cart, created = Cart.objects.get_or_create(consumer= user,product=product)
    
    number_of_items = cart.no_of_items
    if number_of_items >= 0:
        if value == 'add':
            cart.no_of_items +=  1
        if value == 'minus':
            cart.no_of_items -=  1
    cart.save()

    if cart.no_of_items == 0 or value=='remove':
        cart.delete()

    order, created = Order.objects.get_or_create(consumer=user, shipping=False)
     
    if Cart.objects.filter(consumer= user).count() == 0:
        order.delete()
            
    return HttpResponseRedirect('/')


def process_order(request):
    user = request.user.consumer
    data = json.loads(request.body)
    shipping = data['shipping-info']
    shippingaddress, created = ShippingAddress.objects.get_or_create(
        consumer = user,
        address = shipping['address'],
        state = shipping['state'],
        city = shipping['city'],
        zipcode = shipping['zipcode'],
        country =  shipping['country']
    )

    order = Order.objects.get(consumer=user, shipping = False)
    print(order)
    order.address = shippingaddress
    order.shipping = True
    order.save()
    print(order)

    for x in Cart.objects.filter(consumer= user):
        same = BuyerHistory(consumer=x.consumer, product=x.product, no_of_items=x.no_of_items)
        same.save()

    Cart.objects.filter(consumer= user).delete()        
    return HttpResponseRedirect('/')

