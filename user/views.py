# User app views
from django.shortcuts import redirect, render
from django.core.mail.message import sanitize_address
from . forms import RegistrationForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse_lazy
from user.tasks import send_confirmation_mail
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from user.tools.token import account_activation_token

User = get_user_model()

# Create your views here.

def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password = form.cleaned_data.get('password1')
            user.is_active = False
            user.save()
            site_address = request.is_secure() and "https://" or "http://" + request.META['HTTP_HOST']  # https
            send_confirmation_mail(user_id=user.id, site_address=site_address)
            messages.success(request, 'You are successfully registered.')
            return redirect(reverse_lazy('home:home'))
        else:
            messages.error(request, 'Invalid form submission.')
    
    context = {
        'form' : form
    }
    return render(request, 'register.html', context)

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'user-dashboard.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Email is activated')
        return redirect(reverse_lazy('home:home'))
    elif user:
        messages.error(request, 'Email is not activated.')
        return redirect(reverse_lazy('user:register'))
    else:
        messages.error(request, 'Email is not activated')
        return redirect(reverse_lazy('user:register'))