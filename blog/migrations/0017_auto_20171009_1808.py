# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-09 15:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_post_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorytopost',
            name='category',
        ),
        migrations.RemoveField(
            model_name='categorytopost',
            name='post',
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(through='blog.TagToPost', to='blog.Tag'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=martor.models.MartorField(default=''),
        ),
        migrations.DeleteModel(
            name='CategoryToPost',
        ),
    ]