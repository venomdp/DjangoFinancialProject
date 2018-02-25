from django.conf.urls import url
from . import views
from.models import Customer, Crypto, Stock

urlpatterns = [
    url(r'^$', views.index, name='mainpage'),
    url(r'^customer/', views.allCustomers, name='allcustomers')
]