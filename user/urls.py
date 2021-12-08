from django.urls import path
from .views import register, login,user_dashboard

app_name = 'user'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('user-dashoard/', user_dashboard, name='user_dashboard')
]
