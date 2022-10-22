from django.shortcuts import render
from .models import Post

def blog(request):
    return render(request, "blog/blog.html")
