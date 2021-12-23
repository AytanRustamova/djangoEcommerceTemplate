from django.urls import path
from . views import  blog_details, BlogListView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('blog-details/', blog_details, name='blog_details'),
]