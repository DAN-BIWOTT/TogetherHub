from django.urls import path
from .views import allLessons, create_event, createLesson, dashboard, delete_event, delete_lesson, edit_lesson, enroll_lesson, lesson_detail, my_events, myLessons, profile, manage_users, adminHome, manageEvents,manageMembers, adminNotifications, change_approval_state, learning, no_access, register_event, unenroll_lesson, unregister_event, update_event
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('manageUsers/', manage_users, name='manageUsers'),
    path("change_approval_state/", change_approval_state, name="change_approval_state"),
    path('adminHome/', adminHome, name='adminHome'),
    path('manageEvents/', manageEvents, name='manageEvents'),
    path('manageMembers/', manageMembers, name='manageMembers'),
    path('adminNotifications/', adminNotifications, name='adminNotifications'),
    path('learning/', learning, name='learning'),
    path("no-access/", no_access, name="no_access"),
    path("create-event/", create_event, name="create_event"),
    path("createLesson/", createLesson, name="createLesson"),
    path("allLessons/", allLessons, name="allLessons"),
    path('lesson/<int:lesson_id>/', lesson_detail, name='lesson_detail'),
    path('myLessons/', myLessons, name='myLessons'),
    path('edit_lesson/<int:lesson_id>/', edit_lesson, name='edit_lesson'),
    path('enroll_lesson/<int:lesson_id>/', enroll_lesson, name='enroll_lesson'),
    path('unenroll/<int:lesson_id>/', unenroll_lesson, name='unenroll_lesson'),
    path("my-events/", my_events, name="my_events"),
    path("register-event/<int:event_id>/", register_event, name="register_event"),
    path("unregister-event/<int:event_id>/", unregister_event, name="unregister_event"),
    path('delete_lesson/<int:lesson_id>/', delete_lesson, name='delete_lesson'),
    path("update-event/<int:event_id>/", update_event, name="update_event"),
    path("delete-event/<int:event_id>/", delete_event, name="delete_event"),
    ]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
