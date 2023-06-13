from django.urls import path
from . import views
from . import forms
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("login", views.log_in, name="login"),
    path("register", views.register, name="register"),
    path("register/account", views.register_part_two, name="register_part_two"),
    path("register/success", views.register_part_three, name="register_part_three"),
    path("password-reset", views.PasswordResetView.as_view(), name="password_reset"),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='login/password_reset_confirm.html', form_class=forms.SetPassword),
         name='password_reset_confirm'),
    path('password-reset-complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='login/password_reset_complete.html'),
         name='password_reset_complete'),
    path("logout", views.log_out, name="logout"),
    path("signup/ajax/load-towns/", views.load_towns, name="signup_ajax_load_towns"), # AJAX
]
