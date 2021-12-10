# User app views

from django.shortcuts import redirect, render
from . forms import RegistrationForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse_lazy

User = get_user_model()

# Create your views here.

def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password = form.cleaned_data.get('password1')
            user.save()
            messages.success(request, 'You are successfully registered.')
            return redirect(reverse_lazy('home:home'))
        # else:
        #     return redirect(reverse_lazy('user:login'))
    
    context = {
        'form' : form
    }
    return render(request, 'register.html', context)

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'user-dashboard.html')