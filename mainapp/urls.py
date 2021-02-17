from django.urls import path

import mainapp.views as mainapp

from .apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", mainapp.products, name="index"),
    path("category/<int:pk>/", mainapp.products, name="category"),
]
