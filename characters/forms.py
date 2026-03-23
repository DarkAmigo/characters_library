from django import forms
from .models import Character

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'universe', 'creator', 'abilities', 'weapons', 'teams']
        widgets = {
            'abilities': forms.CheckboxSelectMultiple,
            'weapons': forms.CheckboxSelectMultiple,
            'teams': forms.CheckboxSelectMultiple,
        }