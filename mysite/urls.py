#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.test),
    url(r'^login/$', views.loginme, name="login"),
    url(r'^logout/$', views.logoutme, name="logout")
]
