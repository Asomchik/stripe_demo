from django.db import models


class Discount(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Title')
    value = models.IntegerField(blank=False, null=False, verbose_name='Discount Percentage')

    class Meta:
        verbose_name = 'Discount'
        verbose_name_plural = 'Discounts'

    def __str__(self):
        return f'{self.name} {self.value} %'
