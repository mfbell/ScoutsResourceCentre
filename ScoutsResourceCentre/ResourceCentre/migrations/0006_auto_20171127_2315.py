# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 23:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResourceCentre', '0005_auto_20171127_2311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='time_length',
        ),
        migrations.AddField(
            model_name='activity',
            name='time',
            field=models.DurationField(default=datetime.timedelta(0, 3600), help_text='Activity length.'),
        ),
    ]
