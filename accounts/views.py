from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UsersLoginForm, UsersRegisterForm
from django.http import HttpResponseRedirect


def login_view(request):
    form = UsersLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/")
    return render(request, "accounts/form.html", {
        "form": form,
        "title": "Login",
    })


def register_view(request):
    form = UsersRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("/accounts/login")
    return render(request, "accounts/form.html", {
        "title": "Register",
        "form": form,
    })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/accounts/login")
