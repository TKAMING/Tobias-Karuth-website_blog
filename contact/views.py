from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail

def contact(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        msg = request.POST.get("msg")

        #if name.is_valid() and email.is_valid() and msg.is_valid():
        html = render_to_string("email/emailcontact.html", {
            "name": name,
            "email": email,
            "msg": msg
        })
        # sends email
        send_mail("Websie Contact Form", "this is the message", "noreply@tobiaskaruth.com", ["tobiaskaruth@gmail.com"], html_message=html)
        return redirect("contact")

    return render(request, "contact.html")

