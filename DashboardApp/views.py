from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def profile(request):
    interests = ["Technology", "Photography", "Gaming", "Cooking", "Fitness", 
                 "Travel", "Fashion", "Music", "Art", "Writing", "DIY", "Coding"]
    return render(request, 'profile.html', {"interests": interests})