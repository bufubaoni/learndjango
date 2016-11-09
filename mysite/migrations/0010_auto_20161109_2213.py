# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-09 14:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_auto_20161109_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='menu_item',
            field=models.ForeignKey(help_text='\u83dc\u5355', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='\u8fd9\u4e2a+', to='mysite.menu_item'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
