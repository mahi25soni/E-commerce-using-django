from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('seller/' , views.seller , name='seller' ),
    path('delete_seller_product/<int:pk>' , views.delete_seller_product , name='delete_seller_product' ),
    path('cart/', views.cart , name='cart'),
    path('check/', views.checkout , name='checkout'),
    path('login/' , views.logIn , name='login' ),
    path('signup/' , views.SignUp, name='signup' ),
    path('logout/' , views.logOut, name='logout' ),
    path('profile/' , views.profile, name='profile' ),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('process_order/', views.process_order, name='process_order'),
    path('buyer_history/', views.buyer_history, name='buyer_history'),

]