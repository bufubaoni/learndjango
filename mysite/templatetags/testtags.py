#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import template
from django.template.loader import get_template, select_template

register = template.Library()


class TestNode(template.Node):
    # app_dirname = "mysite"
    def __init__(self, content):
        params = content.copy()
        super(TestNode, self).__init__(params)

        self.content = content

    def render(self, context):
        c = self.content.resolve(context)
        print(c)
        t = get_template("form.html")
        context.update({'test': c})
        return t.render(context.flatten())


@register.tag
def my_tag(parser, token):
    bits = token.split_contents()
    print(bits)
    bits.pop(0)
    c = parser.compile_filter(bits.pop(0))
    print(c)
    return TestNode(c)
