#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import template
from django.template.loader import get_template, select_template

register = template.Library()


class TestNode(template.Node):
    def __init__(self, content):
        self.content = content
        pass

    def render(self, context):
        t = get_template("form.html")
        context.update({'test': self.content})
        # context["test"]
        return t.render(context.flatten())


@register.tag
def my_tag(parser, token):
    return TestNode("999999")
