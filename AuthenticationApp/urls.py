from django.urls import path
from .views import sign_up, sign_in, sign_out
from django.contrib.auth import views as auth_views
from .views import password_reset_view, set_new_password_view


urlpatterns = [
    path('sign_in/', sign_in, name='sign_in'),
    path('sign_up/', sign_up, name='sign_up'),
    path('sign_out/', sign_out, name='sign_out'),
    path('password_reset/', password_reset_view, name='password_reset'),  # ✅ Use the view function
    path('set_new_password/', set_new_password_view, name='set_new_password'),
]

