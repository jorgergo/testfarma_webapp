from django import forms


class RecommendationsForm(forms.Form):
    
    height = forms.IntegerField(label="Height", 
                                min_value=0, 
                                max_value=300,
                                widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Altura'}))
    
    weight = forms.IntegerField(label="Weight", 
                                min_value=0, 
                                max_value=300,
                                widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Peso'}))
    
    