# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 20:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BadgeInfo', '0007_remove_badge_stage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='badge',
            name='stage_towards',
        ),
    ]
