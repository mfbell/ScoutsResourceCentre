# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 22:18
from __future__ import unicode_literals

import ResourceCentre.models.base
import ResourceCentre.models.events
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='A short, one-point title for your resources.', max_length=128)),
                ('desciption', models.TextField(help_text='Summerise  your resources.')),
                ('beavers', models.BooleanField(default=False, help_text='Is your resource aimed at the Beaver section?')),
                ('cubs', models.BooleanField(default=False, help_text='Is your resource aimed at the Cub section?')),
                ('scouts', models.BooleanField(default=True, help_text='Is your resource aimed at the Scout section?')),
                ('explorers', models.BooleanField(default=False, help_text='Is your resource aimed at the Explorer section?')),
                ('network', models.BooleanField(default=False, help_text='Is your resource aimed at the Beavers section?')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date-time created.')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Date-time updated.')),
                ('curated', models.BooleanField(default=False, help_text='Is the resource curated? Results in extra protection and restrictions.')),
                ('visibility', models.CharField(choices=[('PU', 'Public'), ('HI', 'Only you - hiden')], default='PU', help_text='Who the resource is visibly to.', max_length=2)),
                ('views', models.IntegerField(default=0)),
                ('plan', models.TextField(help_text='The event plan.')),
                ('resources', models.TextField(help_text='Resources needed to run the event.')),
                ('equipment', models.TextField(help_text='Equipment needed to run the event.')),
                ('location', models.CharField(help_text='Event location.', max_length=256)),
                ('leaders', models.IntegerField(help_text='Number of leaders needed.')),
                ('young_leaders', models.IntegerField(help_text='Number of young leaders.')),
                ('young_people', models.IntegerField(help_text='Number of young people.')),
                ('young_people_approx', models.BooleanField(default=False, help_text='Is the number of young people an approximate number?')),
                ('size', models.CharField(choices=[('ID', 'Individual'), ('PA', 'Patrol'), ('TR', 'Troop'), ('DI', 'District'), ('CO', 'County'), ('NA', 'National'), ('IN', 'International')], default='TR', help_text='Event size.', max_length=2)),
                ('inside_outside', models.CharField(choices=[('IN', 'Inside only'), ('OU', 'Outside only'), ('EI', 'Inside or outside'), ('BO', 'Inside and outside')], default='EI', help_text='Is the event inside, outside or both.', max_length=2)),
                ('cost_per_young_person', models.DecimalField(decimal_places=2, help_text='Cost per young person.', max_digits=11)),
                ('cost_approx', models.BooleanField(default=False, help_text='Is the cost per young person an approximate number?')),
                ('time_length', models.DurationField(help_text='Activity length.')),
                ('contributors', models.ManyToManyField(help_text='Users who have contributed to the resource.', related_name='activity_contributions', related_query_name='activity_contribution', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(editable=False, help_text='The orginal creator.', on_delete=models.SET(ResourceCentre.models.base.get_sentinel_user), related_name='activity_created_resources', related_query_name='activity_created_resource', to=settings.AUTH_USER_MODEL)),
                ('editors', models.ManyToManyField(help_text='Users with permission to edit the resource.', related_name='activity_editor_roles', related_query_name='activity_editor_role', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(help_text='The resource owner.', on_delete=models.SET(ResourceCentre.models.base.get_sentinel_user), related_name='activity_owned_resources', related_query_name='activity_owned_resource', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, help_text='For if the resource was a copy and edited, the parent.', on_delete=models.SET(ResourceCentre.models.base.get_sentinel_parent), related_name='activity_children', related_query_name='activity_child', to='ResourceCentre.Activity')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='A short, one-point title for your resources.', max_length=128)),
                ('desciption', models.TextField(help_text='Summerise  your resources.')),
                ('beavers', models.BooleanField(default=False, help_text='Is your resource aimed at the Beaver section?')),
                ('cubs', models.BooleanField(default=False, help_text='Is your resource aimed at the Cub section?')),
                ('scouts', models.BooleanField(default=True, help_text='Is your resource aimed at the Scout section?')),
                ('explorers', models.BooleanField(default=False, help_text='Is your resource aimed at the Explorer section?')),
                ('network', models.BooleanField(default=False, help_text='Is your resource aimed at the Beavers section?')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date-time created.')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Date-time updated.')),
                ('curated', models.BooleanField(default=False, help_text='Is the resource curated? Results in extra protection and restrictions.')),
                ('visibility', models.CharField(choices=[('PU', 'Public'), ('HI', 'Only you - hiden')], default='PU', help_text='Who the resource is visibly to.', max_length=2)),
                ('views', models.IntegerField(default=0)),
                ('plan', models.TextField(help_text='The event plan.')),
                ('resources', models.TextField(help_text='Resources needed to run the event.')),
                ('equipment', models.TextField(help_text='Equipment needed to run the event.')),
                ('location', models.CharField(help_text='Event location.', max_length=256)),
                ('leaders', models.IntegerField(help_text='Number of leaders needed.')),
                ('young_leaders', models.IntegerField(help_text='Number of young leaders.')),
                ('young_people', models.IntegerField(help_text='Number of young people.')),
                ('young_people_approx', models.BooleanField(default=False, help_text='Is the number of young people an approximate number?')),
                ('size', models.CharField(choices=[('ID', 'Individual'), ('PA', 'Patrol'), ('TR', 'Troop'), ('DI', 'District'), ('CO', 'County'), ('NA', 'National'), ('IN', 'International')], default='TR', help_text='Event size.', max_length=2)),
                ('inside_outside', models.CharField(choices=[('IN', 'Inside only'), ('OU', 'Outside only'), ('EI', 'Inside or outside'), ('BO', 'Inside and outside')], default='EI', help_text='Is the event inside, outside or both.', max_length=2)),
                ('nights', models.IntegerField(help_text='Number of nights')),
                ('start_time', models.TimeField(default=ResourceCentre.models.events.default_camp_start_time, help_text='Camp start time.')),
                ('end_time', models.TimeField(default=ResourceCentre.models.events.default_camp_end_time, help_text='Camp end time.')),
                ('site_cost_per_young_person_per_night', models.DecimalField(decimal_places=2, help_text='Site costs per young person per nights.', max_digits=11)),
                ('food_cost_per_young_person_per_day', models.DecimalField(decimal_places=2, help_text='Food costs per young person per day.', max_digits=11)),
                ('other_costs_per_young_person', models.DecimalField(decimal_places=2, help_text='Extra camp costs per young person.', max_digits=11)),
                ('activities', models.ManyToManyField(help_text='Activities happening at the camp.', related_name='camps', related_query_name='camp', to='ResourceCentre.Activity')),
                ('contributors', models.ManyToManyField(help_text='Users who have contributed to the resource.', related_name='camp_contributions', related_query_name='camp_contribution', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(editable=False, help_text='The orginal creator.', on_delete=models.SET(ResourceCentre.models.base.get_sentinel_user), related_name='camp_created_resources', related_query_name='camp_created_resource', to=settings.AUTH_USER_MODEL)),
                ('editors', models.ManyToManyField(help_text='Users with permission to edit the resource.', related_name='camp_editor_roles', related_query_name='camp_editor_role', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(help_text='The resource owner.', on_delete=models.SET(ResourceCentre.models.base.get_sentinel_user), related_name='camp_owned_resources', related_query_name='camp_owned_resource', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, help_text='For if the resource was a copy and edited, the parent.', on_delete=models.SET(ResourceCentre.models.base.get_sentinel_parent), related_name='camp_children', related_query_name='camp_child', to='ResourceCentre.Camp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='A short, one-point title for your resources.', max_length=128)),
                ('desciption', models.TextField(help_text='Summerise  your resources.')),
                ('beavers', models.BooleanField(default=False, help_text='Is your resource aimed at the Beaver section?')),
                ('cubs', models.BooleanField(default=False, help_text='Is your resource aimed at the Cub section?')),
                ('scouts', models.BooleanField(default=True, help_text='Is your resource aimed at the Scout section?')),
                ('explorers', models.BooleanField(default=False, help_text='Is your resource aimed at the Explorer section?')),
                ('network', models.BooleanField(default=False, help_text='Is your resource aimed at the Beavers section?')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date-time created.')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Date-time updated.')),
                ('curated', models.BooleanField(default=False, help_text='Is the resource curated? Results in extra protection and restrictions.')),
                ('visibility', models.CharField(choices=[('PU', 'Public'), ('HI', 'Only you - hiden')], default='PU', help_text='Who the resource is visibly to.', max_length=2)),
                ('views', models.IntegerField(default=0)),
                ('plan', models.TextField(help_text='The event plan.')),
                ('resources', models.TextField(help_text='Resources needed to run the event.')),
                ('equipment', models.TextField(help_text='Equipment needed to run the event.')),
                ('location', models.CharField(help_text='Event location.', max_length=256)),
                ('leaders', models.IntegerField(help_text='Number of leaders needed.')),
                ('young_leaders', models.IntegerField(help_text='Number of young leaders.')),
                ('young_people', models.IntegerField(help_text='Number of young people.')),
                ('young_people_approx', models.BooleanField(default=False, help_text='Is the number of young people an approximate number?')),
                ('size', models.CharField(choices=[('ID', 'Individual'), ('PA', 'Patrol'), ('TR', 'Troop'), ('DI', 'District'), ('CO', 'County'), ('NA', 'National'), ('IN', 'International')], default='TR', help_text='Event size.', max_length=2)),
                ('inside_outside', models.CharField(choices=[('IN', 'Inside only'), ('OU', 'Outside only'), ('EI', 'Inside or outside'), ('BO', 'Inside and outside')], default='EI', help_text='Is the event inside, outside or both.', max_length=2)),
                ('extra_costs_per_young_person', models.DecimalField(decimal_places=2, help_text='Extra meeting costs per young person.', max_digits=11)),
                ('extra_cost_approx', models.BooleanField(default=False, help_text='Is the extra costs per young person an approximate number?')),
                ('extra_time', models.DurationField(help_text='Extra time needed for the meeting.')),
                ('activities', models.ManyToManyField(help_text='Activities happening at the meeting.', related_name='meetings', related_query_name='meeting', to='ResourceCentre.Activity')),
                ('contributors', models.ManyToManyField(help_text='Users who have contributed to the resource.', related_name='meeting_contributions', related_query_name='meeting_contribution', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(editable=False, help_text='The orginal creator.', on_delete=models.SET(ResourceCentre.models.base.get_sentinel_user), related_name='meeting_created_resources', related_query_name='meeting_created_resource', to=settings.AUTH_USER_MODEL)),
                ('editors', models.ManyToManyField(help_text='Users with permission to edit the resource.', related_name='meeting_editor_roles', related_query_name='meeting_editor_role', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(help_text='The resource owner.', on_delete=models.SET(ResourceCentre.models.base.get_sentinel_user), related_name='meeting_owned_resources', related_query_name='meeting_owned_resource', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, help_text='For if the resource was a copy and edited, the parent.', on_delete=models.SET(ResourceCentre.models.base.get_sentinel_parent), related_name='meeting_children', related_query_name='meeting_child', to='ResourceCentre.Meeting')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RiskAssessment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='A short, one-point title for your resources.', max_length=128)),
                ('desciption', models.TextField(help_text='Summerise  your resources.')),
                ('beavers', models.BooleanField(default=False, help_text='Is your resource aimed at the Beaver section?')),
                ('cubs', models.BooleanField(default=False, help_text='Is your resource aimed at the Cub section?')),
                ('scouts', models.BooleanField(default=True, help_text='Is your resource aimed at the Scout section?')),
                ('explorers', models.BooleanField(default=False, help_text='Is your resource aimed at the Explorer section?')),
                ('network', models.BooleanField(default=False, help_text='Is your resource aimed at the Beavers section?')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date-time created.')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Date-time updated.')),
                ('curated', models.BooleanField(default=False, help_text='Is the resource curated? Results in extra protection and restrictions.')),
                ('visibility', models.CharField(choices=[('PU', 'Public'), ('HI', 'Only you - hiden')], default='PU', help_text='Who the resource is visibly to.', max_length=2)),
                ('views', models.IntegerField(default=0)),
                ('contributors', models.ManyToManyField(help_text='Users who have contributed to the resource.', related_name='riskassessment_contributions', related_query_name='riskassessment_contribution', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(editable=False, help_text='The orginal creator.', on_delete=models.SET(ResourceCentre.models.base.get_sentinel_user), related_name='riskassessment_created_resources', related_query_name='riskassessment_created_resource', to=settings.AUTH_USER_MODEL)),
                ('editors', models.ManyToManyField(help_text='Users with permission to edit the resource.', related_name='riskassessment_editor_roles', related_query_name='riskassessment_editor_role', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RiskAssessmentElement',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='A short, one-point title for your resources.', max_length=128)),
                ('desciption', models.TextField(help_text='Summerise  your resources.')),
                ('beavers', models.BooleanField(default=False, help_text='Is your resource aimed at the Beaver section?')),
                ('cubs', models.BooleanField(default=False, help_text='Is your resource aimed at the Cub section?')),
                ('scouts', models.BooleanField(default=True, help_text='Is your resource aimed at the Scout section?')),
                ('explorers', models.BooleanField(default=False, help_text='Is your resource aimed at the Explorer section?')),
                ('network', models.BooleanField(default=False, help_text='Is your resource aimed at the Beavers section?')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date-time created.')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Date-time updated.')),
                ('curated', models.BooleanField(default=False, help_text='Is the resource curated? Results in extra protection and restrictions.')),
                ('visibility', models.CharField(choices=[('PU', 'Public'), ('HI', 'Only you - hiden')], default='PU', help_text='Who the resource is visibly to.', max_length=2)),
                ('views', models.IntegerField(default=0)),
                ('risk', models.CharField(help_text='State the risk.', max_length=128)),
                ('cause', models.CharField(help_text='State the cause.', max_length=256)),
                ('affects', models.CharField(choices=[('LE', 'Leaders'), ('YP', 'Young people'), ('EV', 'Everyone')], default='EV', help_text='Who is at risk.', max_length=2)),
                ('mitigations', models.CharField(help_text='How will you reduce the risk?', max_length=256)),
                ('severity', models.CharField(choices=[('NE', 'Negligible'), ('LO', 'Low'), ('ME', 'Medium'), ('HI', 'High')], default='ME', help_text='The severity of the risk after mitigation.', max_length=2)),
                ('chance', models.CharField(choices=[('NE', 'Negligible'), ('LO', 'Low'), ('ME', 'Medium'), ('HI', 'High')], default='LO', help_text='The chance of the risk after mitigation.', max_length=2)),
                ('responce', models.CharField(help_text='How to respond to an incident.', max_length=256)),
                ('contributors', models.ManyToManyField(help_text='Users who have contributed to the resource.', related_name='riskassessmentelement_contributions', related_query_name='riskassessmentelement_contribution', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(editable=False, help_text='The orginal creator.', on_delete=models.SET(ResourceCentre.models.base.get_sentinel_user), related_name='riskassessmentelement_created_resources', related_query_name='riskassessmentelement_created_resource', to=settings.AUTH_USER_MODEL)),
                ('editors', models.ManyToManyField(help_text='Users with permission to edit the resource.', related_name='riskassessmentelement_editor_roles', related_query_name='riskassessmentelement_editor_role', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(help_text='The resource owner.', on_delete=models.SET(ResourceCentre.models.base.get_sentinel_user), related_name='riskassessmentelement_owned_resources', related_query_name='riskassessmentelement_owned_resource', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, help_text='For if the resource was a copy and edited, the parent.', on_delete=models.SET(ResourceCentre.models.base.get_sentinel_parent), related_name='riskassessmentelement_children', related_query_name='riskassessmentelement_child', to='ResourceCentre.RiskAssessmentElement')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='riskassessment',
            name='elements',
            field=models.ManyToManyField(help_text='Risk asessments are made up of individual risk assessments for reusability.', related_name='risk_assessments', related_query_name='risk_assessment', to='ResourceCentre.RiskAssessmentElement'),
        ),
        migrations.AddField(
            model_name='riskassessment',
            name='owner',
            field=models.ForeignKey(help_text='The resource owner.', on_delete=models.SET(ResourceCentre.models.base.get_sentinel_user), related_name='riskassessment_owned_resources', related_query_name='riskassessment_owned_resource', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='riskassessment',
            name='parent',
            field=models.ForeignKey(blank=True, help_text='For if the resource was a copy and edited, the parent.', on_delete=models.SET(ResourceCentre.models.base.get_sentinel_parent), related_name='riskassessment_children', related_query_name='riskassessment_child', to='ResourceCentre.RiskAssessment'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='risk_assessment',
            field=models.ForeignKey(help_text='Event risk assessment.', on_delete=django.db.models.deletion.PROTECT, related_name='meeting_events', related_query_name='meeting_event', to='ResourceCentre.RiskAssessment'),
        ),
        migrations.AddField(
            model_name='camp',
            name='risk_assessment',
            field=models.ForeignKey(help_text='Event risk assessment.', on_delete=django.db.models.deletion.PROTECT, related_name='camp_events', related_query_name='camp_event', to='ResourceCentre.RiskAssessment'),
        ),
        migrations.AddField(
            model_name='activity',
            name='risk_assessment',
            field=models.ForeignKey(help_text='Event risk assessment.', on_delete=django.db.models.deletion.PROTECT, related_name='activity_events', related_query_name='activity_event', to='ResourceCentre.RiskAssessment'),
        ),
    ]
