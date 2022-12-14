from django.contrib import admin
from .models import *
class ConsumerAdmin(admin.ModelAdmin):
    list_display = ['username','email','password','is_seller']
admin.site.register(Consumer , ConsumerAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['consumer','name','price','discrip','image']
admin.site.register(Product , ProductAdmin)

class BuyerHistoryAdmin(admin.ModelAdmin):
    list_display = ['consumer','product','no_of_items','created_date']
admin.site.register(BuyerHistory , BuyerHistoryAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ['consumer','product','no_of_items']
admin.site.register(Cart , CartAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['consumer','address','shipping']
admin.site.register(Order , OrderAdmin)

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['consumer','address','state','city', 'zipcode', 'country']
admin.site.register(ShippingAddress , ShippingAddressAdmin)