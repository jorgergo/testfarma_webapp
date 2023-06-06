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

Model_H, Model_M = pickle.load(open("TestFarma_Model_HW.p", "rb"))

# Create your views here.


@login_required(login_url="login")
def home(request):
    return render(request, "home.html")


@login_required(login_url="login")
def recommendations(request):
    form = RecommendationsForm()

    context = {"form": form}

    message = 0

    if request.method == "POST":
        form = RecommendationsForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            weight = float(data["weight"])
            height = float(data["height"])

            weight = np.asarray(weight).reshape(-1, 1)
            height = np.asarray(height).reshape(-1, 1)

            print("Hombres:")

            print(str(Model_H.predict_proba(weight)))
            print(str(Model_H.predict_proba(height)))

            print("Mujeres:")

            print(str(Model_M.predict_proba(weight)))
            print(str(Model_M.predict_proba(height)))

            message = str(Model_H.predict_proba(weight))

    context = {"form": form, "message": message}

    return render(request, "recommendations/recommendations.html", context)


def appointments(request):
    return render(request, "appointments/appointments.html")


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
