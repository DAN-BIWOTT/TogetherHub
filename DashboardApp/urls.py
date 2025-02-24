from django.urls import path
from .views import dashboard
from .views import profile

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
]
