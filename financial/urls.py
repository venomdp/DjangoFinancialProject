from django.conf.urls import url
from . import views
from.models import Customer, Crypto, Stock

urlpatterns = [
    url(r'^$', views.index, name='mainpage'),
    url(r'^customer/', views.allCustomers, name='allcustomers'),
    url(r'^customer/\d+/', views.oneCustomer(Customer, Customer.id), name='onecustomer'),
    ]