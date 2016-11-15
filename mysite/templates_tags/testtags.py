#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import template

class TestTage(template.Node):
    def __init__(self):
        self.tag="666666"
    def render(self, context):
        context["test"] = self.tag
        return ""