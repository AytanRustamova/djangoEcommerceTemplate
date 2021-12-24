from django.urls import path
from .views import  BlogListView
from blog import views
app_name = 'blog'

urlpatterns = [
    path('', views.blog , name='blog'),
    
]