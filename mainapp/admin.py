# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ProductCategory, Product, Collections, Tags, TagsProduct

# Register your models here.

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Collections)
admin.site.register(Tags)
admin.site.register(TagsProduct)
