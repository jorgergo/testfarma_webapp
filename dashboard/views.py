from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from login.views import *
from login.urls import *


# Create your views here.


def home(request):
    return render(request, "home.html")

def recomendations(request, user_id):
    
    return render(request, "recomendations.html")

def appointments(request):
    return render(request, "appointments/appointments.html")


def profile(request):
    return render(request, "profile/profile.html")
