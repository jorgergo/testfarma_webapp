from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("home", views.home, name="home"),
    path(
        "recommendations/<str:user_id>", views.recommendations, name="recommendations"
    ),
    path("profile", views.profile, name="profile"),
]
