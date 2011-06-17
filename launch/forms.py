from django import forms

from models import Signup

class SignupForm(forms.ModelForm):
	class Meta:
		model = Signup
		exclude = ('invitation_sent', 'invitees',)
