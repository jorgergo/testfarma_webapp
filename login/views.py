from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
import json
from .forms import *
from dashboard.views import *
from dashboard.urls import *
from dashboard.models import *

# Create your views here.


def log_in(request):
    if request.user.is_authenticated:
        print("Usuario autenticado")

    if request.method == "POST":
        form = LoginForm(request.POST)

        print(form.is_valid())

        if form.is_valid():
            user = authenticate(
                email=request.POST["email"], password=request.POST["password"]
            )

            if user is not None:
                login(request, user)
                messages.success(request, f"Inicio de sesión exitoso")
                print("Inicio de sesión exitoso")
                
                return redirect("home")
                
            else:
                messages.error(
                    request,
                    "Correo o Contraseña Incorrectos. Los campos son sensibles a mayusculas o minusculas",
                )

        else:
            messages.error(
                request,
                "Correo o Contraseña Incorrectos. Los campos son sensibles a mayusculas o minusculas",
            )

    form = LoginForm()

    context = {"form": form}

    return render(request, "login/login.html", context)


def register(request):
    form = CacheRegisterForm()
    context = {"form": form}

    if request.method == "POST":
        form = CacheRegisterForm(request.POST)
        print(form.is_valid())

        if form.is_valid():
            data = json.dumps(form.cleaned_data, default=str)

            request.session["register_form_part_two"] = data

            return redirect("register_part_two")

    return render(request, "signup/signup.html", context)


def register_part_two(request):
    data = json.loads(request.session["register_form_part_two"])

    form = UserCreationForm()

    context = {"form": form}

    if request.method == "POST":
        updated_request = request.POST.copy()
        updated_request.update(data)

        form = UserCreationForm(updated_request)

        if form.is_valid():
            data = form.cleaned_data

            try:
                form.save()
                messages.success(request, f"Usuario creado exitosamente")
                print("USER CREATED SUSSCESFULLY")

                return redirect("register_part_three")

            except Exception as e:
                messages.error(request, f"Error al crear usuario")
                print(e)

    return render(request, "signup/signup_part_two.html", context)


def register_part_three(request):

    if request.method == "POST":
        return redirect("login")

    return render(request, "signup/signup_part_three.html")


def log_out(request):
    
    logout(request)
    messages.info(request, f"Cierre de sesión exitoso")

    return redirect("login")


def load_towns(request):
    state_id = request.GET.get("state")
    towns = Town.objects.filter(state_id=state_id).order_by("town")
    
    return render(request, "snippets/signup_town_dropdown_list_options.html", {"towns": towns})
