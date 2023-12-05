from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Title')
    iso = models.CharField(max_length=3, unique=True, verbose_name='Currency ISO code')

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return self.iso
