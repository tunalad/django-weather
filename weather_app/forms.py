from django import forms
from .models import Place


class FormPlace(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['place_name']
