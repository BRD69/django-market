from django.urls import path, re_path

import basketapp.views as basketapp

from .apps import BasketappConfig

app_name = BasketappConfig.name

urlpatterns = [
    re_path(r'^$', basketapp.index, name='index'),
    re_path(r'^add/(?P<pk>\d+)/$', basketapp.add, name='add'),
    re_path(r'^remove/(?P<pk>\d+)/$', basketapp.remove, name='remove'),
    re_path(r'^update/(?P<pk>\d+)/(?P<quantity>\d+)/$', basketapp.update),
]
