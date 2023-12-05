from django.views.generic import ListView
from payments.models import Item


class AllItemsView(ListView):
    model = Item
    template_name = 'catalog.html'

    def get_queryset(self):
        return Item.objects.order_by('id')
