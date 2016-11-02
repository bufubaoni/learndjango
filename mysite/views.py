from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render, redirect

# Create your views here.
from requests import sessions
from river.models import State

from mysite.models import MyModel
import pdb


def test(request):
    # my = MyModel.objects.get(pk=2)
    # user = User.objects.get(username=request.user)
    # my.proceed(user)
    # my.proceed(user, next_state=State.objects.get(label='start'))
    return render(request, "test.html", {"test1": request.user})


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
