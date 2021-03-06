# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20160826_0643'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name='User ID')),
                ('phone', models.CharField(blank=True, max_length=128, null=True, unique=True, verbose_name='User Phone Number')),
                ('username', models.CharField(max_length=128, null=True, unique=True, verbose_name='User User')),
                ('imei', models.CharField(blank=True, db_index=True, max_length=128, null=True, verbose_name='User imei')),
                ('password_hash', models.CharField(max_length=128, verbose_name='user password hash')),
                ('password_salt', models.CharField(max_length=128, verbose_name='user password slat')),
                ('verify_code', models.CharField(max_length=128, null=True, verbose_name='verify code for reset password')),
                ('verify_code_create_at', models.DateTimeField(db_index=True, null=True, verbose_name='verify code create at')),
                ('verify_code_expire_at', models.DateTimeField(db_index=True, null=True, verbose_name='verify code expire at')),
                ('guid', models.CharField(db_index=True, max_length=128, null=True, verbose_name='guid')),
                ('create_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='create at')),
                ('register_at', models.DateTimeField(db_index=True, null=True, verbose_name='register at')),
            ],
        ),
    ]
