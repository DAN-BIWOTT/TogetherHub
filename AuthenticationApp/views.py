from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth import login
from .models import CustomUser
from django.contrib.auth.decorators import login_required
import sys
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()

def sign_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # No need to pass 'username' anymore, just 'email'
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, '🎉 Welcome back! You have successfully logged in.')
            if user.membership == "admin":
                return redirect('adminHome')
            else:
                return redirect('dashboard')  # Redirect to home/dashboard
        else:
            messages.error(request, '⚠️ Invalid email or password')

    storage = get_messages(request)
    for message in storage:
        print(message)

    return render(request, "sign_in.html")

def password_reset_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        security_question = request.POST.get("security_question")
        security_answer = request.POST.get("security_answer")

        if not email or not security_question or not security_answer:
            messages.error(request, "All fields are required.")
            return render(request, "password_reset.html")

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            messages.error(request, "No user found with this email.")
            return render(request, "password_reset.html")

        # Check if security answer matches (case-insensitive)
        if hasattr(user, 'security_answer') and user.security_answer.lower() == security_answer.lower():
            request.session['reset_user_id'] = user.id  # Store user ID in session
            return redirect('set_new_password')  # Redirect to reset password page
        else:
            messages.error(request, "Incorrect security answer.")

    return render(request, "password_reset.html")


def set_new_password_view(request):
    user_id = request.session.get('reset_user_id')  # Retrieve user from session
    if not user_id:
        messages.error(request, "Session expired or invalid request.")
        return redirect('password_reset')

    user = User.objects.get(id=user_id)

    if request.method == "POST":
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if new_password and confirm_password and new_password == confirm_password:
            user.password = make_password(new_password)  # Hash and set new password
            user.save()
            del request.session['reset_user_id']  # Clear session data
            messages.success(request, "Password reset successfully. You can now log in.")
            return redirect('sign_in')  # Redirect to login page
        else:
            messages.error(request, "Passwords do not match.")

    return render(request, "set_new_password.html")

def sign_up(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        verify_password = request.POST.get('verify_password')
        membership = request.POST.get('membership')
        interest = request.POST.get('interest')
        security_question = request.POST.get('security_question')  # Get the selected security question
        security_answer = request.POST.get('security_answer')  # Get the answer to the question

        if not membership:
            messages.error(request, "Please select a membership type.")
            return render(request, "sign_up.html", {
                "email": email,
                "membership": membership,
                "interest": interest,
                "security_question": security_question,
                "security_answer": security_answer,
            })
        
        if not verify_password:
            messages.error(request, "Please re-type the password.")
            return render(request, "sign_up.html", {
                "email": email,
                "membership": membership,
                "interest": interest,
                "security_question": security_question,
                "security_answer": security_answer,
            })
        
        if verify_password != password:
            messages.error(request, "Passwords do not match.")
            return render(request, "sign_up.html", {
                "email": email,
                "membership": membership,
                "interest": interest,
                "security_question": security_question,
                "security_answer": security_answer,
            })
        
        if not interest:
            messages.error(request, "Please select an interest.")
            return render(request, "sign_up.html", {
                "email": email,
                "membership": membership,
                "interest": interest,
                "security_question": security_question,
                "security_answer": security_answer,
            })

        if CustomUser.objects.filter(username=email).exists():
            messages.error(request, "Email is already registered")
        else:
            # Create user with extra fields, including security question and answer
            user = CustomUser.objects.create_user(
                username=email,
                email=email,
                password=password,
                membership=membership,
                interest=interest,
                firstname=firstname,
                lastname=lastname,
                security_question=security_question,  # Save the selected question
                security_answer=security_answer,  # Save the answer
            )
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