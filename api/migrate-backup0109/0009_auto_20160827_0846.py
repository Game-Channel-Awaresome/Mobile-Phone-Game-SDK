# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20160826_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='appsecret',
            field=models.CharField(default='', max_length=128, verbose_name='App Secret Key'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(db_index=True, max_length=128, null=True, unique=True, verbose_name='User User'),
        ),
    ]
