from django.db import models


class Tax(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Tax')
    value = models.IntegerField(blank=False, null=False, verbose_name='Tax Percentage')

    class Meta:
        verbose_name = 'Tax'
        verbose_name_plural = 'Taxes'

    def __str__(self):
        return f'{self.name} {self.value} %'
