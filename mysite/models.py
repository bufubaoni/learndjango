# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from river.models.fields.state import StateField
from river.models.managers.wofkflow_object import WorkflowObjectManager
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

# Create your models here.


class MyModel(models.Model):
    testflow = models.CharField(max_length=50, default="6666", verbose_name="测试")
    state = StateField(verbose_name="状态")
    objects = WorkflowObjectManager()


    def __unicode__(self):
        return self.testflow

    def __str__(self):
        return self.testflow
