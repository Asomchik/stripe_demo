from django import forms

from payments.models import OrderContent, Item


class OrderContentForm(forms.ModelForm):
    item = forms.ModelChoiceField(queryset=Item.objects.all())

    class Meta:
        model = OrderContent
        fields = ['order', 'item', 'quantity']
        widgets = {
            'order': forms.HiddenInput(),
        }
