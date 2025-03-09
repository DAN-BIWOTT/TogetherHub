from django.urls import path
from .views import dashboard, profile, manage_users, adminHome

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('manageUsers/', manage_users, name='manageUsers'),
    path('adminHome/', adminHome, name='adminHome'),
    ]
