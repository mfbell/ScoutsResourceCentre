# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 23:23
from __future__ import unicode_literals

import ResourceCentre.models.events
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResourceCentre', '0008_auto_20171127_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='time',
            field=models.DurationField(help_text='Activity length.'),
        ),
    ]
