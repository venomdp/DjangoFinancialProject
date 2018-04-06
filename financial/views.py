from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Customer, Stock, Crypto
from rest_framework import viewsets
from .serializers import CustomerSerializer, StockSerializer
from .services import get_stock_price, get_crypto_price
from django import forms


def index(request):
    return render(request, 'financial/index.html')


def allCustomers(request):
    customer = Customer.objects.all
    return render(request, 'financial/customer.html', {'customer': customer})


def oneCustomer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    return render(request, 'financial/oneCustomer.html', {'customer': customer})


def stockView(request, customer_id, stock_id):
    stock = get_object_or_404(Stock, pk=stock_id)
    stock.currentPrice = get_stock_price(stock.symbol)
    return render(request, 'financial/stock.html', {'stock': stock})


def cryptoView(request, customer_id, crypto_id):
    crypto = get_object_or_404(Crypto, pk=crypto_id)
    crypto.currentPrice = get_crypto_price(crypto.symbol)
    return render(request, 'financial/crypto.html', {'crypto': crypto})

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

def customerEdit(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)




