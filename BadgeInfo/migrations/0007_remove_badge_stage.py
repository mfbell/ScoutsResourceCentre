# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 20:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BadgeInfo', '0006_auto_20171128_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='badge',
            name='stage',
        ),
    ]
