from django import forms

from .models import Participant

class RegisterationForm(forms.ModelForm):
	class Meta:
		model = Participant
		fields = ['email']