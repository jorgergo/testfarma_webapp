from typing import Any
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
    

class UserCreationForm(UserCreationForm):
    
    email = forms.EmailField(widget=forms.widgets.TextInput(attrs={
                'class': 'email-field form-control form-control-lg',
                'placeholder': 'Correo Electrónico'}
            ))
    
    password1 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={
                'class': 'password-field form-control form-control-lg',
                'placeholder': 'Contraseña'}
                                                                   
            ))
    
    password2 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={
                'class': 'password-field form-control form-control-lg',
                'placeholder': 'Contraseña'}
                                                                   
            ))
    
    def email_clean(self):
        
        email = self.cleaned_data.get("email")
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo ya existe")
        
        return email
    
    def clean_password2(self):
        
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        
        return password2
    
    def save(self, commit = True):
        user = User.objects.create_user(
            self.cleaned_data["email"],
            self.cleaned_data["password1"]
        )
        
        return user    


class RegisterForm(forms.Form):
    
    name = forms.CharField(
                label = "",
                widget=forms.widgets.TextInput(attrs={
                'class': 'name-field form-control',
                'placeholder': 'Nombre'
                
                }))
    
    last_name = forms.CharField(
                label = "",
                widget=forms.widgets.TextInput(attrs={
                'class': 'last-name-field form-control',
                'placeholder': 'Apellido Paterno'
                }))
    
    mom_last_name = forms.CharField(
                label = "",
                widget=forms.widgets.TextInput(attrs={
                'class': 'mom-last-name-field form-control',
                'placeholder': 'Apellido Materno'
                
                }))
    
    birth_date = forms.DateField(
                label = "",
                widget=forms.widgets.DateInput(attrs={
                'class': 'birth-date-field form-control',
                'placeholder': 'Fecha de Nacimiento'
                }))
    
    gender = forms.ChoiceField( required = True,
                               label = "",
                                choices=(("","Me identifico con..."),("MaleG", "Maculino"), ("FemaleG", "Femenino")),
                                error_messages={
                                    "required": "No puede estar vacío",
                                },
                                
                                widget = forms.Select(attrs = {
                                    "class": "form-control"
                                    }
                                ))
    
    user_type = forms.ChoiceField( required = True,
                                  label = "",
                                choices=(("","Soy un..."),("DoctorT", "Doctor"), ("UserT", "Paciente")),
                                error_messages={
                                    "required": "No puede estar vacío",
                                },
                                
                                widget = forms.Select(attrs = {
                                    "class": "form-control"
                                    }
                                ))
    
    