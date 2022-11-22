from django.urls import path
from .views import (
    ItemListView,
    ItemDetailView,
    CheckoutSessionView,
    MainView,
    SuccessView,
    CancelView
    )


urlpatterns = [
    path(route='payment_app/item_list/', view=ItemListView.as_view(),
         name='item-list'),
    path(route='payment_app/item_list/item/<int:pk>/', view=ItemDetailView.as_view(),
         name='item-detail'),
    path(route='payment_app/item_list/buy/<int:pk>/',
         view=CheckoutSessionView.as_view(), name='buy'),
    path(route='', view=MainView.as_view(), name='main'),
    path(route='success/', view=SuccessView.as_view(), name='success'),
    path(route='cancel/', view=CancelView.as_view(), name='cancel')
]
