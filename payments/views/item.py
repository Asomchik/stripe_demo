from django.views.generic import DetailView

from payments.models import Item


class ItemView(DetailView):
    model = Item
    template_name = 'item.html'
