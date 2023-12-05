from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from payments.models import Item, Order, OrderContent, Currency


class BuyItemView(View):

    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Item, pk=self.kwargs.get('pk'))
        order = Order.objects.create(currency=Currency.objects.get(iso='USD'))
        OrderContent.objects.create(order=order, item=item, quantity=1)
        return HttpResponseRedirect(reverse('buy-order', kwargs={'pk': order.id}))
