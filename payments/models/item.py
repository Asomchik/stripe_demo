from django.db import models
from django.urls import reverse_lazy


class Item(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Product')
    description = models.TextField(blank=False, null=False, verbose_name='Description')
    price = models.IntegerField(blank=False, null=False, verbose_name='Price in cents')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name[:30]

    def get_absolute_url(self):
        return reverse_lazy('item', kwargs={'pk': self.id})

    def price_display(self):
        return '{0:.2f}'.format(self.price / 100)
