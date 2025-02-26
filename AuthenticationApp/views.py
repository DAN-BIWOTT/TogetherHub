from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth import login
from .models import CustomUser
from django.contrib.auth.decorators import login_required
import sys

def sign_in(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, '🎉 Welcome back! You have successfully logged in.')
            return redirect('dashboard')  # Redirect to home/dashboard
        else:
            messages.error(request, '⚠️ Invalid email or password.')

    storage = get_messages(request)
    for message in storage:
        print(message)

    return render(request, "sign_in.html")

def sign_up(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        verify_password = request.POST.get('verify_password')
        membership = request.POST.get('membership')
        interest = request.POST.get('interest')

        if not membership:
            messages.error(request, "Please select a membership type.")
            return render(request, "sign_up.html", {
                "email": email,
                "membership": membership,
                "interest": interest,
            })
        
        if not verify_password:
            messages.error(request, "Please re-type the password.")
            return render(request, "sign_up.html", {
                "email": email,
                "membership": membership,
                "interest": interest,
            })
        
        if verify_password != password:
            messages.error(request, "Passwords do not match.")
            return render(request, "sign_up.html", {
                "email": email,
                "membership": membership,
                "interest": interest,
            })
        
        if not interest:
            messages.error(request, "Please select an interest.")
            return render(request, "sign_up.html", {
                "email": email,
                "membership": membership,
                "interest": interest,
            })

        if CustomUser.objects.filter(username=email).exists():
            messages.error(request, "Email is already registered")
        else:
            # Create user with extra fields
            user = CustomUser.objects.create_user(username=email, email=email, password=password, membership=membership, interest=interest)
            user.save()
    
            # Auto-login after sign-up
            login(request, user)

            messages.success(request, "Welcome to TogetherHub!")
            return redirect('dashboard')  # Redirecting to homepage

    return render(request, "sign_up.html")


def sign_out(request):
    logout(request)
    return redirect('sign_in')

@login_required  # Ensures only logged-in users can access home
def home(request):
    return render(request, 'home.html')