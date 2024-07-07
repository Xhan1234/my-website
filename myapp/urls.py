from django.urls import path
from . import views
from .views import contact_view, contact_success_view

urlpatterns = [
    path("", views.index, name='home'),
    path("about/", views.about, name='about'),
    path("services/", views.services, name='services'),
    path("projects/", views.projects, name='projects'),
    path("error_404/", views.error_404, name='error_404'),
    path('contact/', contact_view, name='contact'),  # Define once
    path('contact/success/', contact_success_view, name='contact_success'),
]
