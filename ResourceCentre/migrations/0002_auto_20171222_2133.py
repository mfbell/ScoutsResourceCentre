# Generated by Django 2.0 on 2017-12-22 21:33

import ResourceCentre.models.base
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResourceCentre', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='external_id',
            field=models.CharField(default=ResourceCentre.models.base.external_id, editable=False, help_text='Unique, static id for external use.', max_length=6, unique=True),
        ),
        migrations.AddField(
            model_name='camp',
            name='external_id',
            field=models.CharField(default=ResourceCentre.models.base.external_id, editable=False, help_text='Unique, static id for external use.', max_length=6, unique=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='external_id',
            field=models.CharField(default=ResourceCentre.models.base.external_id, editable=False, help_text='Unique, static id for external use.', max_length=6, unique=True),
        ),
        migrations.AddField(
            model_name='riskassessment',
            name='external_id',
            field=models.CharField(default=ResourceCentre.models.base.external_id, editable=False, help_text='Unique, static id for external use.', max_length=6, unique=True),
        ),
        migrations.AddField(
            model_name='riskassessmentelement',
            name='external_id',
            field=models.CharField(default=ResourceCentre.models.base.external_id, editable=False, help_text='Unique, static id for external use.', max_length=6, unique=True),
        ),
    ]
