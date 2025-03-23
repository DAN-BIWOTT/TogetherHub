from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from AuthenticationApp.models import CustomUser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# MANAGE USERS 🥸
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def profile(request):

    user = request.user  # Get the currently logged-in user
    
    if request.method == "POST":
        # Handle the form submission to update the profile
        print(request.POST)  

        # Update profile-related fields if you have a related Profile model
        user.phonenumber = request.POST.get('phone', user.phonenumber)
        user.location = request.POST.get('location', user.location)
        user.membership = request.POST.get('membership', user.membership)
        user.occupation = request.POST.get('occupation', user.occupation)
        user.skills = request.POST.get('skills', user.skills)
        user.interest = request.POST.get('interests', '').split(',')
        user.membership = request.POST.get('membership', user.membership)

        # Save the changes
        user.save()
        print(user)
        print(f"Updated user: {user.interest},{user.phonenumber}, {user.location}, {user.membership}, {user.occupation}, {user.skills}")  # Log updated user details

        # Display a success message
        messages.success(request, "Your profile has been updated successfully!")

        # Redirect to the same profile page ➡️
        return redirect('profile')  # Redirect back to the profile page
    # patch for the interest list.
    user_interests = user.interest.strip("[]").replace("'","").split(',')

    return render(request, 'profile.html', {
        'user': user,
        'MEMBERSHIP_CHOICES': CustomUser.MEMBERSHIP_CHOICES,
        'interests': CustomUser.INTEREST_CHOICES,
        'user_interests':user_interests
    })

# MANAGE ADMIN 🤖
@login_required
def manage_users(request):
    if request.user.membership == 'admin':
        # We get all users from the db
        allUsers = CustomUser.objects.order_by('created_at').exclude(Q(membership="admin") | Q(approvedmember=True)) # The Q is necessary. I don't know why but it is. 🤦‍♂️

        return render(request, 'manageUsers.html', {
            "allUsers":allUsers,
            })
    else:
        return redirect('no_access')  # Redirect users without access@login_required

@login_required
def adminNotifications(request):
    dummy_notifications = [
        {"sender": "Brian Griffin", "message": "wants to collaborate", "timestamp": "5 days ago"},
        {"sender": "Adam (Mayor's Office)", "message": "is looking for people like you.", "timestamp": "1 month ago"},
        {"sender": "Neil", "message": "is looking for people like you.", "timestamp": "1 month ago"},
        {"sender": "Quagmire (Giggity Co.)", "message": "is looking for people like you.", "timestamp": "1 month ago"},
        {"sender": "Herbert (Children's Program)", "message": "is looking for people like you.", "timestamp": "2 months ago"},
    ]
    return render(request, 'adminNotifications.html', {'notifications': dummy_notifications})

@login_required
def change_approval_state(request):
        if request.method == "POST":
                try:
                    data = json.loads(request.body)
                    user_id = data.get("user_id")
                    s = data.get("s")
                    s = s in ["true", "True", "1"] # We are turning every true string to boolean.
                    user = CustomUser.objects.get(id=user_id)
                    user.approvedmember = s
                    user.save()
                    if s: 
                        messages.success(request, f"User {user.username} has been approved!😁")
                        print("I'm here at True. S: ",s)
                    else: 
                        messages.success(request, f"User {user.username} has been banned!🤕")
                        print("I'm here at False. S: ",s)
                    return JsonResponse({"success": True, "message": "User made a member successfully."}) if s else JsonResponse({"success": True, "message": "User banned successfully."})
                except CustomUser.DoesNotExist:
                    messages.error(request, "User not found.🤷‍♀️")
                    return JsonResponse({"success": False, "message": "User not found."})
                except Exception as e:
                    return JsonResponse({"success": False, "message": str(e)})
        return JsonResponse({"success": False, "message": "Invalid request method."})

@login_required
def adminHome(request):
    if request.user.membership == 'admin':

        allUsers = CustomUser.objects.order_by('created_at').exclude(membership="admin") # The - sign orders it in descending order.
        sampleUsers = allUsers[:5]
        community_member_count = allUsers.filter(membership="Community").count()
        key_access_count = allUsers.filter(membership="Key Access").count()
        workspace_count = allUsers.filter(membership="Workspace").count()
        new_users_count = allUsers.filter(approvedmember=False).count()

        return render(request, 'adminHome.html', {
            "sampleUsers":sampleUsers,
            "community_member_count":community_member_count,
            "key_access_count":key_access_count,
            "workspace_count":workspace_count,
            "new_users_count":new_users_count,
            })
    else:
        return redirect('no_access')  # Redirect users without access