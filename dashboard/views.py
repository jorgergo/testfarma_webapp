from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from login.views import *
from login.urls import *


# Create your views here.


def home(request):
    return render(request, "home.html")


def recommendations(request, user_id):
    return render(request, "recommendations/recommendations.html")


def profile(request):
    return render(request, "profile/profile.html")
