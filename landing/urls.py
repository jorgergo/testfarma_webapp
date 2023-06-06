from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("testfarma", views.testfarma, name="testfarma"),
    path("services", views.services, name="services"),
    path("termsandconditions", views.termsandconditions, name="termsandconditions"),
]