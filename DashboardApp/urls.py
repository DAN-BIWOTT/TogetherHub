from django.urls import path
from .views import dashboard, profile, manage_users, adminHome, manageEvents,manageMembers, adminNotifications, change_approval_state,addEvents, learning
from django.urls import path,include

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('manageUsers/', manage_users, name='manageUsers'),
    path("change_approval_state/", change_approval_state, name="change_approval_state"),
    path('adminHome/', adminHome, name='adminHome'),
    path('manageEvents/', manageEvents, name='manageEvents'),
    path('addEvents/', addEvents, name='addEvents'),
    path('manageMembers/', manageMembers, name='manageMembers'),
    path('adminNotifications/', adminNotifications, name='adminNotifications'),
    path('learning/', learning, name='learning'),
    ]
