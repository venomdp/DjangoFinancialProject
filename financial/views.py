from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Customer, Stock, Crypto


def index(request):
    return render(request, 'financial/index.html')


def allCustomers(request):
    customer = Customer.objects.all
    return render(request, 'financial/customer.html', {'customer': customer})


def oneCustomer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    return render(request, 'financial/oneCustomer.html', {'customer': customer})

