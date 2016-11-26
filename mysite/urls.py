#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.test),
    url(r'^login/$', views.loginme, name="login"),
    url(r'^logout/$', views.logoutme, name="logout"),
    url(r'^addmodel/$', views.addmodel, name="addmodel"),
    url(r'^promodel/(?P<md_id>[0-9]+)/$', views.promodel, name="promodel"),
    url(r'^addsomework/$', views.addsomework, name="addsomework"),
    url(r'^addsomework/(?P<work_id>[0-9]+)/$', views.someworkstat, name="someworkstat"),
    url(r'^checkwork/(?P<work_id>[0-9]+)/$', views.checkwork, name="checkwork"),
    url(r'^bohuiqingjia/(?P<md_id>[0-9]+)/$', views.bohuiqingjia, name="bohuiqingjia"),
    url(r'^pizhun/(?P<md_id>[0-9]+)/$', views.pizhun, name="pizhun"),
    # url(r'^promodel/(?P<test_id>[0-9]+)$', views.promodel, name="promodel"),
    url(r'^testcvb/', views.cvb.as_view()),
    url(r'^testupload/',views.testupload.as_view())
]
