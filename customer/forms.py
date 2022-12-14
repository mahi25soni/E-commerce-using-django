from django import forms
from .models import Consumer , Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm , UsernameField

class ConsumerForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Passoword'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    class Meta:
        model = Consumer
        fields = ['username','email','password1','password2','is_seller']
        widgets = {
            'username': forms.TextInput(attrs = {'class':'form-control','placeholder':'Name'}),
            'email': forms.EmailInput(attrs = {'class':'form-control','placeholder':'Email'}),
        }
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Password',
        }
))

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['consumer','name','price','discrip','image']
        widgets = {
            'name': forms.TextInput(attrs = {'class':'form-control','placeholder':'Name'}),
            'price': forms.NumberInput(attrs = {'class':'form-control','placeholder':'Price'}),
            'discrip': forms.Textarea(attrs = {'class':'form-control','placeholder':'Discription'}),
        }
