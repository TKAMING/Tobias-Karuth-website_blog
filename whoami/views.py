from django.shortcuts import render

def whoami(request):
    return render(request, "index.html")
