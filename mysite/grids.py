#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models import MyModel
import django_tables2 as tables


class MyModelTable(tables.Table):
    class Meta:
        model = MyModel
        attrs = {'class': 'table  table-bordered table-hover'}

    def render_id(self, value):
        return '%s' % value

    def render_state(self, value):
        return '%s' % value
