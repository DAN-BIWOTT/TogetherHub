from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import login
from .models import CustomUser
from django.contrib.auth.decorators import login_required

def sign_in(request):
    # if request.method == 'POST':
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     user = authenticate(request, username=email, password=password)

    #     if user is not None:
    #         login(request, user)
    #         return redirect('dashboard')  # Redirect to home/dashboard
    #     else:
    #         messages.error(request, "Invalid email or password")

    return render(request, "sign_in.html")

def sign_up(request):
    # if request.method == 'POST':
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     membership = request.POST['membership']
    #     interest = request.POST['interest']

    #     if CustomUser.objects.filter(username=email).exists():
    #         messages.error(request, "Email is already registered")
    #     else:
    #         # Create user with extra fields
    #         user = CustomUser.objects.create_user(username=email, email=email, password=password, membership=membership, interest=interest)
    #         user.save()

    #         # Auto-login after sign-up
    #         login(request, user)

    #         messages.success(request, "Welcome to TogetherHub!")
    #         return redirect('dashboard')  # Redirect to homepage

    return render(request, "sign_up.html")


def sign_out(request):
    logout(request)
    return redirect('sign_in')

# @login_required  # Ensures only logged-in users can access home
# def home(request):
#     return render(request, 'home.html')