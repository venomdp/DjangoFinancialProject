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


