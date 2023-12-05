# from django.shortcuts import redirect
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from payments.models import Order, Currency


class OrderCreateView(View):

    def get(self, request, *args, **kwargs):
        new_order = Order.objects.create(currency=Currency.objects.get(iso='USD'))
        return HttpResponseRedirect(reverse('order', kwargs={'pk': new_order.id}))
