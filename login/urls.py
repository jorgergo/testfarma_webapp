from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    path("login", views.log_in, name = "login"),
    path("register", views.register, name = "register"),

]