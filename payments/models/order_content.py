from django.db import models

from .order import Order
from .item import Item


class OrderContent(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Order')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Product')
    quantity = models.IntegerField(blank=False, null=False, verbose_name='Quantity')

    class Meta:
        verbose_name = "Order's Product"
        verbose_name_plural = "Orders' Products"

    def __str__(self):
        return f'{self.item} in {self.order}'
