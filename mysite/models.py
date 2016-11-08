# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from river.models.fields.state import StateField
from river.models.managers.wofkflow_object import WorkflowObjectManager
from treebeard.mp_tree import MP_Node
import sys
from mptt.models import MPTTModel, TreeForeignKey

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


class somework(models.Model):
    title = models.CharField(max_length=100, verbose_name="题目")
    content = models.TextField(verbose_name="汇报")
    state = StateField(verbose_name="提交状态")
    objects = WorkflowObjectManager()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class menu_item(MPTTModel):
    name = models.CharField(max_length=50, unique=True, verbose_name='菜单名称')
    icon = models.CharField(max_length=50, null=True, blank=True, verbose_name='图标')
    uil = models.CharField(max_length=100, verbose_name='链接')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children',
                            db_index=True,verbose_name='父节点')

    def __unicode__(self):
        return self.name
