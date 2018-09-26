# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.views import login,logout
from accounts.forms import RegistrationForm, Edituserform , PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



# Create your views here.
def login(request):
	return render(request, 'accounts/login.html')


def logout(request):
	return render(request, 'accounts/logout.html')

def register(request):
	if request.method =='POST' :
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/accounts/login')
	else:
		form = RegistrationForm()
	args={'form': form}
	return render(request,'accounts/register.html', args)

@login_required
def view_profile(request):
	args={'user': request.user}
	return render(request, 'accounts/profile.html', args)


def edit_profile(request):
	if request.method == 'POST':
		form = Edituserform(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('/accounts/profile')

	else:
		form = Edituserform(instance=request.user)
		args = {'form': form}
		return render(request, 'accounts/profile_edit.html',args)



