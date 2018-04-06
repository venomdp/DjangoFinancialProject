from django import forms
from .models import Customer, Crypto, Stock

class EditCustomerForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    address = forms.CharField(max_length=50)
    city = forms.CharField(max_length=30)
    state = forms.CharField(max_length=30)
    zip = forms.DecimalField(max_digits=5, decimal_places=0)
    email = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=12)

    class Meta:
        model = Customer
        fields = ['name', 'address', 'city', 'state', 'zip', 'email', 'phone']


class EditStockForm(forms.ModelForm):
    symbol = forms.CharField(max_length=6)
    name = forms.CharField(max_length=30)
    numShares = forms.DecimalField(max_digits=10, decimal_places=0)
    buyPrice = forms.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Stock
        fields = ['symbol', 'name', 'numShares', 'buyPrice']


class EditCryptoForm(forms.ModelForm):
    symbol = forms.CharField(max_length=6)
    name = forms.CharField(max_length=30)
    numCoins = forms.DecimalField(max_digits=15, decimal_places=4)
    buyPrice = forms.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        model = Crypto
        fields = ['symbol', 'name', 'numCoins', 'buyPrice']