# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings

import datetime
import random
from mainapp import utils
from .models import ProductCategory, Product
from basketapp.models import Basket


# Create your views here.


def main(request):
    title = "Главная"
    now_year = datetime.datetime.now().year
    phone = "+7 (123) 456-78-90"
    email = "info@mc.com"
    random_image = ["background-dc.jpg", "background-marvel.jpg", "background-dc.jpg", "background-marvel.jpg"][
        random.randint(0, 3)
    ]
    catalogs = utils.get_slice_catalog()

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    content = {
        "title": title,
        "now_year": now_year,
        "links_menu": utils.get_menu(),
        "phone": phone,
        "email": email,
        "random_image": random_image,
        "catalogs": catalogs,
        "media_url": settings.MEDIA_URL,
        "basket": basket,
    }
    return render(request, "mainapp/index.html", content)


def products(request, pk=None):
    title = "Каталог"
    links_menu = ProductCategory.objects.all()

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            catalogs = Product.objects.all()
        else:
            catalogs = Product.objects.filter(category__pk=pk).order_by("date_create") 
    content = {
        "title": title,
        "catalogs": catalogs,
        "links_menu": links_menu,
        "media_url": settings.MEDIA_URL,
        "basket": basket,
    }
    return render(request, "mainapp/catalog.html", content)


def contact(request):
    title = "Наши контакты"
    location = [
        {
            "city": "г. Санкт-Петербург",
            "address": "Санкт-Петербург, пр. Невский 1",
            "phone": "+7 (123) 456-78-90",
            "schedule": "ежедневно с 9:00 до 22:00",
        },
    ]
    content = {
        "title": title,
        "location": location[0],
        "links_menu": utils.get_menu(),
    }
    return render(request, "mainapp/contact.html", content)


def about(request):
    title = "О нас"
    content = {
        "title": title,
        "links_menu": utils.get_menu(),
    }
    return render(request, "mainapp/about.html", content)
