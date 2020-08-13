from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from crispy_forms.helper import FormHelper
class SignupForm(UserCreationForm):
	password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email']
		labels = {'email':'Email'}
		help_texts = {

            'username': None,
            'email': None,
            

        }