from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from user.models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    
    email = forms.EmailField(widget=forms.widgets.TextInput(attrs={
                'class': 'email-field form-control form-control-lg',
                "placeholder": "Correo Electrónico"}
            ))
    
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={
                'class': 'password-field form-control form-control-lg',
                "placeholder": "Contraseña"}
            ))   
    
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)