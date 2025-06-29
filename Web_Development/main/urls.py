from django.urls import path
from . import views

# This file defines the URL patterns for the main application.
# It maps the root URL to the home view function, which renders the home.html template.

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]
