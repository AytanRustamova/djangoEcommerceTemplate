from django.urls import path
from .views import product, product_details

app_name = 'product'

urlpatterns = [
    path('', product, name='product'),
    path('product_details/',  product_details, name=' product_details'),
]
