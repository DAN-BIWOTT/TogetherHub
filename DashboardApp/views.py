from .models import Event
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Lesson
from .forms import LessonForm
from django.contrib import messages
from AuthenticationApp.models import CustomUser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render, redirect
import os
from django.conf import settings

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
        allEvents = Event.objects.order_by('created_at').count()
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
            "all_events": allEvents
            })
    else:
        return redirect('no_access')  # Redirect users without access
        
@login_required
def manageMembers(request):
    if request.user.membership == 'admin':

        # We get all users from the db
        allMembers = CustomUser.objects.order_by('created_at').exclude(Q(membership="admin") | Q(approvedmember=False)) # The Q is necessary. I don't know why but it is. 🤦‍♂️
        
        return render(request, 'manageMembers.html', {
            "allMembers": allMembers,
            })
    else:
        return redirect('no_access')

# MANAGE WORKSPACE 🏢
@login_required
def manageEvents(request):
    if request.user.membership == 'admin' or request.user.membership == 'Workspace':
        allEvents = Event.objects.order_by('created_at')

        return render(request, 'manageEvents.html', {
            "allEvents":allEvents
        })
    else:
        return redirect('no_access')

@login_required
def create_event(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        location = request.POST.get("location")
        organizer_id = request.POST.get("organizer")
        poster = request.FILES.get("poster")  # File upload handling
        
        # Ensure the organizer exists
        organizer = CustomUser.objects.get(id=organizer_id)

        # Save poster manually
        poster_path = None
        if poster:
            poster_directory = os.path.join(settings.MEDIA_ROOT, "event_posters")
            os.makedirs(poster_directory, exist_ok=True)
            poster_path = os.path.join("event_posters", poster.name)

            with open(os.path.join(settings.MEDIA_ROOT, poster_path), "wb+") as destination:
                for chunk in poster.chunks():
                    destination.write(chunk)

        event = Event.objects.create(
            name=name,
            description=description,
            start_date=start_date,
            end_date=end_date,
            location=location,
            organizer=organizer,
            poster=poster_path,  # Store relative path
        )

        return redirect("manageEvents")  # Redirect to event list page

    return render(request, "addEvents.html")

@login_required
def update_event(request, event_id):
    """Edit an existing event."""
    event = Event.objects.get(id=event_id)


    if request.method == "POST":
        event.name = request.POST.get("name")
        event.description = request.POST.get("description")
        event.start_date = request.POST.get("start_date")
        event.end_date = request.POST.get("end_date")
        event.location = request.POST.get("location")

        if "poster" in request.FILES:
            event.poster = request.FILES["poster"]

        event.save()
        return redirect("manageEvents")

    return render(request, "editEvent.html", {"event": event})

@login_required
def delete_event(request, event_id):
    """Delete an event."""
    event = Event.objects.get(id=event_id)

    if request.method == "POST":
        event.delete()
        return redirect("manageEvents")

    return render(request, "deleteEvent.html", {"event": event})

@login_required
def addEvents(request):
    if request.user.membership != 'admin':
        print('here at events')
        return render(request, 'addEvents.html')
    else:
        return redirect('no_access')

# MANAGE KEY ACCESS 🏫
@login_required
def learning(request): # Add a check that results in only lessons made by the current user.
    if request.user.membership in ['admin', 'Key Access', 'community']:
        lessons = Lesson.objects.all()
        print(lessons.count())
        return render(request, 'learning.html', {'lessons': lessons})
    else:
        return redirect('no_access')

@login_required
def createLesson(request):
    if request.user.membership in ['admin', 'Key Access']:
        if request.method == 'POST':
            form = LessonForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('learning')
        else:
            form = LessonForm()
            print("Form errors:", form.errors)
        return render(request, 'createLesson.html', {'form': form})
    else:
        return redirect('no_access')

@login_required
def edit_lesson(request, lesson_id):
    if request.user.membership in ['admin', 'Key Access']:
        lesson = get_object_or_404(Lesson, id=lesson_id)
        if request.method == 'POST':
            form = LessonForm(request.POST, instance=lesson)
            if form.is_valid():
                form.save()
                return redirect('learning')
        else:
            form = LessonForm(instance=lesson)
        return render(request, 'editLesson.html', {'form': form})
    else:
        return redirect('no_access')

@login_required
def lesson_detail(request, lesson_id):
    if request.user.membership in ['admin', 'Key Access']:
        lesson = get_object_or_404(Lesson, id=lesson_id)
        return render(request, 'lessonDetail.html', {'lesson': lesson})
    else:
        return redirect('no_access')

@login_required
def delete_lesson(request, lesson_id):
    if request.user.membership in ['admin', 'Key Access']:
        lesson = get_object_or_404(Lesson, id=lesson_id)
        if request.method == 'POST':
            lesson.delete()
            return redirect('learning')
        return render(request, 'learning.html', {'lesson': lesson})
    else:
        return redirect('no_access')


def no_access(request):
    print(request.user.membership)
    return render(request, "no_access.html")

# MANAGE COMMUNITY 🧑‍🤝‍🧑

@login_required
def allLessons(request):
    lessons = Lesson.objects.all()
    return render(request, 'allLessons.html', {'lessons': lessons})