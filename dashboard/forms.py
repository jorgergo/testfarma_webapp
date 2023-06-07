from django import forms
from .models import *


class RecommendationsForm(forms.Form):
    
    height = forms.IntegerField(label="Height", 
                                min_value=0, 
                                max_value=300,
                                widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Altura'}))
    
    weight = forms.IntegerField(label="Weight", 
                                min_value=0, 
                                max_value=300,
                                widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Peso'}))

    state = forms.ModelChoiceField( required = True, 
                                    label = "Estado",
                                    queryset = State.objects.all(),
                                    error_messages={
                                        "required": "No puede estar vacío",
                                    },
                                    widget = forms.Select(attrs = {
                                        "class": "form-control"
                                        }
                                    ))
    
    town = forms.ModelChoiceField( required = True, 
                                    label = "Municipio",
                                    queryset = Town.objects.all(),
                                    error_messages={
                                        "required": "No puede estar vacío",
                                    },
                                    widget = forms.Select(attrs = {
                                        "class": "form-control"
                                        }
                                    ))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["town"].queryset = Town.objects.none()

        if "state" in self.data:
            try:
                state = int(self.data.get("state"))
                self.fields["town"].queryset =  Town.objects.filter(state_id = state)
            
            except (ValueError, TypeError):
                pass
    
            

class AppointmentsForm(forms.Form):
    
    state = forms.ModelChoiceField( required = True, 
                                    label = "",
                                    queryset = State.objects.all(),
                                    error_messages={
                                        "required": "No puede estar vacío",
                                    },
                                    widget = forms.Select(attrs = {
                                        "class": "form-select "
                                        }
                                    ))
    
    town = forms.ModelChoiceField( required = True, 
                                    label = "",
                                    queryset = Town.objects.all(),
                                    error_messages={
                                        "required": "No puede estar vacío",
                                    },
                                    widget = forms.Select(attrs = {
                                        "class": "form-select"
                                        }
                                    ))
    
    study = forms.ModelChoiceField( required = True, 
                                    label = "",
                                    queryset = Study.objects.all(),
                                    error_messages={
                                        "required": "No puede estar vacío",
                                    },
                                    widget = forms.Select(attrs = {
                                        "class": "form-control form-select"
                                        }
                                    ))
    
    date = forms.DateField(label="",
                           required=True,
                           widget=forms.DateInput(attrs={'class': 'form-control', 
                                                         'placeholder': 'Fecha', 
                                                         'type': 'date'})
                            )
    
    hour = forms.TimeField(label="",
                           widget=forms.TimeInput(attrs={'class': 'form-control', 
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
    
    