# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0013_auto_20161111_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='menugroup',
            name='note',
            field=models.CharField(help_text='\u8fd9\u91cc\u6dfb\u52a0\u5907\u6ce8', max_length=50, null=True, verbose_name='\u5907\u6ce8'),
        ),
    ]
