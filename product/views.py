from django.shortcuts import render

# Create your views here.

def product(request):
    return render(request, "product.html")

def product_details(request):
    return render(request, "product_details.html")



