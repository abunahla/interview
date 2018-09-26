from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm


class RegistrationForm(UserCreationForm):

	class Meta:
		model=User
		fields={
		   'first_name',
		   'last_name',
		   'username',
		   'password1',
		   'password2',
		}

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=True)
		user.first_name=self.cleaned_data['first_name']
		user.last_name=self.cleaned_data['last_name']
		if commit:
			user.save
			
class Edituserform(UserChangeForm):
	class Meta:
		model = User
		fields={
		   'first_name',
		   'last_name',
		   'username',		   
		   'password'
		}

