# forms.py
from django import forms
from .models import ContactMessage  # Adjust the import as per your model name

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'project', 'message']
