from django.shortcuts import render
from .models import Post

def whoami(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})
