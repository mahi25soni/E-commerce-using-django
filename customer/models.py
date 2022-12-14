from django.db import models
from django.contrib.auth.models import User , AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from django.utils.timezone import now
class Consumer(User):
    is_seller = models.BooleanField(default=False , blank=True)
    class Meta:
        pass

class Product(models.Model):
    consumer = models.ForeignKey(Consumer , on_delete=models.CASCADE , blank=True , null=True)
    name = models.CharField(max_length=200, blank=True)
    price = models.PositiveIntegerField(blank=True)
    discrip = models.CharField(max_length= 1000, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name

# class ProductReview(models.Model):
#     product = models.ForeignKey(Product , on_delete=models.CASCADE , blank=True)
#     review = models.CharField(max_length=2000, blank=True)
#     rating = models.IntegerField(default=1, validators=[MaxValueValidator(5),MinValueValidator(0)] , blank=True)

class Cart(models.Model):
    consumer = models.ForeignKey(Consumer , on_delete=models.CASCADE , blank=True , null=True)
    product = models.ForeignKey(Product , on_delete=models.CASCADE , blank=True)
    no_of_items = models.IntegerField(default=0,  null=True, blank=True)

    def item_total(self):
        return self.product.price*self.no_of_items

class BuyerHistory(models.Model):
    consumer = models.ForeignKey(Consumer , on_delete=models.CASCADE , blank=True , null=True)
    product = models.ForeignKey(Product , on_delete=models.CASCADE , blank=True)
    no_of_items = models.IntegerField(default=0,  null=True, blank=True)
    created_date = models.DateTimeField(default=now , blank=True)

class ShippingAddress(models.Model):
    consumer = models.ForeignKey(Consumer , on_delete=models.CASCADE , blank=True , null=True)
    address = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    zipcode = models.IntegerField(blank=True)
    country = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.address


class Order(models.Model):
    consumer = models.ForeignKey(Consumer , on_delete=models.CASCADE , blank=True , null=True)
    address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE , blank=True , null=True)
    shipping = models.BooleanField(default=False, blank=True)
    