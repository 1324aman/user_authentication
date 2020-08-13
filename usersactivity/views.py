from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.forms import(
	AuthenticationForm,
	PasswordChangeForm
	)
from django.contrib.auth import(
	authenticate, login, update_session_auth_hash,
	logout
	)
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User


def sign_up(request):
	if request.method == 'POST':
		sign_up_form = SignupForm(request.POST)
		if sign_up_form.is_valid():
			sign_up_form.save()
			return HttpResponseRedirect('login')
	else:
		sign_up_form = SignupForm()

	return render(request, 'usersactivity/sign_up.html', {'form':sign_up_form})


def user_login(request):
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request,'logged in successfully')
				#return render(request, 'usersactivity/profile.html')
				return HttpResponseRedirect('profile')
	else:
		form = AuthenticationForm()
	return render(request, 'usersactivity/login.html', {'form':form})


def user_profile(request):
	if request.user.is_authenticated:
		context ={
			'name': request.user.get_full_name(),
			'first_name': request.user.first_name,
			'email': request.user.email,
		}
	else:
		return HttpResponseRedirect('login')
	return render(request, 'usersactivity/profile.html', context)


def user_logout(request):
	logout(request)
	return HttpResponseRedirect('login')


def change_user_password(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = PasswordChangeForm(user=request.user, data=request.POST)
			if form.is_valid():
				form.save()
				update_session_auth_hash(request, form.user)
				return HttpResponseRedirect('profile')
		else:
			form = PasswordChangeForm(user=request.user)
		return render(request, 'usersactivity/change_password.html', {'form':form})
	else:
		return HttpResponseRedirect('login')


class ProfileUpdate(UpdateView):
    model = User
    fields = ['first_name','last_name','email']
    template_name = 'usersactivity/profile_update.html'

    def get_success_url(request):
    	return reverse('usersactivity:profile')
