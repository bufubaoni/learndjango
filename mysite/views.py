from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render, redirect

# Create your views here.
from requests import sessions
from river.models import State

from mysite.models import MyModel
import pdb


def test(request):
    return render(request, "test.html", {"user": request.user})


def loginme(request):
    class loginform(forms.Form):
        username = forms.CharField(label='username')
        password = forms.CharField(label='password', widget=forms.PasswordInput)

    if request.method == "POST":
        form = loginform(request.POST)
        user = authenticate(username=form.data['username'],
                            password=form.data['password'])
        if user is not None:
            login(request, user)
            return redirect("/mysite")

    return render(request, "login.html", {"form": loginform()})


def logoutme(request):
    if request.user != "AnonymousUser":
        logout(request)
        return redirect("/mysite")
    else:
        return redirect("/mysite/login")
