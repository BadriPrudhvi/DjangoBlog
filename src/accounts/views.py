from django.shortcuts import render, redirect

from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)

from .forms import UserLoginForm, UserRegisterForm

# Create your views here.

def login_view(request):
	next = request.GET.get('next')
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username = username, password = password)
		login(request,user)
		if next:
			return redirect(next)
		return redirect("/")
	return render(request,"login_form.html",{"form":form})


def register_view(request):
	next = request.GET.get('next')
	title = "Register"
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()

		new_user = authenticate(username = user.username, password = password)
		login(request, new_user)
		if next:
			return redirect(next)
		return redirect("/")
	context = {
		"form": form,
		"title":title
		}
	return render(request,"register_form.html", context)


def logout_view(request):
	logout(request)
	return render(request,"logout_form.html",{})



