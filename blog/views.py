from django.shortcuts import render

# Create your views here.

def blog(request):
    return render(request, "blog-list.html")

def blog_details(request):
    return render(request, "single-blog.html")