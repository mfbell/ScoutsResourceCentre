# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BadgeInfo', '0004_auto_20171128_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='stage',
            field=models.IntegerField(default=0, help_text='Stage, only for staged badges.', null=True),
        ),
    ]
