# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0006_remove_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='model_pic',
            field=models.ImageField(blank=True, default='static/img/None/no-img.jpg', null=True, upload_to='charity/static/img/'),
        ),
    ]
