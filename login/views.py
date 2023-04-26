from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User

# Create your views here.

def log_in(request):
    
    if request.user.is_authenticated:
        print("Usuario autenticado")
    
    if request.method == "POST":
        
        form = LoginForm(request.POST)
        
        print(form.is_valid())

        if form.is_valid():
            user = authenticate(
                email = request.POST["email"],
                password = request.POST["password"]
            )
            
            if user is not None:
                login(request, user)
                messages.success(request, f"Inicio de sesión exitoso")
                print("Inicio de sesión exitoso")
            else:
                messages.error(request, "Correo o Contraseña Incorrectos. Los campos son sensibles a mayusculas o minusculas")
                
        else:
            messages.error(request, "Correo o Contraseña Incorrectos. Los campos son sensibles a mayusculas o minusculas")
        
    form = LoginForm()
    
    context = {
        "form": form
    }
    
    return render(request, "login/login.html", context)
