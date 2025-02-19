from django.shortcuts import HttpResponse, render


def sign_in(request):
    # Common commands
    # python manage.py startapp AuthenticationApp
    return render(request,"sign_in.html")

def sign_up(request):
    return render(request,"sign_up.html")