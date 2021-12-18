from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/user/login/')
def blog(request):
    return render(request, "blog-list.html")

@login_required(login_url='/user/login/')
def blog_details(request):
    return render(request, "single-blog.html")