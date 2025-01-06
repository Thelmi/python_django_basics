from django import forms # type: ignore

from .models import Participant

class RegisterationForm(forms.ModelForm):
	class Meta:
		model = Participant
		fields = ['email']