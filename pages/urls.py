from django.urls import path
from .views import error, account_setting, checkout, faq, shopping_cart, wishlist

app_name = 'pages'

urlpatterns = [
    path('error/', error, name='error'),
    path('account_setting/', account_setting, name='account_setting'),
    path('checkout/', checkout, name='checkout'),
    path('faq/', faq, name='faq'),
    path('shopping_cart/', shopping_cart, name='shopping_cart'),
    path('wishlist/', wishlist, name='wishlist'),
]
