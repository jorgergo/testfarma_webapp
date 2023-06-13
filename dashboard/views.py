from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from login.views import *
from login.urls import *
import numpy as np
import pickle
import bson
from utils import *


Model_H, Model_M = pickle.load(open("TestFarma_Model_HW.p", "rb"))
db = get_db_handle("testfarma")

# Create your views here.


@login_required(login_url="login")
def home(request):
    return render(request, "home.html")


@login_required(login_url="login")
def recommendations(request):
    
    form = RecommendationsForm()
    
    user_data = db.medic_data.find_one({"_id" : request.user.id})

    context = {"form": form}

    threshold = 0.8
    studies = []
    
    if request.method == "POST":
        
        form = RecommendationsForm(request.POST)
        
        if form.is_valid():
            
            data = form.cleaned_data
            
            weight = float(data["weight"])
            height = float(data["height"])
            
            variables = np.asarray([weight, height]).reshape(1, -1)
            
            if request.user.gender == "M":
                
                print("Mujer")
                probability = str(np.max(Model_M.predict_proba(variables)))
            
            elif request.user.gender == "H":
                
                print("Hombre")
                probability = str(np.max(Model_H.predict_proba(variables)))
                
            else:
                
                messages.error(request, "Error al obtener el género")
            
            
            if float(probability) > threshold:
                
                print("Se necesita un estudio")
                studies.append(Study.objects.get(pk=3))
                
            if user_data["cholesterol"] >= 2:
                
                studies.append(Study.objects.get(pk=7))
            
            if user_data["gluc"] >= 2:
                
                studies.append(Study.objects.get(pk=8))
            
            if user_data["smoke"] == 1:
                
                studies.append(Study.objects.get(pk=9))
                
            if user_data["alco"] == 1:
                
                studies.append(Study.objects.get(pk=10))
            
            
    context = {
        "form": form,
        "studies" : studies,
    }
    
    return render(request, "recommendations/recommendations.html", context)


def appointments(request):
    
    if request.session.get("recommended") is None:
    
        form = AppointmentsForm()
    
    else:
        
        json_data = json.loads(request.session.get("recommended"))
        
        form = AppointmentsForm(initial={
            
            "study": Study.objects.get(code = json_data["code"]),
            "state": State.objects.get(state = json_data["state"]),
            "town" : Town.objects.get(town = json_data["town"]),
        
        })
    
    context = {
        "form": form,
        "appointments" : Appointment.objects.filter(user_id=request.user.pk)
    }
    
    if request.method == "POST":
        
        form = AppointmentsForm(request.POST)
        
        if form.is_valid():
            
            data = form.cleaned_data
            
            try:
                    
                Appointment.objects.create(
                    id = str(bson.ObjectId()),
                    user_id = request.user.pk, 
                    place = f"{data['state'].state}, {data['town'].town}",
                    study = data["study"],
                    date = data["date"],
                    hour = data["hour"]                
                )
                
                messages.success(request, "Cita creada correctamente")
                
            except Exception as e:
                messages.error(request, "Error al crear la cita")
                print(e)
                
                
    
    return render(request, "appointments/appointments.html", context)


@login_required(login_url="login")
def profile(request):
    
    if request.method == "POST":
        
        form = PasswordChange(data=request.POST, user=request.user)
        
        if form.is_valid():
            
            messages.success(request, "Contraseña cambiada correctamente")
            form.save()
    
    else:
        
        form = PasswordChange(user=request.user)
        
    context = {
        "form": form
    }

    return render(request, "profile/profile.html", context)


def appointment_delete(request, id_appointment):
    
    try:
        
        Appointment.objects.get(id=id_appointment).delete()
        messages.success(request, "Cita eliminada correctamente")
        return redirect('appointments')

    except Exception as e:
        messages.error(request, f"Error al eliminar la cita, {e}")


def load_towns(request):
    state_id = request.GET.get("state")
    towns = Town.objects.filter(state_id=state_id).order_by("town")
    return render(request, "snippets/town_dropdown_list_options.html", {"towns": towns})


def recommended_appointment(request):
    
    code = request.GET.get("code")
    state = request.GET.get("state")
    town = request.GET.get("town")
    
    request.session["recommended"] = json.dumps({"code": code, "state": state, "town": town})
    
    print("DONE")
    
    return HttpResponse(status=200)
