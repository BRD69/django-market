from django.urls import path, re_path

import ordersapp.views as ordersapp

from .apps import OrdersappConfig

app_name = OrdersappConfig.name

urlpatterns = [
    re_path(r'^$', ordersapp.OrderList.as_view(), name='index'),
    re_path(r'^create/$', ordersapp.OrderItemsCreate.as_view(), name='order_create'),
    re_path(r'^read/(?P<pk>\d+)/$', ordersapp.OrderRead.as_view(), name='order_read'),
    re_path(r'^update/(?P<pk>\d+)/$', ordersapp.OrderItemsUpdate.as_view(), name='order_update'),
    re_path(r'^delete/(?P<pk>\d+)/$', ordersapp.OrderDelete.as_view(), name='order_delete'),
]
