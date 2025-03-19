from django.urls import path
from .views import events_home

urlpatterns = [
    path('', events_home, name='events_home'),  # This URL pattern will be used in the template
]