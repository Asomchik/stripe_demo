import stripe
from settings.settings import STRIPE_SECRET_KEY


class PaymentServices:

    @classmethod
    def get_stripe_payment_session(cls, order, cancel_url, success_url):
        stripe.api_key = STRIPE_SECRET_KEY
        discount_id = cls._apply_discount(order)
        tax_id = cls._apply_tax(order)
        currency = order.currency.iso.lower()

        if tax_id:
            line_items = [
                {'price_data': {
                    'currency': currency,
                    'product_data': {'name': order_content.item.name, },
                    'unit_amount': order_content.item.price, },
                    'tax_rates': [tax_id],
                    'quantity': order_content.quantity, }
                for order_content in order.ordercontent_set.all()
            ]
        else:
            line_items = [
                {'price_data': {
                    'currency': currency,
                    'product_data': {'name': order_content.item.name, },
                    'unit_amount': order_content.item.price, },
                    'quantity': order_content.quantity, }
                for order_content in order.ordercontent_set.all()
            ]

        session = stripe.checkout.Session.create(
            line_items=line_items,
            mode='payment',
            discounts=[{
                'coupon': discount_id}
            ],
            success_url=success_url,
            cancel_url=cancel_url
        )
        return session

    @classmethod
    def _apply_discount(cls, order):
        if order.discount:
            stripe.api_key = STRIPE_SECRET_KEY
            coupon = stripe.Coupon.create(
                percent_off=order.discount.value, duration='once'
            )
            return coupon.id

    @classmethod
    def _apply_tax(cls, order):
        if order.tax:
            stripe.api_key = STRIPE_SECRET_KEY
            tax = stripe.TaxRate.create(
                display_name=order.tax.name, inclusive=False,
                percentage=order.tax.value
            )
            return tax.id
