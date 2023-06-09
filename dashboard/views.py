from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from login.views import *
from login.urls import *
import pandas as pd
from sklearn.mixture import GaussianMixture
import numpy as np
import pickle
import bson
from datetime import datetime, date, timedelta


Model_H, Model_M = pickle.load(open("TestFarma_Model_HW.p", "rb"))

# Create your views here.


@login_required(login_url="login")
def home(request):
    return render(request, "home.html")


@login_required(login_url="login")
def recommendations(request):
    
    form = RecommendationsForm()

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
            
            print(probability)
            
            if float(probability) > threshold:
                
                print("Se necesita un estudio General")
                studies.append(Study.objects.get(pk=1))
                
            else :
                print("Dentro del Rango")
            
            
    context = {
        "form": form,
        "studies" : studies,
    }
    
    return render(request, "recommendations/recommendations.html", context)


def appointments(request):
    
    if request.session.get("reccomended") is None:
    
        form = AppointmentsForm(initial={"study": Study.objects.get(pk=1),
                                         "date" : date.today() + timedelta(days=1)})
    
    else:
        
        form = AppointmentsForm(initial={"study": Study.objects.get(request.session.get("recommended"))})
    
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
    user = User.objects.get(pk=request.user.pk)

    if user.gender == "M":
        user.gender_text = "Masculino"
    elif user.gender == "F":
        user.gender_text = "Femenino"
    else:
        user.gender_text = user.gender

    context = {"user": user}

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

