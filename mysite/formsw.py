#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from uni_form.helper import FormHelper
from crispy_forms.bootstrap import StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div
from django import forms

CRISPY_CLASS_CONVERTERS = {'textinput': "textinput inputtext"}


class ExampleForm(forms.Form):
    testflow = forms.CharField(
        label="工作流程",
        help_text="请假管理",
        max_length=80,
    )
    datetime = forms.DateTimeField(
        label="时间",
    )

    file = forms.ImageField(
        label="文件",
        help_text="正面照片",
    )
    file2 = forms.ImageField(
        label="文件2"
    )

    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.field_template = "form/customField.html"
        self.helper.layout = Layout(
            'testflow', 'datetime','file', 'file2',
            Div(StrictButton('添加', css_class='btn-success'),
                StrictButton('取消', css_class='btn-default'),
                css_class="col-md-offset-2 col-md-9"))
