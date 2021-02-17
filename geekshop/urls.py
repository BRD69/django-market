"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

import mainapp.views as mainapp


urlpatterns = [
    # path(r'admin/', admin.site.urls),
    path("", mainapp.main, name='main'),
    path("products/", include("mainapp.urls", namespace="products")),
    path("contact/", mainapp.contact, name='contact'),
    path("about/", mainapp.about, name='about'),
    path("auth/", include("authapp.urls", namespace="auth")),
    path("basket/", include("basketapp.urls", namespace="basket")),
    path("myadmin/", include("adminapp.urls", namespace="myadmin")),
    path("auth/veryfy/", include('social_django.urls', namespace='social')),
    path("orders/", include('ordersapp.urls', namespace='orders')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
