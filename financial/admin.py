from django.contrib import admin
from .models import Customer, Crypto, Stock, TopTen


class stockInLine(admin.TabularInline):
    model = Stock
    extra = 0


class cryptoInLine(admin.TabularInline):
    model = Crypto
    extra = 0

@admin.register(Customer)


class customerAdmin(admin.ModelAdmin):
    inlines = [stockInLine, cryptoInLine]

@admin.register(TopTen)

class topTenAdmin(admin.ModelAdmin):
    inlines = []