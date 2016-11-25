# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from hijack_admin.admin import HijackUserAdminMixin
from .models import MyModel, somework, MenuItem, CustomUser, MenuGroup
from mptt.admin import DraggableMPTTAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdim
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(somework)
admin.site.register(MenuGroup)
admin.site.register(MenuItem, DraggableMPTTAdmin)


class Custom(admin.StackedInline):
    model = CustomUser
    can_delete = False
    verbose_name_plural = "扩展属性"


class UserAdmin(BaseUserAdim, HijackUserAdminMixin):
    list_display = ("username", "email", "is_superuser", "hijack_field")
    inlines = (Custom,)



class MyModelAdmin(admin.ModelAdmin):
    list_display = ('id','testflow', 'state')


admin.site.register(MyModel, MyModelAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
