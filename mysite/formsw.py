#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from uni_form.helper import FormHelper
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

CRISPY_CLASS_CONVERTERS = {'textinput': "textinput inputtext"}
class ExampleForm(forms.Form):

    testflow = forms.CharField(
        label="testflow",
        max_length=80,
        required=True,
    )


    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        favorite_food = forms.CharField(
            label="What is your favorite food?",
            max_length=80,
            required=True,
        )
        # self.helper.template = "boostrap3/inlineform.html"
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.add_input(Submit('submit', 'Submit'))
