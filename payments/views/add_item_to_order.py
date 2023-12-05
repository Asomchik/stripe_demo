from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from payments.models import OrderContent


class AddItemToOrderView(CreateView):
    model = OrderContent
    fields = ['order', 'item', 'quantity']

    def form_valid(self, form):
        if form.is_valid():
            order = form.cleaned_data['order']
            item = form.cleaned_data['item']
            quantity = form.cleaned_data['quantity']

            if content := OrderContent.objects.filter(order=order, item=item).first():
                self._change_quantity(content, quantity)
            else:
                self._add_new_item(order, item, quantity)

            return HttpResponseRedirect(reverse_lazy('order', kwargs={'pk': order.pk}))

    def _change_quantity(self, content, quantity):
        if quantity >= 0:
            content.quantity += quantity
            content.save()
            return

        if (new_quantity := quantity + content.quantity) <= 0:
            content.delete()
            return
        content.quantity = new_quantity
        content.save()

    def _add_new_item(self, order, item, quantity):
        if quantity >= 0:
            OrderContent.objects.create(order=order, item=item, quantity=quantity)
