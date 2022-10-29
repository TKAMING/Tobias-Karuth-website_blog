from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail

def contact(request):
    return render(request, "contact.html")

