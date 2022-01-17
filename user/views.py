# User app views
from django.shortcuts import redirect, render
from django.core.mail.message import sanitize_address
from . forms import RegistrationForm,LoginForm
from django.contrib.auth import get_user_model, authenticate, login as django_login, logout as django_logout
from django.contrib import messages
from django.urls import reverse_lazy
from user.tasks import send_confirmation_mail
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from user.tools.token import account_activation_token
from django.http import HttpResponseRedirect

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
    
    
    
def login(request):
    redirect_to = request.GET.get('next', ' ')
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user= authenticate(username= email, password=password)
            if user:
                django_login(request, user)
                messages.success(request, 'Siz ugurla login oldunuz.')
                return HttpResponseRedirect(redirect_to) 
            else:
                messages.success(request, 'Siz login ola bilmediniz.')
    context = {
        'form':form,
    }
    return render(request, 'login.html', context)


def logout(request):
    django_logout(request)
    return redirect(reverse_lazy('user:login'))
    