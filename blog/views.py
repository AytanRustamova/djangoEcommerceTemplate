from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Blog
# Create your views here.
@login_required
def blog(request):
    
    page = request.GET.get('page', 1)
    per_count = 2
    if page:
        page = int(page)
    blog = Blog.objects.all()[per_count*(page-1): page*per_count]
    return render(request, "blog-list.html", blogs=blog)
    

# @login_required
# def blog_details(request):
#     return render(request, "single-blog.html")


# class BlogListView(ListView):
#     model = Blog
#     template_name = 'blog-list.html'
#     context_object_name = 'blogs'
#     queryset = Blog.objects.filter(is_active = True)
#     paginate_by = 1
    
    
    