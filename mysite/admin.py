# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from hijack_admin.admin import HijackUserAdminMixin
from .models import MyModel, somework, MenuItem, CustomUser, MenuGroup
from mptt.admin import DraggableMPTTAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdim
from django.contrib.auth.models import User
from djcelery.models import TaskMeta

# Register your models here.

# class MenuItemAdmin(DraggableMPTTAdmin):
#     # super.__init__()
#     list_display = ('id', 'name', 'uil')



admin.site.register(somework)
admin.site.register(MenuGroup)
admin.site.register(MenuItem, DraggableMPTTAdmin,
                    list_display=('tree_actions', 'indented_title', 'icon', 'uil'),
                    list_display_links=(
                        'indented_title',
                    ), )


class TaskAdmin(admin.ModelAdmin):
    def task(self, obj):
        # import pdb
        # pdb.set_trace()
        return 1

    list_display = ('id', "task_id", 'status', 'task', 'result','meta')


admin.site.register(TaskMeta, TaskAdmin)


class Custom(admin.StackedInline):
    model = CustomUser
    can_delete = False
    verbose_name_plural = "扩展属性"


class UserAdmin(BaseUserAdim, HijackUserAdminMixin):
    list_display = ("username", "email", "is_superuser", "hijack_field")
    inlines = (Custom,)


class MyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'testflow', 'state',)


admin.site.register(MyModel, MyModelAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
