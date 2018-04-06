from .models import Customer, Stock, Crypto
from rest_framework import serializers

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'email', 'stock_set')

class StockSerializer(serializers.HyperlinkedModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.name')
    class Meta:
        model = Stock
        fields = ('symbol', 'numShares', 'customer')