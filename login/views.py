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


def register(request):
    
    form = CacheRegisterForm()
    context = {
        "form": form
    }

    if request.method == "POST":
            
        form = CacheRegisterForm(request.POST)

        if form.is_valid():
            
            data = form.cleaned_data
                
            request.session["register_form"] = request.POST
            
            redirect("register_part_two")

    return render(request, "signup/signup.html", context)

def register_part_two(request):
    
    form = UserCreationForm()
    context = {
        "form" : form
    }
    
    if request.method == "POST":
        
        if form.is_valid():
            
            try:
                form.save()
                messages.success(request, "Registro exitoso, ya puedes iniciar sesión")
            except Exception as e:
                messages.error(request, f"No se pudo registrar el usuario -> {e}")
        
    return render(request, "signup/signup_part_two.html", context)