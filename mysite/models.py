# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from river.models.fields.state import StateField
from river.models.managers.wofkflow_object import WorkflowObjectManager


# Create your models here.


class MyModel(models.Model):
    testflow = models.CharField(max_length=50, default="6666", verbose_name="测试")
    state = StateField()
    mnage = WorkflowObjectManager()

    def __unicode__(self):
        return self.testflow