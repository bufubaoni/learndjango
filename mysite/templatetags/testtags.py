#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import template
from django.template.loader import get_template, select_template

register = template.Library()


class TestNode(template.Node):
    def __init__(self):
        pass

    def render(self, context):
        t = get_template("form.html")
        context.update({'test': "66666666"})
        # context["test"]
        return t.render(context.flatten())


@register.tag
def my_tag(parser, token):
    return TestNode()
