# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 06:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import river.models.fields.state


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('river', '0008_auto_20161017_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(help_text='\u8f93\u5165\u7535\u8bdd\u53f7\u7801', max_length=16, null=True, verbose_name='\u7535\u8bdd')),
            ],
        ),
        migrations.CreateModel(
            name='MenuGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='\u83dc\u5355\u5206\u7ec4', max_length=16, verbose_name='\u540d\u79f0')),
                ('note', models.CharField(help_text='\u8fd9\u91cc\u6dfb\u52a0\u5907\u6ce8', max_length=50, null=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u83dc\u5355\u540d\u79f0')),
                ('icon', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u56fe\u6807')),
                ('uil', models.CharField(max_length=100, verbose_name='\u94fe\u63a5')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_item', to='mysite.MenuItem', verbose_name='\u7236\u8282\u70b9')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testflow', models.CharField(default='6666', max_length=50, verbose_name='\u6d4b\u8bd5')),
                ('state', river.models.fields.state.StateField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='river.State', verbose_name='\u72b6\u6001')),
            ],
        ),
        migrations.CreateModel(
            name='somework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u9898\u76ee')),
                ('content', models.TextField(verbose_name='\u6c47\u62a5')),
                ('state', river.models.fields.state.StateField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='river.State', verbose_name='\u63d0\u4ea4\u72b6\u6001')),
            ],
        ),
        migrations.AddField(
            model_name='menugroup',
            name='menu',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menuitem', to='mysite.MenuItem', verbose_name='\u83dc\u5355'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='menugroup',
            field=models.ForeignKey(help_text='\u83dc\u5355', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='menugroup', to='mysite.MenuGroup'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
