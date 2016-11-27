#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/11/25
from django.views import View

from mysite.models import CustomUser, MenuItem
from django.views.generic.detail import SingleObjectMixin, ContextMixin
import pdb


class MenuMixin(object):
    def get_menu_response(self, request, **kwargs):
        return CustomUser.objects.get(user=request.user.pk).menugroup.menu.get_descendants()
