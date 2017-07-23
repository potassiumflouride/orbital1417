# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-23 12:33
from __future__ import unicode_literals

from django.db import migrations, models
import pairing.models


class Migration(migrations.Migration):

    dependencies = [
        ('pairing', '0004_remove_pairing_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='pairing',
            name='img',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=pairing.models.upload_location, width_field='width_field'),
        ),
    ]
