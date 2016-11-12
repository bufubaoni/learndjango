# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
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


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=16, null=True, verbose_name="电话",
                              help_text="输入电话号码")
    menugroup = models.ForeignKey("MenuGroup", null=True, on_delete=models.SET_NULL,
                                  help_text="菜单", related_name='menugroup')


class MenuGroup(models.Model):
    name = models.CharField(max_length=16, verbose_name="名称", help_text="菜单分组")
    note = models.CharField(max_length=50, null=True, verbose_name="备注",
                            help_text="这里添加备注")
    menu = models.OneToOneField("MenuItem", verbose_name="菜单", null=True, blank=True,
                                related_name="menuitem")

    def __unicode__(self):
        return self.name


class MenuItem(MPTTModel):
    name = models.CharField(max_length=50, verbose_name='菜单名称')
    icon = models.CharField(max_length=50, null=True, blank=True, verbose_name='图标')
    uil = models.CharField(max_length=100, verbose_name='链接')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='menu_item',
                            db_index=True, verbose_name='父节点')

    def __unicode__(self):
        return self.name
