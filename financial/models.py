from django.db import models
from datetime import date


class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip = models.DecimalField(max_digits=5, decimal_places=0)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Stock(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    symbol = models.CharField(max_length=6)
    name = models.CharField(max_length=30)
    numShares = models.DecimalField(max_digits=10, decimal_places=0)
    buyPrice = models.DecimalField(max_digits=10, decimal_places=2)
    buyDate = models.DateField(default=date.today())


class Crypto(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    symbol = models.CharField(max_length=6)
    name = models.CharField(max_length=30)
    numCoins = models.DecimalField(max_digits=15, decimal_places=4)
    buyPrice = models.DecimalField(max_digits=7, decimal_places=2)
    buyDate = models.DateField(default=date.today())