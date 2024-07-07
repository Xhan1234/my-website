import logging
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactMessage

logger = logging.getLogger(__name__)

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def services(request):
    return render(request, "service.html")

def projects(request):
    return render(request, "project.html")

def error_404(request):
    return render(request, "404.html")


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')  # Use the correct name here
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_success_view(request):
    return render(request, 'contact_success.html')