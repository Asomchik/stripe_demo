from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import View
import json

from payments.models import Order
from payments.services import PaymentServices


class BuyOrderView(View):

    def get(self, request, *args, **kwargs):
        order = get_object_or_404(Order, pk=self.kwargs.get('pk'))
        domain = request.build_absolute_uri('/')[:-1]
        cancel_url = domain + reverse('order', kwargs={'pk': order.id})
        success_url = domain + reverse('catalog')
        stripe_session = PaymentServices.get_stripe_payment_session(
            order, cancel_url, success_url
        )
        return HttpResponse(
            json.dumps({'session_id': stripe_session.id}),
            content_type="application/json"
        )
