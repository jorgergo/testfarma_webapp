from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.testfarma, name="testfarma"),
    path("about_us", views.about_us, name="about_us"),
    path("services", views.services, name="services"),
    path("contact", views.contact, name="contact"),
    path("terms", views.terms, name="terms"),
]