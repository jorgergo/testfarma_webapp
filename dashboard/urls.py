from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("home", views.home, name="home"),
    path("appointments", views.appointments, name="appointments"),
    path("profile", views.profile, name="profile"),
]
