from django.contrib import admin

from payments.models import Currency, Discount, Item, Order, OrderContent, Tax


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'iso')


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    list_filter = ('value',)
    search_fields = ['name', ]


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ['name', ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'currency', 'date', 'discount', 'tax', 'order_subtotal')
    list_filter = ('discount', 'tax')
    list_display_links = ('id', 'date', 'order_subtotal')

    def order_subtotal(self, instance):
        return instance.total()


class OrderContentAdmin(admin.ModelAdmin):
    list_display = ('order', 'item', 'quantity')
    list_filter = ('item', 'order')


class TaxAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    list_filter = ('value',)


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderContent, OrderContentAdmin)
admin.site.register(Tax, TaxAdmin)
