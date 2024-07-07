# myapp/admin.py
from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'project', 'created_at')  # Assuming created_at is a DateTimeField in ContactMessage
