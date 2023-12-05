"""stripe_demo URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from payments.views import (
    AddItemToOrderView,
    AllItemsView,
    AllOrdersView,
    BuyItemView,
    BuyOrderView,
    ItemView,
    OrderCreateView,
    OrderView,
    UpdateOrderOptionsView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AllItemsView.as_view(), name='catalog'),
    path('item/<int:pk>', ItemView.as_view(), name='item'),
    path('buy/<int:pk>', BuyItemView.as_view(), name='buy-item'),
    path('orders/', AllOrdersView.as_view(), name='orders'),
    path('order/<int:pk>', OrderView.as_view(), name='order'),
    path('add_item/', AddItemToOrderView.as_view(), name='add-item-to-order'),
    path('buy_order/<int:pk>', BuyOrderView.as_view(), name='buy-order'),
    path('create_order/', OrderCreateView.as_view(), name='create-order'),
    path('apply_discount/<int:pk>', UpdateOrderOptionsView.as_view(), name='apply-order-discount'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
