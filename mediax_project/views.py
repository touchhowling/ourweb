from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

def connect(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            description = form.cleaned_data['description']

            message = f"""
Name: {name}
Email: {email}
Phone: {phone}

Message:
{description}
"""

            send_mail(
                "New Contact Form Submission",
                message,
                email,
                ["desarka.co.in@gmail.com"],
            )

            return render(request,"connect.html",{"success":True})

    else:
        form = ContactForm()

    return render(request,"connect.html",{"form":form})