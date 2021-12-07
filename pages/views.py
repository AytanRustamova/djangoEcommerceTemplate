from django.shortcuts import render

# Create your views here.

def error(request):
    return render(request, '404.html')

def account_setting(request):
    return render(request, 'account-setting.html')

def checkout(request):
    return render(request, 'checkout.html')

def faq(request):
    return render(request, 'faq.html')

def shopping_cart(request):
    return render(request, 'shopping-cart.html')

def wishlist(request):
    return render(request, 'wishlist.html')