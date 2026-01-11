from .forms import ContactForm
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Email send
            send_mail(
                f"New message from {name}",
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['recipient_email@example.com'],  # jahan mail bhejna hai
                fail_silently=False,
            )
            return render(request, 'success.html')  # simple success page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
