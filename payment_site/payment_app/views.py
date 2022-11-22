import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import generic
from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY
YOUR_DOMAIN = 'http://127.0.0.1:8000'


class SuccessView(generic.TemplateView):
    template_name = "payment_app/success.html"


class CancelView(generic.TemplateView):
    template_name = "payment_app/cancel.html"


class MainView(generic.TemplateView):
    template_name = "payment_app/main.html"


class ItemListView(generic.ListView):
    model = Item
    context_object_name = 'item_list'


class ItemDetailView(generic.DetailView):
    model = Item
    context_object_name = 'item_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })

        return context

class CheckoutSessionView(generic.View):
    def post(self, request, pk, *args, **kwargs):
        item = Item.objects.get(id=pk)
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'rub',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': int(item.price),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({'id': session.id})
