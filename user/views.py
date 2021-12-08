from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def user_dashboard(request):
    return render(request, 'user-dashboard.html')