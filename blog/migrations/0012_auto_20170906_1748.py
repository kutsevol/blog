# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-06 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170906_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preview_image_height',
            field=models.PositiveIntegerField(blank=True, default='100', editable=False, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='preview_image_width',
            field=models.PositiveIntegerField(blank=True, default='100', editable=False, null=True),
        ),
    ]
