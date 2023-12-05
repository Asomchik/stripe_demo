from django.views.generic.edit import UpdateView

from payments.models import Order


class UpdateOrderOptionsView(UpdateView):
    model = Order
    fields = ['discount', 'tax', 'currency']
