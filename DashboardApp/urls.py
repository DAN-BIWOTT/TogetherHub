from django.urls import path
from .views import dashboard, profile, manage_users, adminHome, manageEvents, manageMembers, change_approval_state

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('manageUsers/', manage_users, name='manageUsers'),    
    path("change_approval_state/", change_approval_state, name="change_approval_state"),
    path('adminHome/', adminHome, name='adminHome'),
    path('manageEvents/', manageEvents, name='manageEvents'),
    path('manageMembers/', manageMembers, name='manageMembers'),
    ]
