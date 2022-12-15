
from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index,name='index'),
    path('signin/',views.login, name='login'),
    path('signup/', views.register,name='register'),
    path('logout/', views.logout, name='logout'),
    path('about/',views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('shop/', views.shop, name='shop'),
    path('thankyou/', views.thankyou, name='thankyou'),
]