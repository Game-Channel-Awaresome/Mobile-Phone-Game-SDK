# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20160910_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='pay_callback_url',
            field=models.URLField(default='', max_length=256, verbose_name='\u652f\u4ed8\u56de\u8c03\u5730\u5740'),
        ),
    ]
