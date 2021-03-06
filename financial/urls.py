from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet)
router.register(r'stocks', views.StockViewSet)
router.register(r'cryptos', views.CryptoViewSet)

urlpatterns = [
    url(r'^$', views.index, name='mainpage'),
    url(r'^customer/$', views.allCustomers, name='allcustomers'),
    url(r'^customer/(\d+)/$', views.oneCustomer, name='onecustomer'),
    url(r'^customer/(\d+)/s/(\d+)/$', views.stockView, name='stockview'),
    url(r'^customer/(\d+)/c/(\d+)/$', views.cryptoView, name='cryptoview'),
    url(r'api/', include(router.urls)),
    url(r'^customer/(\d+)/update', views.customerEdit, name='customerupdate'),
    url(r'^customer/(\d+)/s/(\d+)/update', views.stockEdit, name='stockupdate'),
    url(r'^customer/(\d+)/c/(\d+)/update', views.cryptoEdit, name='cryptoupdate'),
    url(r'^topten/(\d+)/', views.topTen, name='topten'),
    url(r'^customer/(\d+)/s/(\d+)/delete', views.stockDelete, name='stockdelete'),
    url(r'^customer/(\d+)/c/(\d+)/delete', views.cryptoDelete, name='cryptodelete'),
    url(r'^customer/(\d+)/delete', views.customerDelete, name='customerdelete'),
    ]