from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet)
router.register(r'stocks', views.StockViewSet)

urlpatterns = [
    url(r'^$', views.index, name='mainpage'),
    url(r'^customer/$', views.allCustomers, name='allcustomers'),
    url(r'^customer/(\d+)/$', views.oneCustomer, name='onecustomer'),
    url(r'^customer/(\d+)/s/(\d+)/$', views.stockView, name='stockview'),
    url(r'^customer/(\d+)/c/(\d+)/$', views.cryptoView, name='cryptoview'),
    url(r'api/', include(router.urls))
    ]