from django.shortcuts import HttpResponse, render


def index(request):
    # Common commands
    # python manage.py startapp AuthenticationApp
    return render(request, "base.html")
