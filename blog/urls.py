from django.urls import path
from .views import blog, blog_details

app_name = 'blog'

urlpatterns = [
    path('', blog, name='blog'),
    path('blog-details/', blog_details, name='blog_details'),
]