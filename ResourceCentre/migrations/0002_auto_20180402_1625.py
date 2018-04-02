# Generated by Django 2.0.3 on 2018-04-02 15:25

import uuid

import ResourceCentre.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('ResourceCentre', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourceslug',
            name='content_type',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resourceslug',
            name='resource_id',
            field=models.UUIDField(default=uuid.uuid4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activitystageimage',
            name='image',
            field=models.ImageField(upload_to=ResourceCentre.models.activity_stage_image_filename),
        ),
    ]
