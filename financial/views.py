from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Stock, Crypto


def index(request):
    customers = Customer.objects.all
    return render(request, 'financial/index.html', {'customers': customers})


