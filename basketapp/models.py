from django.conf import settings
from django.db import models


from mainapp.models import Product


class BasketQuerySetManager(models.QuerySet):
    def delete(self):
        for object in self:
            object.product.quantity += object.quantity
            object.product.save()
        super().delete()


class Basket(models.Model):
    objects = BasketQuerySetManager.as_manager()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="basket")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="количество", default=0)
    add_datetime = models.DateTimeField(verbose_name="время добавления", auto_now_add=True)

    @property
    def product_cost(self):
        "return cost of all products this type"
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        "return total quantity for user"
        return sum(list(map(lambda x: x.quantity, self.user.basket.all())))

    @property
    def total_cost(self):
        "return total cost for user"
        return sum(list(map(lambda x: x.product_cost, self.user.basket.all())))

    @classmethod
    def get_item(cls, pk):
        try:
            return cls.objects.get(pk=pk)
        except Exception as e:
            print(e)

    def save(self, *args, **kwargs):
        if self.pk:
            self.product.quantity -= self.quantity - \
                                     self.__class__.get_item(self.pk).quantity
        else:
            self.product.quantity -= self.quantity
        self.product.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.product.quantity += self.quantity
        self.product.save()
        super().delete()
