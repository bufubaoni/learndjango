# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 14:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0018_auto_20161111_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='menu_item',
            field=models.ForeignKey(help_text='\u83dc\u5355', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to='mysite.MenuGroup'),
        ),
    ]
