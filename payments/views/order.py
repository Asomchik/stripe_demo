from django.views.generic import DetailView

from payments.forms import OrderContentForm, OrderForm
from payments.models import Order


class OrderView(DetailView):
    model = Order
    template_name = 'order.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        order = Order.objects.get(pk=self.kwargs.get('pk'))
        context['add_item_form'] = OrderContentForm(initial={'order': order})
        context['order_form'] = OrderForm(
            initial={
                'discount': order.discount,
                'tax': order.tax,
                'currency': order.currency,
            }
        )
        return context
