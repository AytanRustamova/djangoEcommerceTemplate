from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()
class Blog(models.Model):
    title = models.CharField(max_length=100,)
    content = models.TextField(max_length=500)
    image = models.ImageField(upload_to='blog/')
    is_active = models.BooleanField(default=False)
    
# def __str__(self):
#     return self.title 