from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from login.views import *
from login.urls import *

# Create your views here.

def dashboard(request, user_id):
    
    context = {
        "user": user_id
    }
    
    if request.user.is_authenticated:
        print("Usuario autenticado")
        return render(request, "home/dashboard.html", context)
    
    messages.error(request, "No ha iniciado sesión")
    return redirect("login")
    