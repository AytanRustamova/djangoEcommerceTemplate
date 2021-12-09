from django.shortcuts import render
from . forms import RegistrationForm

# Create your views here.

def register(request):
    # form = RegistrationForm()
    # context = {
    #     'form' : form
    # }
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'user-dashboard.html')