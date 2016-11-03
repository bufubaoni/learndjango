#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.test),
    url(r'^login/$', views.loginme, name="login"),
    url(r'^logout/$', views.logoutme, name="logout"),
    url(r'^addmodel/$',views.addmodel,name="addmodel"),
    url(r'^promodel/$', views.promodel, name="promodel"),
    url(r'^addsomework/$', views.addsomework, name="addsomework"),
    url(r'^addsomework/(<?work_id[0-9]+>)$', views.someworkstat, name="someworkstat"),
    # url(r'^promodel/(?P<test_id>[0-9]+)$', views.promodel, name="promodel")
]
