from django import forms
from .models import *


class RecommendationsForm(forms.Form):
    
    height = forms.IntegerField(label="Height", 
                                min_value=0, 
                                max_value=300,
                                widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg', 
                                                                'placeholder': 'Altura',
                                                                'type': 'number'}))
    
    weight = forms.IntegerField(label="Weight", 
                                min_value=0, 
                                max_value=300,
                                widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg', 
                                                                'placeholder': 'Peso',
                                                                'type': 'number'}))
               

class AppointmentsForm(forms.Form):
    
    state = forms.ModelChoiceField( required = True, 
                                    label = "Estado",
                                    queryset = State.objects.all(),
                                    error_messages={
                                        "required": "No puede estar vacío",
                                    },
                                    widget = forms.Select(attrs = {
                                        "class": "form-control form-select form-select-lg"
                                        }
                                    ))
    
    town = forms.ModelChoiceField( required = True, 
                                    label = "Sucursal",
                                    queryset = Town.objects.all(),
                                    error_messages={
                                        "required": "No puede estar vacío",
                                    },
                                    widget = forms.Select(attrs = {
                                        "class": "form-control form-select form-select-lg"
                                        }
                                    ))
    
    study = forms.ModelChoiceField( required = True, 
                                    label = "Estudio",
                                    queryset = Study.objects.all(),
                                    error_messages={
                                        "required": "No puede estar vacío",
                                    },
                                    widget = forms.Select(attrs = {
                                        "class": "form-control form-select form-select-lg"
                                        }
                                    ))
    
    date = forms.DateField(label="Fecha",
                           required=True,
                           widget=forms.DateInput(attrs={'class': 'form-control form-control-lg', 
                                                         'placeholder': 'Fecha', 
                                                         'type': 'date'})
                            )
    
    hour = forms.TimeField(label="Hora",
                           widget=forms.TimeInput(attrs={'class': 'form-control form-control-lg', 
                                                         'placeholder': 'Hora', 
                                                         'type': 'time'})
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
    
    