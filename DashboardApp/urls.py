from django.urls import path
from .views import create_event, dashboard, delete_event, profile, manage_users, adminHome, manageEvents,manageMembers, adminNotifications, change_approval_state,addEvents, learning, no_access, update_event
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
    path('addEvents/', addEvents, name='addEvents'),
    path('manageMembers/', manageMembers, name='manageMembers'),
    path('adminNotifications/', adminNotifications, name='adminNotifications'),
    path('learning/', learning, name='learning'),
    path("no-access/", no_access, name="no_access"),
    path("create-event/", create_event, name="create_event"),
    path("update-event/<int:event_id>/", update_event, name="update_event"),
    path("delete-event/<int:event_id>/", delete_event, name="delete_event"),
    ]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
