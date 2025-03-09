from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from AuthenticationApp.models import CustomUser

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def profile(request):

    user = request.user  # Get the currently logged-in user
    
    if request.method == "POST":
        # Handle the form submission to update the profile
        print(request.POST)  # Log POST data for debugging purposes

        # Update profile-related fields if you have a related Profile model
        user.phonenumber = request.POST.get('phone', user.phonenumber)
        user.location = request.POST.get('location', user.location)
        user.membership = request.POST.get('membership', user.membership)
        user.occupation = request.POST.get('occupation', user.occupation)
        user.skills = request.POST.get('skills', user.skills)
        
        # Handle the membership and interest selections
        user.membership = request.POST.get('membership', user.membership)
        user.interest = request.POST.get('interest', user.interest)

        # Save the changes
        user.save()
        print(user)
        print(f"Updated user: {user.phonenumber}, {user.location}, {user.membership}, {user.occupation}, {user.skills}")  # Log updated user details

        # Display a success message
        messages.success(request, "Your profile has been updated successfully!")

        # Redirect to the same profile page
        return redirect('profile')  # Redirect back to the profile page

    # For GET request, just render the profile page
    return render(request, 'profile.html', {
        'user': user,
        'MEMBERSHIP_CHOICES': CustomUser.MEMBERSHIP_CHOICES,
        'interests': CustomUser.INTEREST_CHOICES,
    })

@login_required
def manage_users(request):
    if request.user.membership == 'admin':
        return render(request, 'manageUsers.html')
    else:
        return redirect('no_access')  # Redirect users without access@login_required

@login_required
def adminHome(request):
    if request.user.membership == 'admin':
        return render(request, 'adminHome.html')
    else:
        return redirect('no_access')  # Redirect users without access