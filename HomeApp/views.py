from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from DashboardApp.models import Event  

# Create your views here.
def index(request):
    latest_events = Event.objects.order_by('-created_at')[:2]  # Corrected query
    return render(request, "index.html", {"latest_events": latest_events})
