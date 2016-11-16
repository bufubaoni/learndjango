#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import template
from django.template.loader import get_template, select_template

register = template.Library()


class TestNode(template.Node):
    def __init__(self, content):
        super(TestNode, self).__init__()
        self.content = content
        pass

    def render(self, context):
        c = self.content.resolve(context)
        print(c)
        t = get_template("form.html")
        context.update({'test': c})
        # context["test"]
        return t.render(context.flatten())


@register.tag
def my_tag(parser, token):
    bits = token.split_contents()
    print(bits)
    bits.pop(0)
    c = parser.compile_filter(bits.pop(0))
    print(c)
    return TestNode(c)
