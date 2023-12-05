from django.views.generic import ListView

from payments.models import Order


class AllOrdersView(ListView):
    model = Order
    template_name = 'all_orders.html'

    def get_queryset(self):
        return Order.objects.order_by('id')
