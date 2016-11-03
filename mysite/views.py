# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render, redirect

# Create your views here.
from django.utils import six
from requests import sessions
from river.models import State

from mysite.models import MyModel, somework
import pdb


def test(request):
    task = MyModel.objects.all()
    return render(request, "test.html", {"user": request.user, "task": task})


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


def addmodel(request):
    class Taskflow(forms.Form):
        testflow = forms.CharField(label="testflow")

    if request.method == "POST":
        form = Taskflow(request.POST)
        my = MyModel.objects.create(testflow=form.data["testflow"].encode("utf8"))
        type(request.user)
        my.proceed(request.user)
        return redirect("/mysite")
    else:
        return render(request, "taskflow.html", {"form": Taskflow()})


def promodel(request):
    task = MyModel.objects.get(pk=5)
    # task = MyModel.objects.all()
    task.proceed(request.user)
    return render(request, "promodel.html", {"task": task})


def addsomework(request):
    class SomeWork(forms.Form):
        title = forms.CharField(label="题目")
        content = forms.CharField(label="内容")

    if request.method == "POST":
        form = SomeWork(request.POST)
        work = somework.object.create(title=form.data["title"],
                                      content=form.data["content"])
        work.proceed(request.user)
        return redirect("/mysite")
    else:
        return render(request, "addsomework.html", {"form": SomeWork()})


def someworkstat(request, work_id):
    work = somework.objects.get(pk=work_id)
    return render(request, "someworkstat.html", {"work": work})


def checkwork(request, work_id):
    work = somework.objects.get(pk=work_id)
    work.proceed(request.user)
    return redirect("/someworkstat", (work_id,))
