from django.urls import path
<<<<<<< HEAD
from .views import dashboard, profile, manage_users, adminHome, manageEvents, manageMembers, change_approval_state
=======
from .views import dashboard, profile, manage_users, adminHome, manageEvents, manageMembers
>>>>>>> 5559b8e76a04c5b04b7d7f70070990ab04704720

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('manageUsers/', manage_users, name='manageUsers'),    
    path("change_approval_state/", change_approval_state, name="change_approval_state"),
    path('adminHome/', adminHome, name='adminHome'),
    path('manageEvents/', manageEvents, name='manageEvents'),
    path('manageMembers/', manageMembers, name='manageMembers'),
    ]
