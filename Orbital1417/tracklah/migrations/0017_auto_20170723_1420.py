# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-23 06:20
from __future__ import unicode_literals

from django.db import migrations, models
import tracklah.models


class Migration(migrations.Migration):

    dependencies = [
        ('tracklah', '0016_auto_20170722_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='charpost',
            name='img1',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=tracklah.models.upload_location, width_field='width_field'),
        ),
        migrations.AddField(
            model_name='charpost',
            name='img2',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=tracklah.models.upload_location, width_field='width_field'),
        ),
    ]
