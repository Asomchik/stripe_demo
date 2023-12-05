from django.db import models
from django.urls import reverse_lazy

from .currency import Currency
from .discount import Discount
from .tax import Tax


class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date of order')
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Discount')
    tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tax')
    currency = models.ForeignKey(
        Currency,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        verbose_name='Currency',
        # default=Currency.objects.get(name='USD')
    )

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'Order №{self.id}'

    def get_absolute_url(self):
        return reverse_lazy('order', kwargs={'pk': self.id})

    def total(self):
        total = sum(content.quantity * content.item.price for content in self.ordercontent_set.all())
        return '{0:.2f}'.format(total / 100)
