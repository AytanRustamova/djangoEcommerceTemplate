from django.contrib import admin
from blog.models import Blog
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

"""shopery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls", namespace='home')),
    path('blog/', include("blog.urls", namespace='blog')),
    path('about/', include("about.urls", namespace='about')),
    path('contact/', include("contact.urls", namespace='contact')),
    path('product/', include("product.urls", namespace='product')),
    path('pages/', include("pages.urls", namespace='pages')),
    path('user/', include("user.urls", namespace='user')),
    path('social-auth/', include('social_django.urls', namespace="social")),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

