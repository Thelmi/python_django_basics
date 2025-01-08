from django import forms # type: ignore

from .models import Participant

class RegisterationForm(forms.Form):
    email = forms.EmailField()