
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ConsumerForm, UserLoginForm, ProductForm
from .models import Consumer,Product, ShippingAddress, BuyerHistory
from .utils import gettingimfo
from django.contrib.auth import authenticate , login , logout 


def logIn(request):
    if request.method == 'POST':
        logindata = UserLoginForm(data = request.POST)
        if logindata.is_valid():
            username = logindata.cleaned_data.get('username')
            password = logindata.cleaned_data.get('password')
            user = authenticate(request , username = username , password = password)
            if user is not None:
                login(request , user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('no hoga')
    else:
        logindata = UserLoginForm()
    return render(request , 'customer/login.html',{'form':logindata})

def SignUp(request):
    if request.method == 'POST':
        formdata = ConsumerForm(data = request.POST)
        if formdata.is_valid():
            formdata.save()
            return HttpResponseRedirect('/')
    else:
        formdata = ConsumerForm()
    return render(request , 'customer/signup.html',{'form':formdata})

def logOut(request):
    logout(request)
    return HttpResponseRedirect('/')

def buyer_history(request):
    user = request.user.consumer
    history = BuyerHistory.objects.filter(consumer=user).order_by('-created_date')
    return render(request , 'customer/buyerhistory.html', {'form':history})


def profile(request):
    user = request.user.consumer
    try:
        name = Consumer.objects.get(username = request.user)
    except Consumer.DoesNotExist:
        name = None
        
    if ( name!=None and name.is_seller==True):
        data = Product.objects.filter(consumer = user)
        return render(request , 'customer/sellerhistory.html', {'form':data})
    else:
        Person = Consumer.objects.get(username = user)
        Address = ShippingAddress.objects.filter(consumer = user)
        return render(request , 'customer/profile.html',{'user':Person,'addresses':Address})

def seller(request):
    user = request.user.consumer
    if request.method == 'POST':
        productdata = ProductForm(request.POST , request.FILES)
        if productdata.is_valid():
            name = productdata.cleaned_data['name']
            price = productdata.cleaned_data['price']
            image = productdata.cleaned_data['image']
            discrip = productdata.cleaned_data['discrip']
            reg = Product(consumer = user, name=name, price=price, image=image, discrip=discrip)
            reg.save()
            return HttpResponseRedirect('/')
    else:
        productdata = ProductForm()
        return render(request , 'customer/seller.html', {'form':productdata})

def delete_seller_product(request , pk):
    Product.objects.get(id=pk).delete()
    return HttpResponseRedirect('/profile/')

