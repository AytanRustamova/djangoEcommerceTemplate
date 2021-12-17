from django.urls import path, re_path
from .views import logout, register, login, dashboard, activate, logout

app_name = 'user'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,33})/$',
            activate, name='activate'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout, name='logout')
    
]
