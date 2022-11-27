from django import forms
from payments.models import Order, Discount, Tax, Currency


class OrderForm(forms.ModelForm):
    discount = forms.ModelChoiceField(queryset=Discount.objects.all(), required=False)
    tax = forms.ModelChoiceField(queryset=Tax.objects.all(), required=False)
    currency = forms.ModelChoiceField(queryset=Currency.objects.all(), required=True)

    class Meta:
        model = Order
        fields = ['discount', 'tax', 'currency']
