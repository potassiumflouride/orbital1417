# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-18 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pairing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pairing',
            name='jax',
        ),
        migrations.AddField(
            model_name='pairing',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pairing',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]
