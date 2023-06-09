from typing import Any
from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
)
from user.models import User
from testfarma import settings
from dashboard.models import *

from django.contrib.auth import authenticate

from django.utils.safestring import mark_safe


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.widgets.TextInput(
            attrs={
                "class": "email-field form-control form-control-lg",
                "placeholder": "Correo Electrónico",
            }
        )
    )

    password = forms.CharField(
        widget=forms.widgets.PasswordInput(
            attrs={
                "class": "password-field form-control form-control-lg",
                "placeholder": "Contraseña",
            }
        )
    )


class CacheRegisterForm(forms.Form):
    name = forms.CharField(
        label="",
        widget=forms.widgets.TextInput(
            attrs={"class": "name-field form-control", "placeholder": "Nombre"}
        ),
    )
    last_name = forms.CharField(
        label="",
        widget=forms.widgets.TextInput(
            attrs={
                "class": "last-name-field form-control",
                "placeholder": "Apellido Paterno",
            }
        ),
    )

    mom_last_name = forms.CharField(
        label="",
        widget=forms.widgets.TextInput(
            attrs={
                "class": "mom-last-name-field form-control",
                "placeholder": "Apellido Materno",
            }
        ),
    )

    birth_date = forms.DateField(
        label="",
        input_formats=["%d-%m-%Y", "%Y-%m-%d"],
        widget=forms.widgets.DateInput(
            attrs={
                "class": "birth-date-field form-control",
                "type": "date",
                "placeholder": "Fecha de Nacimiento",
            }
        ),
    )
    
    state = forms.ModelChoiceField( required = True, 
                                   empty_label="Estado de Residencia",
                                    label = "",
                                    queryset = State.objects.all(),
                                    error_messages={
                                        "required": "No puede estar vacío",
                                    },
                                    widget = forms.Select(attrs = {
                                        "class": "form-control form-select form-select-lg"
                                        }
                                    ))
    
    town = forms.ModelChoiceField( required = True, 
                                    label = "",
                                    empty_label="Municipio",
                                    queryset = Town.objects.all(),
                                    error_messages={
                                        "required": "No puede estar vacío",
                                    },
                                    widget = forms.Select(attrs = {
                                        "class": "form-control form-select form-select-lg"
                                        }
                                    ))

    gender = forms.ChoiceField(
        required=True,
        label="",
        choices=(("", "Me identifico con..."), ("M", "Masculino"), ("F", "Femenino")),
        error_messages={
            "required": "No puede estar vacío",
        },
        widget=forms.Select(attrs={"class": "form-control form-select form-select-lg"}),
    )

    user_type = forms.ChoiceField(
        required=True,
        choices=(("DoctorT", "Doctor"), ("UserT", "Paciente")),
        error_messages={
            "required": "No puede estar vacío",
        },
        widget=forms.RadioSelect(),
    )
    
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["town"].queryset = Town.objects.none()

        if "state" in self.data:
            try:
                state = int(self.data.get("state"))
                self.fields["town"].queryset =  Town.objects.filter(state_id = state)
            
            except (ValueError, TypeError):
                pass

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "name",
            "last_name",
            "mom_last_name",
            "birth_date",
            "gender",
            "user_type",
            "email",
            "password1",
            "password2",
        )

    name = forms.CharField(
        label="",
        widget=forms.widgets.TextInput(
            attrs={"class": "name-field form-control", "placeholder": "Nombre"}
        ),
    )
    last_name = forms.CharField(
        label="",
        widget=forms.widgets.TextInput(
            attrs={
                "class": "last-name-field form-control",
                "placeholder": "Apellido Paterno",
            }
        ),
    )

    mom_last_name = forms.CharField(
        label="",
        widget=forms.widgets.TextInput(
            attrs={
                "class": "mom-last-name-field form-control",
                "placeholder": "Apellido Materno",
            }
        ),
    )

    birth_date = forms.DateField(
        label="",
        widget=forms.widgets.DateInput(
            attrs={
                "class": "birth-date-field form-control",
                "placeholder": "Fecha de Nacimiento",
            }
        ),
    )

    gender = forms.ChoiceField(
        required=True,
        label="",
        choices=(("", "Me identifico con..."), ("M", "Masculino"), ("F", "Femenino")),
        error_messages={
            "required": "No puede estar vacío",
        },
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    user_type = forms.ChoiceField(
        required=True,
        label="",
        choices=(("", "Soy un..."), ("DoctorT", "Doctor"), ("UserT", "Paciente")),
        error_messages={
            "required": "No puede estar vacío",
        },
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    email = forms.EmailField(
        widget=forms.widgets.TextInput(
            attrs={
                "class": "email-field form-control form-control-lg",
                "placeholder": "Correo Electrónico",
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.widgets.PasswordInput(
            attrs={
                "class": "password-field form-control form-control-lg",
                "placeholder": "Contraseña",
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.widgets.PasswordInput(
            attrs={
                "class": "password-field form-control form-control-lg",
                "placeholder": "Contraseña",
            }
        )
    )

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

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data["email"],
            self.cleaned_data["password1"],
            first_name=self.cleaned_data["name"],
            last_name=self.cleaned_data["last_name"],
            mom_last_name=self.cleaned_data["mom_last_name"],
            birth_date=self.cleaned_data["birth_date"],
            gender=self.cleaned_data["gender"],
            user_type=self.cleaned_data["user_type"],
        )

        return user
