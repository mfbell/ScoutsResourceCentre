# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 20:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desciption', models.TextField(blank=True, help_text='Badge description, can be html.')),
                ('categoty', models.CharField(choices=[('CO', 'Core Badge'), ('AW', 'Awards'), ('CH', 'Challenge Awards'), ('AC', 'Activity Badges'), ('ST', 'Staged Badges'), ('YL', 'Young Leader Award')], default='CH', help_text='Badge type.', max_length=2)),
                ('url', models.URLField(help_text="Link to the badge's page on members.scouts.org.uk.")),
                ('notes', models.TextField(blank=True, help_text='Exta infomation, can be html.')),
                ('guidance_for_leaders', models.TextField(blank=True, help_text='Guidance for Leaders, can be html.')),
                ('stage', models.IntegerField(default=0, help_text='Stage, only for staged badges.')),
                ('required_badges', models.ManyToManyField(blank=True, help_text='Required badges', related_name='_badge_required_badges_+', to='BadgeInfo.Badge')),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='Title, not html.', max_length=128)),
                ('beavers', models.BooleanField(default=False)),
                ('cubs', models.BooleanField(default=False)),
                ('scouts', models.BooleanField(default=True)),
                ('explorers', models.BooleanField(default=False)),
                ('network', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True, help_text='Date-time updated.')),
                ('requirement', models.TextField(help_text='The requirement, can be html.')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StagedBadgeCollection',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='Title, not html.', max_length=128)),
                ('beavers', models.BooleanField(default=False)),
                ('cubs', models.BooleanField(default=False)),
                ('scouts', models.BooleanField(default=True)),
                ('explorers', models.BooleanField(default=False)),
                ('network', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True, help_text='Date-time updated.')),
                ('desciption', models.TextField(blank=True, help_text='Staged badge collection description, can be html.')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='badge',
            name='requirements',
            field=models.ManyToManyField(help_text='Badge requirements.', related_name='badges', related_query_name='badge', to='BadgeInfo.Requirement'),
        ),
        migrations.AddField(
            model_name='badge',
            name='stage_towards',
            field=models.ForeignKey(blank=True, help_text='Staged badge collection, only for staged badges.', on_delete=django.db.models.deletion.CASCADE, related_name='stages', related_query_name='stage', to='BadgeInfo.StagedBadgeCollection'),
        ),
    ]
