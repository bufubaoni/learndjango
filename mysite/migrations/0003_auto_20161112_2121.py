# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 13:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20161112_2119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='menu_item',
            new_name='menugroup',
        ),
        migrations.RenameField(
            model_name='menugroup',
            old_name='menu_item',
            new_name='menu',
        ),
    ]
