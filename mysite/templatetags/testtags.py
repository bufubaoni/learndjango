#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import template

register = template.Library()


class TestNode(template.Node):
    def __init__(self):
        pass

    def render(self, context):
        return "xxxxx"

@register.tag
def my_tag(parser, token):
    return TestNode()

