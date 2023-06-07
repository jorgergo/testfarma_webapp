from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("home", views.home, name="home"),
    path("recommendations", views.recommendations, name="recommendations"),
    path("appointments", views.appointments, name="appointments"),
    path("profile", views.profile, name="profile"),
    
    path("ajax/load-towns/", views.load_towns, name="ajax_load_towns"), # AJAX
]
