from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("home", views.home, name="home"),
    path("recomendations/<str:user_id>", views.recomendations, name = "recomendations"),
    path("appointments", views.appointments, name = "appointments"),
    path("profile", views.profile, name = "profile"),
]
