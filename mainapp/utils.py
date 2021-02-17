import random
from .models import ProductCategory, Product


def get_menu():
    return ProductCategory.objects.all()


def get_catalog():
    return Product.objects.all()


def get_slice_catalog():
    catalog = []
    rand_index_list = []
    CATALOG = list(get_catalog())
    while True:
        if len(catalog) == 6:
            break

        rand_index = random.randint(0, len(CATALOG) - 1)
        if rand_index in rand_index_list:
            continue
        else:
            catalog.append(CATALOG[rand_index])
            rand_index_list.append(rand_index)
    return catalog
