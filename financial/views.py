from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Customer, Stock, Crypto, TopTen
from rest_framework import viewsets
from .serializers import CustomerSerializer, StockSerializer, CryptoSerializer
from .services import get_stock_price, get_crypto_price
from django import forms
from .forms import EditCustomerForm, EditStockForm, EditCryptoForm, DeleteCryptoForm, DeleteCustomerForm, DeleteStockForm


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

class CryptoViewSet(viewsets.ModelViewSet):
    queryset = Crypto.objects.all()
    serializer_class = CryptoSerializer

def customerEdit(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == "POST":
        form = EditCustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save()
            return redirect(f'/customer/{customer_id}', pk=customer_id)
    else:
        form = EditCustomerForm(instance=customer)
    return render(request, 'financial/update_form.html', {'form': form})


def customerDelete(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == "POST":
        form = DeleteCustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer.delete()
            return redirect(f'/customer/', pk=customer_id)
    else:
        form = EditCustomerForm(instance=customer)
    return render(request, 'financial/delete_form.html', {'form': form})


def stockEdit(request, customer_id, stock_id):
    stock = get_object_or_404(Stock, pk=stock_id)
    if request.method == "POST":
        form = EditStockForm(request.POST, instance=stock)
        if form.is_valid():
            stock = form.save()
            return redirect(f'/customer/{customer_id}')
    else:
        form = EditStockForm(instance=stock)
    return render(request, 'financial/update_form.html', {'form': form})

def stockDelete(request, customer_id, stock_id):
    stock = get_object_or_404(Stock, pk=stock_id)
    if request.method == "POST":
        form = DeleteStockForm(request.POST, instance=stock)
        if form.is_valid():
            stock.delete()
            return redirect(f'/customer/{customer_id}')
    else:
        form = DeleteStockForm(instance=stock)
    return render(request, 'financial/delete_form.html', {'form': form})


def cryptoDelete(request, customer_id, crypto_id):
    crypto = get_object_or_404(Crypto, pk=crypto_id)
    if request.method == "POST":
        form = DeleteCryptoForm(request.POST, instance=crypto)
        if form.is_valid():
            crypto.delete()
            return redirect(f'/customer/{customer_id}')
    else:
        form = DeleteCryptoForm(instance=crypto)
    return render(request, 'financial/delete_form.html', {'form': form})


def cryptoEdit(request, customer_id, crypto_id):
    crypto = get_object_or_404(Crypto, pk=crypto_id)
    if request.method == "POST":
        form = EditCryptoForm(request.POST, instance=crypto)
        if form.is_valid():
            form = form.save()
            return redirect(f'/customer/{customer_id}')
    else:
        form = EditCryptoForm(instance=crypto)
    return render(request, 'financial/update_form.html', {'form': form})

def topTen(request, topten_id):
    topten = get_object_or_404(TopTen, pk=topten_id)
    topten.currentPrice1 = get_stock_price('AAPL')
    topten.symbol1 = 'AAPL'
    topten.name1 = 'Apple'
    topten.currentPrice2 = get_stock_price('GOOG')
    topten.symbol2 = 'GOOG'
    topten.name2 = 'Google'
    topten.currentPrice3 = get_stock_price('TSLA')
    topten.symbol3 = 'TSLA'
    topten.name3 = 'Tesla'
    topten.currentPrice4 = get_stock_price('MSFT')
    topten.symbol4 = 'MSFT'
    topten.name4 = 'Microsoft'
    topten.currentPrice5 = get_stock_price('AMZN')
    topten.symbol5 = 'AMZN'
    topten.name5 = 'Amazon'
    topten.currentPrice6 = get_crypto_price('BTC')
    topten.symbol6 = 'BTC'
    topten.name6 = 'Bitcoin'
    topten.currentPrice7 = get_crypto_price('ETH')
    topten.symbol7 = 'ETH'
    topten.name7 = 'Ethereum'
    topten.currentPrice8 = get_crypto_price('XRP')
    topten.symbol8 = 'XRP'
    topten.name8 = 'Ripple'
    topten.currentPrice9 = get_crypto_price('BCH')
    topten.name9 = 'Bitcoin Cash'
    topten.symbol9 = 'BCH'
    topten.currentPrice10 = get_crypto_price('LTC')
    topten.symbol10 = 'LTC'
    topten.name10 = 'Litecoin'
    return render(request, 'financial/topten.html', {'topten': topten})






