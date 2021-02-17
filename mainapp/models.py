# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="имя", unique=True, max_length=50)
    description = models.TextField(verbose_name="описание", max_length=1500, blank=True)
    date_create = models.DateTimeField(verbose_name="дата создания", auto_now=True)

    def __str__(self):
        return self.name


class Collections(models.Model):
    name = models.CharField(verbose_name="имя", max_length=100)
    description = models.TextField(verbose_name="описание", max_length=250, blank=True)
    year_of_issue_begin = models.IntegerField(verbose_name="год выпуска начало", default=0)
    year_of_issue_end = models.IntegerField(verbose_name="год выпуска конец", default=0)
    date_create = models.DateTimeField(verbose_name="дата создания", auto_now=True)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(verbose_name="имя", max_length=50)
    date_create = models.DateTimeField(verbose_name="дата создания", auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name="имя", max_length=100)
    description = models.TextField(verbose_name="описание", max_length=500, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, blank=True, default=None)
    price = models.DecimalField(verbose_name="цена продукта", default=0, decimal_places=2, max_digits=5)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    image = models.ImageField(verbose_name="изображение", upload_to="product_images", blank=True)
    file_product = models.FileField(verbose_name="файл продукта", upload_to="product_files", blank=True)
    year_of_issue = models.IntegerField(verbose_name="год выпуска", default=0)
    colection = models.ForeignKey(Collections, on_delete=models.SET_NULL, null=True, default=None)
    date_create = models.DateTimeField(verbose_name="дата создания", auto_now=True)

    def __str__(self):
        return self.name


class TagsProduct(models.Model):
    id_tag = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)
    id_product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Tag[{self.id_tag}] - Product[{self.id_product}]"
