#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/11/25
from django.views import View

from mysite.models import CustomUser, MenuItem
from django.views.generic.detail import SingleObjectMixin, ContextMixin
import pdb


class MenuMixin(ContextMixin):
    def get_nodes(self):
        nodes=0
        return nodes
    def get_context_data(self, **kwargs):
        context = super(MenuMixin, self).get_context_data(**kwargs)
        context['nodes'] = self.get_nodes()
        return context
